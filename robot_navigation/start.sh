#!/bin/bash
# 快速开始脚本 - 一键启动项目环境

echo "=========================================="
echo "  室内机器人导航数据分析项目"
echo "  快速开始"
echo "=========================================="
echo ""

# 进入项目目录
cd "$(dirname "$0")"

# 检查是否是第一次运行
if [ ! -f ".setup_done" ]; then
    echo "检测到首次运行，开始环境设置..."
    echo ""

    # 运行环境检查
    echo "→ 步骤 1/3: 检查环境..."
    python3 code/setup_check.py

    echo ""
    echo "→ 步骤 2/3: 安装依赖"
    echo ""
    echo "请选择安装方式:"
    echo "  1) 运行自动安装脚本（推荐）"
    echo "  2) 手动安装"
    echo "  3) 跳过（已安装）"
    read -p "请选择 [1-3]: " install_choice

    case $install_choice in
        1)
            bash install.sh
            ;;
        2)
            echo ""
            echo "请运行以下命令手动安装:"
            echo "  sudo apt install python3-pip python3-pandas python3-numpy python3-matplotlib python3-seaborn python3-sklearn python3-jupyter"
            echo ""
            read -p "按回车键继续..."
            ;;
        3)
            echo "跳过安装"
            ;;
    esac

    echo ""
    echo "→ 步骤 3/3: 下载数据集"
    echo ""
    echo "请选择下载方式:"
    echo "  1) 使用自动下载工具"
    echo "  2) 查看手动下载指南"
    echo "  3) 跳过（已下载）"
    read -p "请选择 [1-3]: " download_choice

    case $download_choice in
        1)
            python3 code/download_data.py
            ;;
        2)
            echo ""
            echo "手动下载步骤:"
            echo "  1. 访问: https://www.kaggle.com/datasets/narayananpp/indoor-robot-navigation-dataset-irnd/data"
            echo "  2. 点击 Download 按钮"
            echo "  3. 解压后将CSV文件放到 robot_navigation/data/ 目录"
            echo ""
            read -p "按回车键继续..."
            ;;
        3)
            echo "跳过下载"
            ;;
    esac

    # 标记为已设置
    touch .setup_done
    echo ""
    echo "✅ 环境设置完成！"
    echo ""
fi

# 最终验证
echo "=========================================="
echo "  环境验证"
echo "=========================================="
python3 code/setup_check.py

echo ""
echo "=========================================="
echo "  启动选项"
echo "=========================================="
echo ""
echo "请选择要执行的操作:"
echo "  1) 启动 Jupyter Notebook 进行数据分析"
echo "  2) 查看项目文档"
echo "  3) 重新运行环境检查"
echo "  4) 重新运行数据下载"
echo "  5) 退出"
echo ""
read -p "请选择 [1-5]: " action

case $action in
    1)
        echo ""
        echo "正在启动 Jupyter Notebook..."
        cd code
        jupyter notebook robot_navigation_analysis.ipynb
        ;;
    2)
        echo ""
        echo "=========================================="
        echo "  项目文档"
        echo "=========================================="
        echo ""
        echo "📖 主要文档："
        echo "  - QUICKSTART.md      : 快速开始指南（推荐阅读）"
        echo "  - PROJECT_STATUS.md  : 项目进度和状态"
        echo "  - README.md          : 项目总体说明"
        echo ""
        echo "📊 分析代码："
        echo "  - code/robot_navigation_analysis.ipynb"
        echo ""
        echo "📝 报告模板："
        echo "  - report/report_template.md"
        echo ""
        read -p "按回车键继续..."
        ;;
    3)
        echo ""
        python3 code/setup_check.py
        echo ""
        read -p "按回车键继续..."
        ;;
    4)
        echo ""
        python3 code/download_data.py
        echo ""
        read -p "按回车键继续..."
        ;;
    5)
        echo ""
        echo "再见！"
        exit 0
        ;;
    *)
        echo ""
        echo "无效选择"
        ;;
esac

echo ""
echo "=========================================="
echo "要重新运行此脚本，请执行:"
echo "  bash start.sh"
echo ""
echo "或删除 .setup_done 文件重新进行初始设置:"
echo "  rm .setup_done && bash start.sh"
echo "=========================================="
