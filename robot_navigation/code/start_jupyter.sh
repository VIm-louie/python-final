#!/bin/bash
# Jupyter Notebook 启动脚本

echo "=========================================="
echo "  启动 Jupyter Notebook"
echo "=========================================="
echo ""

# 进入项目目录
cd /home/tong/projects/work/final/robot_navigation/code

# 激活虚拟环境
source ../.venv/bin/activate

# 检查必要的包
echo "检查依赖包..."
python -c "import pandas, numpy, matplotlib, seaborn, sklearn; print('✅ 所有包已安装')" || {
    echo "❌ 缺少必要的包,正在安装..."
    pip install pandas numpy matplotlib seaborn scikit-learn joblib -q
}

echo ""
echo "启动 Jupyter Notebook..."
echo "浏览器会自动打开 http://localhost:8888"
echo ""
echo "📝 使用提示:"
echo "  1. 按顺序运行每个单元格 (Shift + Enter)"
echo "  2. Cell 23会移除数据泄漏特征"
echo "  3. 逻辑回归准确率应该是 85.65%"
echo "  4. 随机森林准确率应该是 99.92%"
echo ""
echo "按 Ctrl+C 停止 Jupyter"
echo "=========================================="
echo ""

# 启动Jupyter
jupyter notebook robot_navigation_analysis.ipynb
