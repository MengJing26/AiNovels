#!/bin/bash

# IMA studio All-in-One - 环境检查与安装脚本
# 用法: bash install.sh

set -e

echo "=========================================="
echo " IMA studio All-in-One 安装脚本"
echo "=========================================="

# 检查 Node.js
echo "检查 Node.js..."
if ! command -v node &> /dev/null; then
    echo "❌ Node.js 未找到，请先安装 Node.js v18+"
    echo "   下载: https://nodejs.org/"
    exit 1
fi
NODE_VERSION=$(node --version)
echo "✅ Node.js 版本: $NODE_VERSION"

# 检查 FFmpeg
echo "检查 FFmpeg..."
if ! command -v ffmpeg &> /dev/null; then
    echo "❌ FFmpeg 未找到！"
    echo ""
    echo "请根据系统安装 FFmpeg："
    echo ""
    echo "  macOS:"
    echo "    brew install ffmpeg"
    echo ""
    echo "  Ubuntu/Debian:"
    echo "    sudo apt update && sudo apt install ffmpeg"
    echo ""
    echo "  CentOS/RHEL/Fedora:"
    echo "    sudo yum install ffmpeg"
    echo ""
    echo "  Windows:"
    echo "    下载: https://www.gyan.dev/ffmpeg/builds/"
    echo "    解压并添加 ffmpeg/bin 到系统 PATH"
    echo ""
    exit 1
fi
FFMPEG_VERSION=$(ffmpeg -version | head -n1)
echo "✅ FFmpeg 已安装: $FFMPEG_VERSION"

# 检查 Python (可选)
echo "检查 Python (可选)..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo "✅ Python 已安装: $PYTHON_VERSION"
else
    echo "⚠️  Python 未安装，媒体分析功能不可用"
    echo "   建议安装 Python 3.9+"
fi

# 复制配置文件
if [ ! -f "config.yaml" ]; then
    echo "复制配置文件..."
    cp config.example.yaml config.yaml
    echo "✅ config.yaml 已创建，如需自定义请编辑"
fi

# 安装 Node.js 依赖
echo "安装 Node.js 依赖..."
npm install
echo "✅ Node.js 依赖安装完成"

# 安装 Python 依赖 (如果 Python 可用)
if command -v python3 &> /dev/null; then
    echo "安装 Python 依赖..."
    python3 -m pip install --upgrade pip
    python3 -m pip install -r requirements.txt
    echo "✅ Python 依赖安装完成"
fi

# 创建临时目录
echo "创建临时目录..."
mkdir -p temp
echo "✅ temp/ 目录已创建"

echo ""
echo "=========================================="
echo " 安装完成！"
echo "=========================================="
echo ""
echo "下一步："
echo "1. 如有需要，编辑 config.yaml 配置 FFmpeg 路径等"
echo "2. 重启 OpenClaw Gateway: openclaw gateway restart"
echo "3. 开始使用技能: 参考 README.md"
echo ""
echo "测试命令（可选）："
echo "  node scripts/index.js '{\"action\":\"media-info\",\"input\":\"test.mp4\"}'"
echo ""
