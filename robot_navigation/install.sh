#!/bin/bash
# 一键安装脚本 - 室内机器人导航数据分析项目
# 使用方法: bash install.sh

set -e  # 遇到错误立即退出

echo "=========================================="
echo "室内机器人导航数据分析 - 环境安装脚本"
echo "=========================================="
echo ""

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 检测操作系统
OS_TYPE="unknown"
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS_TYPE="linux"
    echo "✓ 检测到Linux系统"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS_TYPE="mac"
    echo "✓ 检测到macOS系统"
else
    echo "⚠ 未知操作系统: $OSTYPE"
fi

echo ""
echo "=========================================="
echo "步骤 1/4: 更新系统包管理器"
echo "=========================================="

if [[ "$OS_TYPE" == "linux" ]]; then
    echo "正在更新apt..."
    sudo apt update
    echo -e "${GREEN}✓ apt更新完成${NC}"
elif [[ "$OS_TYPE" == "mac" ]]; then
    if ! command -v brew &> /dev/null; then
        echo -e "${YELLOW}Homebrew未安装，正在安装...${NC}"
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi
    echo "正在更新brew..."
    brew update
    echo -e "${GREEN}✓ brew更新完成${NC}"
fi

echo ""
echo "=========================================="
echo "步骤 2/4: 安装Python和pip"
echo "=========================================="

# 检查Python版本
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
    echo "✓ 已安装Python: $PYTHON_VERSION"
else
    echo -e "${YELLOW}Python3未安装，正在安装...${NC}"
    if [[ "$OS_TYPE" == "linux" ]]; then
        sudo apt install -y python3
    elif [[ "$OS_TYPE" == "mac" ]]; then
        brew install python3
    fi
fi

# 检查pip
if command -v pip3 &> /dev/null; then
    echo "✓ 已安装pip3"
else
    echo -e "${YELLOW}pip3未安装，正在安装...${NC}"
    if [[ "$OS_TYPE" == "linux" ]]; then
        sudo apt install -y python3-pip
    elif [[ "$OS_TYPE" == "mac" ]]; then
        brew install python3
    fi
fi

echo ""
echo "=========================================="
echo "步骤 3/4: 安装Python科学计算包"
echo "=========================================="

echo "您希望使用哪种安装方式？"
echo "  1) 使用pip安装（推荐，最新版本）"
echo "  2) 使用系统包管理器（Ubuntu/Debian系统）"
echo "  3) 跳过安装（手动安装）"
read -p "请选择 [1-3]: " INSTALL_METHOD

case $INSTALL_METHOD in
    1)
        echo ""
        echo "使用pip安装Python包..."
        pip3 install --user pandas numpy matplotlib seaborn scikit-learn jupyter notebook jupyterlab joblib
        echo -e "${GREEN}✓ Python包安装完成${NC}"
        ;;
    2)
        if [[ "$OS_TYPE" == "linux" ]]; then
            echo ""
            echo "使用apt安装Python包..."
            sudo apt install -y python3-pandas python3-numpy python3-matplotlib \
                                python3-seaborn python3-sklearn python3-jupyter \
                                python3-notebook
            echo -e "${GREEN}✓ Python包安装完成${NC}"
        else
            echo -e "${RED}此选项仅适用于Ubuntu/Debian系统${NC}"
            echo "使用pip安装..."
            pip3 install --user pandas numpy matplotlib seaborn scikit-learn jupyter notebook jupyterlab joblib
        fi
        ;;
    3)
        echo -e "${YELLOW}跳过安装，请手动安装依赖包${NC}"
        ;;
    *)
        echo -e "${RED}无效选择，使用pip安装...${NC}"
        pip3 install --user pandas numpy matplotlib seaborn scikit-learn jupyter notebook jupyterlab joblib
        ;;
esac

echo ""
echo "=========================================="
echo "步骤 4/4: 验证安装"
echo "=========================================="

echo "正在验证Python包安装..."
python3 code/setup_check.py

echo ""
echo "=========================================="
echo "安装完成！"
echo "=========================================="
echo ""
echo -e "${GREEN}下一步操作：${NC}"
echo "  1. 下载数据集："
echo "     访问: https://www.kaggle.com/datasets/narayananpp/indoor-robot-navigation-dataset-irnd/data"
echo "     下载后解压到 robot_navigation/data/ 目录"
echo ""
echo "  2. 启动Jupyter Notebook："
echo "     cd code"
echo "     jupyter notebook robot_navigation_analysis.ipynb"
echo ""
echo "  3. 查看详细指南："
echo "     cat QUICKSTART.md"
echo ""
echo "=========================================="
