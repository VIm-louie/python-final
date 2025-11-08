#!/bin/bash
# 手动执行安装指南
# 请在终端中依次执行以下命令

echo "=========================================="
echo "Python环境安装指南"
echo "=========================================="
echo ""

cat << 'EOF'
由于系统限制，需要您手动执行以下命令来完成安装。

第1步：选择安装方法
========================================

推荐方法A：使用系统包管理器（最简单）
--------------------
sudo apt update
sudo apt install -y python3-pandas python3-numpy python3-matplotlib \
                    python3-seaborn python3-sklearn python3-jupyter \
                    python3-notebook python3-joblib

推荐方法B：使用虚拟环境（最干净）
--------------------
# 安装venv
sudo apt install -y python3-venv python3-pip

# 创建虚拟环境
cd /home/tong/projects/work/final/robot_navigation
python3 -m venv venv

# 激活虚拟环境
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

方法C：强制使用pip（不推荐）
--------------------
pip3 install --user --break-system-packages pandas numpy matplotlib \
             seaborn scikit-learn jupyter notebook joblib

========================================

第2步：验证安装
========================================

执行完上述命令后，运行验证：

python3 code/setup_check.py

应该看到所有包都显示 ✅

========================================

第3步：下载数据集
========================================

执行以下命令之一：

方法A：自动下载
--------------------
python3 code/download_data.py

方法B：手动下载
--------------------
1. 在浏览器打开：
   https://www.kaggle.com/datasets/narayananpp/indoor-robot-navigation-dataset-irnd/data

2. 登录Kaggle（免费注册）

3. 点击 "Download" 按钮

4. 解压下载的zip文件

5. 将CSV文件复制到data目录：
   cp <解压路径>/*.csv /home/tong/projects/work/final/robot_navigation/data/

6. 验证：
   ls -lh data/*.csv

========================================

第4步：运行分析
========================================

# 如果使用虚拟环境，先激活
source venv/bin/activate  # 如果使用了虚拟环境

# 启动Jupyter
cd code
jupyter notebook robot_navigation_analysis.ipynb

# 或者使用 jupyter lab
jupyter lab robot_navigation_analysis.ipynb

========================================

快速命令复制
========================================

一键安装（方法A - 系统包）：
--------------------
sudo apt update && sudo apt install -y python3-pandas python3-numpy python3-matplotlib python3-seaborn python3-sklearn python3-jupyter python3-notebook python3-joblib && python3 code/setup_check.py

一键安装（方法B - 虚拟环境）：
--------------------
sudo apt install -y python3-venv python3-pip && cd /home/tong/projects/work/final/robot_navigation && python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt && python3 code/setup_check.py

========================================

下一步做什么？
========================================

安装完成后：

1. 运行验证：
   python3 code/setup_check.py

2. 下载数据：
   python3 code/download_data.py

3. 启动分析：
   cd code
   jupyter notebook robot_navigation_analysis.ipynb

4. 按照Notebook中的提示依次运行每个单元格

5. 生成的图表会自动保存到 ../figures/ 目录

6. 根据结果填写报告模板：
   report/report_template.md

========================================

需要帮助？
========================================

查看详细文档：
  - START.md - 快速入门
  - QUICKSTART.md - 详细步骤
  - NEXT_STEPS.md - 下一步指南

EOF
