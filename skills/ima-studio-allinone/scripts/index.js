#!/usr/bin/env node

/**
 * IMA studio All-in-One - OpenClaw Skill
 * 全能音频/视频处理工具
 */

const { exec } = require('child_process');
const path = require('path');
const fs = require('fs');
const { promisify } = require('util');
const execAsync = promisify(exec);

// 配置
const CONFIG = {
  ffmpeg: process.env.FFMPEG_PATH || 'ffmpeg',
  ffprobe: process.env.FFPROBE_PATH || 'ffprobe',
  tempDir: process.env.TEMP_DIR || path.join(__dirname, '..', 'temp'),
  logLevel: process.env.LOG_LEVEL || 'info'
};

// 日志函数
function log(level, message) {
  const levels = { debug: 0, info: 1, warn: 2, error: 3 };
  if (levels[level] >= levels[CONFIG.logLevel]) {
    console.log(`[${level.toUpperCase()}] ${message}`);
  }
}

// 主处理函数
async function processAction(params) {
  const { action, input, output, ...options } = params;

  log('info', `开始执行动作: ${action}`);
  log('debug', `输入: ${input}`);
  log('debug', `输出: ${output}`);
  log('debug', `参数: ${JSON.stringify(options)}`);

  // 确保输入文件存在
  if (!fs.existsSync(input)) {
    throw new Error(`输入文件不存在: ${input}`);
  }

  // 确保输出目录存在
  if (output) {
    const outputDir = path.dirname(output);
    if (!fs.existsSync(outputDir)) {
      fs.mkdirSync(outputDir, { recursive: true });
    }
  }

  switch (action) {
    case 'audio-convert':
      return await audioConvert(input, output, options);
    case 'video-compress':
      return await videoCompress(input, output, options);
    case 'batch-convert':
      return await batchConvert(input, output, options);
    case 'media-info':
      return await mediaInfo(input, output, options);
    case 'audio-extract':
      return await audioExtract(input, output, options);
    case 'video-screenshot':
      return await videoScreenshot(input, output, options);
    default:
      throw new Error(`未知动作: ${action}`);
  }
}

// 音频转换
async function audioConvert(input, output, options) {
  const { format = 'wav', bitrate, sampleRate, channels } = options;

  const args = [
    '-i', input,
    '-vn',  // 无视频
  ];

  // 编解码器映射
  const codecMap = {
    'ima-adpcm': 'adpcm_ima_wav',
    'wav': 'pcm_s16le',
    'mp3': 'libmp3lame',
    'aac': 'aac',
    'flac': 'flac',
    'ogg': 'libvorbis'
  };

  if (codecMap[format]) {
    args.push('-acodec', codecMap[format]);
  } else {
    throw new Error(`不支持的音频格式: ${format}`);
  }

  // 码率
  if (bitrate) {
    args.push('-b:a', bitrate);
  }

  // 采样率
  if (sampleRate) {
    args.push('-ar', sampleRate.toString());
  }

  // 声道
  if (channels) {
    args.push('-ac', channels.toString());
  }

  args.push('-y');  // 覆盖输出
  args.push(output);

  log('info', `音频转换: ${input} → ${output}`);
  const { stdout, stderr } = await execAsync(`${CONFIG.ffmpeg} ${args.join(' ')}`);
  if (stdout) log('debug', stdout);
  if (stderr) log('warn', stderr);

  return { success: true, output };
}

// 视频压缩
async function videoCompress(input, output, options) {
  const {
    codec = 'h264',
    crf = 23,
    preset = 'medium',
    resolution,
    framerate,
    bitrate
  } = options;

  const args = [
    '-i', input,
    '-c:v', codec === 'h264' ? 'libx264' : codec === 'h265' ? 'libx265' : codec
  ];

  // CRF 质量参数
  if (crf) {
    args.push('-crf', crf.toString());
  }

  // 预设
  if (preset) {
    args.push('-preset', preset);
  }

  // 分辨率
  if (resolution && resolution !== 'keep') {
    args.push('-vf', `scale=${resolution}`);
  }

  // 帧率
  if (framerate) {
    args.push('-r', framerate.toString());
  }

  // 音频编码（默认 AAC）
  args.push('-c:a', 'aac');
  if (bitrate) {
    args.push('-b:a', bitrate);
  }

  args.push('-y');
  args.push(output);

  log('info', `视频压缩: ${input} → ${output} (codec: ${codec}, crf: ${crf})`);
  const { stdout, stderr } = await execAsync(`${CONFIG.ffmpeg} ${args.join(' ')}`);
  if (stdout) log('debug', stdout);
  if (stderr) log('warn', stderr);

  return { success: true, output };
}

// 批量处理
async function batchConvert(inputDir, outputDir, options) {
  const {
    targetFormat,
    concurrent = 2,
    recursive = false
  } = options;

  // 扫描文件
  const files = [];
  const scanDir = (dir) => {
    const items = fs.readdirSync(dir);
    for (const item of items) {
      const fullPath = path.join(dir, item);
      const stat = fs.statSync(fullPath);
      if (stat.isDirectory() && recursive) {
        scanDir(fullPath);
      } else if (stat.isFile()) {
        files.push(fullPath);
      }
    }
  };
  scanDir(inputDir);

  log('info', `发现 ${files.length} 个文件，并发数: ${concurrent}`);

  // 并发处理
  const results = [];
  for (let i = 0; i < files.length; i += concurrent) {
    const batch = files.slice(i, i + concurrent);
    const promises = batch.map(async (file) => {
      try {
        const relPath = path.relative(inputDir, file);
        const outFile = path.join(outputDir, relPath);
        const ext = path.extname(outFile);
        const base = path.basename(outFile, ext);
        const finalOutput = `${base}.${targetFormat}`;

        // 判断是音频还是视频
        const probeCmd = `${CONFIG.ffprobe} -v error -show_entries stream=codec_type -of json "${file}"`;
        const probeResult = await execAsync(probeCmd);
        const probeData = JSON.parse(probeResult.stdout);
        const hasVideo = probeData.streams.some(s => s.codec_type === 'video');

        if (hasVideo) {
          await videoCompress(file, finalOutput, { ...options, codec: 'h264' });
        } else {
          await audioConvert(file, finalOutput, { ...options, format: targetFormat });
        }

        return { file, output: finalOutput, success: true };
      } catch (err) {
        log('error', `处理失败 ${file}: ${err.message}`);
        return { file, success: false, error: err.message };
      }
    });

    const batchResults = await Promise.all(promises);
    results.push(...batchResults);
  }

  const successCount = results.filter(r => r.success).length;
  log('info', `批量处理完成: ${successCount}/${files.length} 成功`);

  return { success: true, total: files.length, success: successCount, results };
}

// 媒体信息
async function mediaInfo(input, output, options) {
  const { format = 'json' } = options;

  const probeCmd = `${CONFIG.ffprobe} -v error -show_format -show_streams -of json "${input}"`;
  const { stdout } = await execAsync(probeCmd);
  const data = JSON.parse(stdout);

  // 简化信息
  const info = {
    file: input,
    format: data.format.format_name,
    duration: parseFloat(data.format.duration).toFixed(2),
    size: data.format.size,
    bitrate: data.format.bit_rate,
    streams: data.streams.map(s => ({
      index: s.index,
      codec_type: s.codec_type,
      codec_name: s.codec_name,
      width: s.width,
      height: s.height,
      sample_rate: s.sample_rate,
      channels: s.channels
    }))
  };

  if (output) {
    const outContent = format === 'json' ? JSON.stringify(info, null, 2) : `Media Info:\n${JSON.stringify(info, null, 2)}`;
    fs.writeFileSync(output, outContent);
    log('info', `媒体信息已保存: ${output}`);
  }

  return { success: true, info };
}

// 音频提取
async function audioExtract(input, output, options) {
  const { format = 'mp3', bitrate = '128k' } = options;

  const args = [
    '-i', input,
    '-vn',  // 无视频
    '-acodec', format === 'mp3' ? 'libmp3lame' : format,
    '-b:a', bitrate,
    '-y',
    output
  ];

  log('info', `提取音频: ${input} → ${output}`);
  const { stdout, stderr } = await execAsync(`${CONFIG.ffmpeg} ${args.join(' ')}`);
  if (stdout) log('debug', stdout);
  if (stderr) log('warn', stderr);

  return { success: true, output };
}

// 视频截图
async function videoScreenshot(input, output, options) {
  const { time = '00:00:05', width, height } = options;

  const args = [
    '-i', input,
    '-ss', time,
    '-vframes', '1'
  ];

  if (width && height) {
    args.push('-vf', `scale=${width}:${height}`);
  }

  args.push('-y');
  args.push(output);

  log('info', `视频截图: ${input} @ ${time} → ${output}`);
  const { stdout, stderr } = await execAsync(`${CONFIG.ffmpeg} ${args.join(' ')}`);
  if (stdout) log('debug', stdout);
  if (stderr) log('warn', stderr);

  return { success: true, output };
}

// 主入口
async function main() {
  try {
    // 从参数或 stdin 读取配置
    let params;
    if (process.argv.length > 2) {
      // 从命令行参数读取（简化版）
      // 实际应解析 JSON 参数
      params = JSON.parse(process.argv[2]);
    } else {
      // 从 stdin 读取（OpenClaw 调用方式）
      const stdin = await promisify(fs.readFile)(0, 'utf8');
      params = JSON.parse(stdin);
    }

    const result = await processAction(params);
    console.log(JSON.stringify(result, null, 2));
    process.exit(0);
  } catch (err) {
    log('error', `执行失败: ${err.message}`);
    console.log(JSON.stringify({ success: false, error: err.message }, null, 2));
    process.exit(1);
  }
}

// 如果是直接执行，运行主函数
if (require.main === module) {
  main();
}

module.exports = { processAction, audioConvert, videoCompress, batchConvert, mediaInfo, audioExtract, videoScreenshot };
