# IMA studio All-in-One

**一个全能的音频/视频处理技能，集成 IMA ADPCM 编解码、格式转换、媒体分析、批量处理等功能。**

---

## 概述

IMA studio All-in-One 是 OpenClaw 的媒体处理瑞士军刀。基于 IMA ADPCM（Adaptive Differential Pulse Code Modulation）技术，提供高效的音频压缩解码，以及全方位的音视频转换、分析、批处理能力。

**核心定位**：一键式媒体处理，无需复杂配置，适合日常使用和自动化流程。

---

## 功能列表

### 1. 音频处理
- ✅ IMA ADPCM 编码/解码（.ima, .adpcm 格式）
- ✅ 音频格式转换（WAV, MP3, AAC, FLAC, OGG 互转）
- ✅ 音频提取（从视频中提取音轨）
- ✅ 音频合并/分割
- ✅ 音量标准化（-16 LUFS 广播标准）
- ✅ 降噪处理（基于 RNNoise 算法）

### 2. 视频处理
- ✅ 视频格式转换（MP4, AVI, MKV, MOV, WebM）
- ✅ 视频压缩（H.264/H.265，可调码率）
- ✅ 视频截图（指定时间点或间隔）
- ✅ 视频合并/分割
- ✅ 提取音频轨道
- ✅ 调整分辨率/帧率

### 3. 批量处理
- ✅ 文件夹批量转换
- ✅ 格式自动识别
- ✅ 并发处理（多线程）
- ✅ 进度显示与日志

### 4. 媒体分析
- ✅ 获取媒体元数据（时长、码率、分辨率、编码格式）
- ✅ 检测文件完整性
- ✅ 生成媒体报告（JSON/CSV）

### 5. 自动化集成
- ✅ 支持 OpenClaw 工作流
- ✅ 可与其他技能链式调用
- ✅ 提供 RESTful API 接口（可选）

---

## 安装要求

### 依赖环境
- **OpenClaw Gateway** v2.0+
- **Node.js** v18+（运行时）
- **FFmpeg** v5.0+（核心处理引擎）
- **Python** 3.9+（部分分析脚本）

### 自动安装脚本（推荐）

```bash
# 在 OpenClaw 终端中执行
openclaw skills install ima-studio-allinone
```

如果从 GitHub 手动安装：

```bash
cd ~/.openclaw/workspace/skills
git clone https://github.com/openclaw/ima-studio-allinone.git
cd ima-studio-allinone
npm install  # 安装 Node 依赖
python -m pip install -r requirements.txt  # 安装 Python 依赖
```

---

## 快速开始

### 示例 1：音频转换（WAV → IMA ADPCM）

```yaml
skill: ima-studio-allinone
action: audio-convert
input: "/path/to/input.wav"
output: "/path/to/output.ima"
format: ima-adpcm
bitrate: 64k
```

### 示例 2：视频压缩（MP4 → H.264）

```yaml
skill: ima-studio-allinone
action: video-compress
input: "/path/to/input.mp4"
output: "/path/to/output.mp4"
codec: h264
crf: 23  # 质量参数，越小质量越高
preset: medium  # 压缩速度：fast, medium, slow
```

### 示例 3：批量处理整个文件夹

```yaml
skill: ima-studio-allinone
action: batch-convert
input-dir: "/path/to/folder"
output-dir: "/path/to/output"
target-format: mp4
concurrent: 4  # 同时处理4个文件
```

### 示例 4：提取媒体元数据

```yaml
skill: ima-studio-allinone
action: media-info
input: "/path/to/video.mp4"
output: "/path/to/info.json"
format: json
```

---

## 参数详解

### 音频转换 (audio-convert)

| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| `action` | string | 是 | 固定为 `audio-convert` | `audio-convert` |
| `input` | string | 是 | 输入文件路径 | `"/music/input.wav"` |
| `output` | string | 是 | 输出文件路径 | `"/music/output.ima"` |
| `format` | string | 是 | 目标格式：`ima-adpcm`, `wav`, `mp3`, `aac`, `flac`, `ogg` | `ima-adpcm` |
| `bitrate` | string | 否 | 码率（如 `64k`, `128k`, `192k`） | `64k` |
| `sample-rate` | number | 否 | 采样率（Hz），默认保持原样 | `44100` |
| `channels` | number | 否 | 声道数：1（单声道）, 2（立体声） | `2` |

### 视频压缩 (video-compress)

| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| `action` | string | 是 | 固定为 `video-compress` | `video-compress` |
| `input` | string | 是 | 输入文件路径 | `"/video/input.mp4"` |
| `output` | string | 是 | 输出文件路径 | `"/video/output.mp4"` |
| `codec` | string | 是 | 编码器：`h264`, `h265`, `vp9`, `av1` | `h264` |
| `crf` | number | 否 | 质量参数（0-51，越小质量越高），默认23 | `23` |
| `preset` | string | 否 | 压缩速度：`ultrafast`, `superfast`, `veryfast`, `faster`, `fast`, `medium`, `slow`, `slower`, `veryslow` | `medium` |
| `resolution` | string | 否 | 目标分辨率：`1920x1080`, `1280x720`, `640x480` 或 `keep` | `keep` |
| `framerate` | number | 否 | 目标帧率，默认保持 | `30` |

### 批量处理 (batch-convert)

| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| `action` | string | 是 | 固定为 `batch-convert` | `batch-convert` |
| `input-dir` | string | 是 | 输入文件夹路径 | `"/videos/originals"` |
| `output-dir` | string | 是 | 输出文件夹路径 | `/videos/converted` |
| `target-format` | string | 是 | 目标格式：`mp4`, `avi`, `mkv`, `mov`, `webm`（视频）或 `mp3`, `wav`, `flac`（音频） | `mp4` |
| `concurrent` | number | 否 | 并发数，默认2，最大8 | `4` |
| `recursive` | boolean | 否 | 是否递归处理子文件夹，默认false | `true` |

### 获取媒体信息 (media-info)

| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| `action` | string | 是 | 固定为 `media-info` | `media-info` |
| `input` | string | 是 | 输入文件路径 | `"/video/test.mp4"` |
| `output` | string | 否 | 输出报告路径（默认同源文件，扩展名.json） | `"/video/test.json"` |
| `format` | string | 否 | 输出格式：`json`, `csv`, `yaml` | `json` |

---

## 工作流程集成示例

### 场景：自动化视频处理管道

```
1. 监控文件夹（监听新视频文件）
   ↓ 触发
2. 使用 media-info 获取元数据
   ↓ 判断分辨率
3. 如果 > 1080p，使用 video-compress 压缩到 1080p
   ↓
4. 使用 video-screenshot 提取封面图
   ↓
5. 使用 audio-extract 提取音频为 MP3
   ↓
6. 移动原文件到归档，输出文件到发布目录
```

YAML 配置示例：

```yaml
# step1: 分析
- skill: ima-studio-allinone
  action: media-info
  input: "{{trigger.file}}"
  output: "{{temp.dir}}/info.json"

# step2: 条件压缩
- skill: ima-studio-allinone
  action: video-compress
  input: "{{trigger.file}}"
  output: "{{output.dir}}/{{filename}}.mp4"
  codec: h264
  crf: 23
  condition: "{{info.width}} > 1920"

# step3: 提取音频
- skill: ima-studio-allinone
  action: audio-extract
  input: "{{trigger.file}}"
  output: "{{output.dir}}/{{filename}}.mp3"
  format: mp3
  bitrate: 192k
```

---

## 配置文件

技能支持配置文件 `~/.openclaw/skills/ima-studio-allinone/config.yaml`：

```yaml
# FFmpeg 路径（如果未加入系统PATH）
ffmpeg-path: "/usr/local/bin/ffmpeg"
ffprobe-path: "/usr/local/bin/ffprobe"

# 默认设置
defaults:
  video:
    codec: h264
    crf: 23
    preset: medium
  audio:
    codec: aac
    bitrate: 128k
  concurrent: 2

# 日志级别
log-level: info  # debug, info, warn, error

# 临时文件目录
temp-dir: "/tmp/ima-studio"
```

---

## 错误处理与调试

### 常见错误

| 错误码 | 说明 | 解决方案 |
|--------|------|----------|
| `FFMPEG_NOT_FOUND` | 未找到 FFmpeg | 安装 FFmpeg 并配置 PATH，或在 config.yaml 指定路径 |
| `INVALID_INPUT` | 输入文件不存在或格式不支持 | 检查文件路径，确认文件完整 |
| `OUTPUT_EXISTS` | 输出文件已存在 | 删除旧文件或指定新路径 |
| `UNSUPPORTED_CODEC` | 编码器不支持 | 更换 codec 参数（如 h264 → h265） |
| `INSUFFICIENT_DISK` | 磁盘空间不足 | 清理临时文件或更换输出目录 |

### 调试模式

在调用技能时开启调试：

```yaml
skill: ima-studio-allinone
debug: true
verbose: true
```

日志输出到 `~/.openclaw/logs/ima-studio-allinone.log`。

---

## 性能优化建议

1. **并发数设置**：根据 CPU 核心数调整，通常 `物理核心数 - 1` 为佳
2. **使用 SSD**：输入输出目录放在 SSD 上，大幅提升速度
3. **预设选择**：
   - 需要速度快：`ultrafast` → `crf` 提高 2-3 点补偿质量
   - 需要高质量：`slow` 或 `slower`
4. **临时文件清理**：定期清理 `temp-dir`，避免磁盘占满

---

## 更新日志

### v1.0.0 (2025-12)
- 🎉 首次发布
- 支持音频 IMA ADPCM 编解码
- 支持视频格式转换与压缩
- 支持批量处理与并发
- 支持媒体元数据分析

---

## 技术细节

### IMA ADPCM 简介

IMA ADPCM 是一种有损音频压缩算法，特点：
- **压缩比**：4:1（16-bit PCM → 4-bit IMA）
- **音质**：适合语音，音乐尚可
- **延迟**：极低（实时处理友好）
- **应用**：游戏音频、嵌入式设备、语音存储

### 依赖工具

- **FFmpeg**：核心媒体处理引擎
- **ffprobe**：媒体信息探测
- **sox**：音频处理辅助（可选）
- **Python 3**：元数据分析脚本

---

## 许可证

MIT License

---

## 支持与反馈

- **问题反馈**：OpenClaw Discord #ima-studio
- **功能请求**：GitHub Issues
- **商业支持**：contact@openclaw.ai

---

**Skill ID**: `ima-studio-allinone`  
**Version**: 1.0.0  
**Author**: OpenClaw Community  
**Maintainer**: 蒙境 (基于社区版本)  
**Created**: 2026-03-20  
**Last Updated**: 2026-03-20  
**Tags**: audio, video, conversion, ima-adpcm, batch-processing, media  
**Category**: multimedia  
**Compatibility**: OpenClaw v2.0+
