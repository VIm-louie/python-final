#!/bin/bash
# 快速执行命令清单
# 复制粘贴即可执行

# ============================================
# 第1步：安装Python环境（选择其中一个方法）
# ============================================

# 方法A：系统包管理器（最简单，推荐）
sudo apt update && sudo apt install -y python3-pip python3-pandas python3-numpy python3-matplotlib python3-seaborn python3-sklearn python3-jupyter python3-notebook

# 方法B：pip用户安装
sudo apt install -y python3-pip
pip3 install --user pandas numpy matplotlib seaborn scikit-learn jupyter notebook jupyterlab joblib

# 方法C：虚拟环境（最干净）
sudo apt install -y python3-venv python3-pip
cd /home/tong/projects/work/final/robot_navigation
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 验证安装
python3 code/setup_check.py

# ============================================
# 第2步：下载数据集（选择其中一个方法）
# ============================================

# 方法A：自动下载工具
python3 code/download_data.py

# 方法B：手动下载
# 1. 浏览器打开: https://www.kaggle.com/datasets/narayananpp/indoor-robot-navigation-dataset-irnd/data
# 2. 点击 Download
# 3. 解压后复制CSV文件到 data/ 目录

# 验证数据
ls -lh data/*.csv

# ============================================
# 第3步：运行分析
# ============================================

cd /home/tong/projects/work/final/robot_navigation/code
jupyter notebook robot_navigation_analysis.ipynb

# 或者使用 jupyter lab
# jupyter lab robot_navigation_analysis.ipynb

# ============================================
# 第4步：撰写报告
# ============================================

# 打开报告模板进行编辑
cd /home/tong/projects/work/final/robot_navigation/report
# 使用文本编辑器编辑 report_template.md

# 转换为Word（在完成编辑后）
sudo apt install pandoc
pandoc report_template.md -o Python数据分析报告_姓名_学号.docx

# ============================================
# 第5步：最终检查
# ============================================

# 检查生成的文件
ls -lh figures/*.png          # 应该有11张图
ls -lh report/*.csv           # 应该有2个CSV文件
ls -lh code/*.pkl             # 应该有3个模型文件

# 验证报告完整性
wc -w report/report_template.md  # 应该大于8000字

# ============================================
# 快捷命令参考
# ============================================

# 重新运行环境检查
python3 code/setup_check.py

# 查看项目状态
cat NEXT_STEPS.md

# 查看待办清单
cat << 'CHECKLIST'
待办清单：
[ ] 安装Python环境
[ ] 下载数据集
[ ] 验证环境
[ ] 运行Jupyter Notebook
[ ] 生成所有图表
[ ] 记录关键数据
[ ] 填写报告模板
[ ] 插入图表
[ ] 转换为Word
[ ] 最终审核
[ ] 准备提交
CHECKLIST
