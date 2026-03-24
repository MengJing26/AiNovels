# IMA studio All-in-One - OpenClaw Skill

[![OpenClaw Skill](https://img.shields.io/badge/OpenClaw-Skill-blue)](https://openclaw.ai)
[![Version](https://img.shields.io/badge/version-1.0.0-green)]()

全能音频/视频处理技能，集成 IMA ADPCM 编解码、格式转换、媒体分析、批量处理。

---

## 📦 安装

### 方式一：自动安装（推荐）

```bash
# 在 OpenClaw 终端执行
openclaw skills install ima-studio-allinone
```

### 方式二：手动安装

1. 克隆技能到 skills 目录：
```bash
cd ~/.openclaw/workspace/skills
git clone https://github.com/openclaw/ima-studio-allinone.git
```

2. 安装依赖：
```bash
cd ima-studio-allinone
npm install  # Node.js 依赖（主脚本需要）
# 如果使用 Python 分析功能
python -m pip install -r requirements.txt
```

3. 配置 FFmpeg：
   - 下载 FFmpeg：https://ffmpeg.org/download.html
   - 解压并加入系统 PATH，或修改 `config.yaml` 指定路径

4. 复制配置文件：
```bash
cp config.example.yaml config.yaml
# 编辑 config.yaml，设置 ffmpeg-path 等参数
```

5. 重启 OpenClaw Gateway：
```bash
openclaw gateway restart
```

---

## 🚀 快速开始

### 音频转换（WAV → IMA ADPCM）

```yaml
skill: ima-studio-allinone
action: audio-convert
input: "/music/input.wav"
output: "/music/output.ima"
format: ima-adpcm
bitrate: 64k
```

### 视频压缩

```yaml
skill: ima-studio-allinone
action: video-compress
input: "/video/input.mp4"
output: "/video/output.mp4"
codec: h264
crf: 23
preset: medium
```

### 批量转换文件夹

```yaml
skill: ima-studio-allinone
action: batch-convert
input-dir: "/videos/originals"
output-dir: "/videos/converted"
target-format: mp4
concurrent: 4
```

### 获取媒体信息

```yaml
skill: ima-studio-allinone
action: media-info
input: "/video/test.mp4"
output: "/video/test.json"
format: json
```

---

## 📝 所有动作说明

### 1. audio-convert（音频转换）

将音频文件转换为指定格式。

**参数：**
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `action` | string | 是 | `audio-convert` |
| `input` | string | 是 | 输入文件路径 |
| `output` | string | 是 | 输出文件路径 |
| `format` | string | 是 | 目标格式：`ima-adpcm`, `wav`, `mp3`, `aac`, `flac`, `ogg` |
| `bitrate` | string | 否 | 码率（如 `64k`, `128k`） |
| `sample-rate` | number | 否 | 采样率（Hz） |
| `channels` | number | 否 | 声道数（1/2） |

**示例：**
```yaml
skill: ima-studio-allinone
action: audio-convert
input: "recording.wav"
output: "recording.ima"
format: ima-adpcm
bitrate: 64k
sample-rate: 44100
channels: 1
```

### 2. video-compress（视频压缩）

压缩或转换视频文件。

**参数：**
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `action` | string | 是 | `video-compress` |
| `input` | string | 是 | 输入文件路径 |
| `output` | string | 是 | 输出文件路径 |
| `codec` | string | 是 | `h264`, `h265`, `vp9`, `av1` |
| `crf` | number | 否 | 质量参数（0-51），默认 23 |
| `preset` | string | 否 | 速度预设，默认 `medium` |
| `resolution` | string | 否 | `1920x1080`, `1280x720`, `keep` |
| `framerate` | number | 否 | 目标帧率 |
| `bitrate` | string | 否 | 视频码率（如 `2M`） |

**示例：**
```yaml
skill: ima-studio-allinone
action: video-compress
input: "original.mp4"
output: "compressed.mp4"
codec: h264
crf: 23
preset: fast
resolution: 1920x1080
```

### 3. batch-convert（批量处理）

批量转换整个文件夹。

**参数：**
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `action` | string | 是 | `batch-convert` |
| `input-dir` | string | 是 | 输入文件夹 |
| `output-dir` | string | 是 | 输出文件夹 |
| `target-format` | string | 是 | 目标格式（视频：`mp4`, `avi`；音频：`mp3`, `wav`等） |
| `concurrent` | number | 否 | 并发数，默认 2 |
| `recursive` | boolean | 否 | 是否递归子文件夹 |

**示例：**
```yaml
skill: ima-studio-allinone
action: batch-convert
input-dir: "./raw_videos"
output-dir: "./compressed"
target-format: mp4
concurrent: 4
recursive: true
```

### 4. media-info（获取媒体信息）

提取文件的元数据。

**参数：**
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `action` | string | 是 | `media-info` |
| `input` | string | 是 | 输入文件路径 |
| `output` | string | 否 | 输出报告路径（默认同源+`.json`） |
| `format` | string | 否 | `json`, `csv`, `yaml` |

**示例：**
```yaml
skill: ima-studio-allinone
action: media-info
input: "video.mp4"
output: "video_info.json"
format: json
```

### 5. audio-extract（提取音频）

从视频中提取音轨。

**参数：**
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `action` | string | 是 | `audio-extract` |
| `input` | string | 是 | 输入视频文件 |
| `output` | string | 是 | 输出音频文件 |
| `format` | string | 否 | `mp3`, `wav`, `aac`, `flac`（默认 `mp3`） |
| `bitrate` | string | 否 | 码率，默认 `128k` |

**示例：**
```yaml
skill: ima-studio-allinone
action: audio-extract
input: "movie.mp4"
output: "movie_audio.mp3"
format: mp3
bitrate: 192k
```

### 6. video-screenshot（视频截图）

截取视频某一帧。

**参数：**
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `action` | string | 是 | `video-screenshot` |
| `input` | string | 是 | 输入视频文件 |
| `output` | string | 是 | 输出图片路径（支持 png/jpg） |
| `time` | string | 否 | 时间点 `HH:MM:SS` 或秒数，默认 `00:00:05` |
| `width` | number | 否 | 目标宽度（高度按比例） |
| `height` | number | 否 | 目标高度（宽度按比例） |

**示例：**
```yaml
skill: ima-studio-allinone
action: video-screenshot
input: "movie.mp4"
output: "thumbnail.jpg"
time: "00:01:30"
width: 1920
```

---

## 🔧 依赖安装

### Windows

1. 下载 FFmpeg：https://www.gyan.dev/ffmpeg/builds/
2. 解压到 `C:\ffmpeg\`
3. 添加 `C:\ffmpeg\bin` 到系统 PATH
4. 重启 OpenClaw

### macOS

```bash
brew install ffmpeg
```

### Linux

```bash
# Ubuntu/Debian
sudo apt update && sudo apt install ffmpeg

# CentOS/RHEL/Fedora
sudo yum install ffmpeg  # 或 dnf install ffmpeg
```

---

## 🐛 故障排除

### 错误：`FFMPEG_NOT_FOUND`
**原因**：FFmpeg 未安装或不在 PATH 中。
**解决**：安装 FFmpeg，或编辑 `config.yaml` 设置 `ffmpeg-path` 为绝对路径。

### 错误：`INVALID_INPUT`
**原因**：输入文件不存在或路径错误。
**解决**：检查文件路径，确保 OpenClaw 有读取权限。

### 错误：`OUTPUT_EXISTS`
**原因**：输出文件已存在。
**解决**：删除旧文件，或使用新文件名。

### 错误：`UNSUPPORTED_CODEC`
**原因**：FFmpeg 版本不支持该编码器。
**解决**：升级 FFmpeg 到最新版。

### 性能慢
**解决**：
1. 增加 `concurrent` 并发数（不超过 CPU 核心数）
2. 使用 SSD 作为输入输出目录
3. 调整视频压缩 `preset` 为 `fast`（牺牲质量换速度）

---

## 📊 性能基准

| 任务 | CPU (i7) | 内存 | 时长 (10min 1080p 视频) |
|------|----------|------|------------------------|
| video-compress (h264, crf=23, medium) | 2核 | 512MB | ~3-5分钟 |
| audio-convert (WAV→IMA) | 1核 | 128MB | <10秒 |
| batch-convert (10 files, concurrent=4) | 4核 | 2GB | 取决于文件大小 |
| media-info | 0.5核 | 64MB | <1秒 |

---

## 🎯 使用场景建议

### 场景 1：语音录制压缩
- **动作**：`audio-convert` → `ima-adpcm`
- **参数**：`bitrate: 64k`, `sample-rate: 8000`, `channels: 1`
- **效果**：语音文件压缩为 1/4 大小，音质足够

### 场景 2：视频归档
- **动作**：`video-compress` → `h264`, `crf=20`
- **参数**：`preset: slow`, `resolution: keep`
- **效果**：体积减少 50%，质量几乎无损

### 场景 3：批量提取音频（播客转文字）
- **动作**：`batch-convert` + `audio-extract`
- **参数**：`target-format: wav`, `concurrent: 4`
- **效果**：10小时视频批量提取，耗时约30分钟

---

## 📜 许可证

MIT License - 可自由使用、修改、商业分发。

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

## 📞 支持

- OpenClaw Discord: #ima-studio-allinone
- GitHub: https://github.com/openclaw/ima-studio-allinone
- 作者：蒙境 (基于社区)

---

**Enjoy your media processing!** 🎬🎵
