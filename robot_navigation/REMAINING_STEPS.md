#!/bin/bash
# 后续步骤执行指南

echo "══════════════════════════════════════════════════════════════════"
echo "  剩余待办事项 - 执行清单"
echo "══════════════════════════════════════════════════════════════════"
echo ""

cat << 'EOF'
当前状态检查：Python包尚未成功导入

请先完成Python包安装，然后继续以下步骤：

══════════════════════════════════════════════════════════════════
步骤1：确认Python包安装 ⭐ （必须完成）
══════════════════════════════════════════════════════════════════

快速安装命令（选择一个）：

方法A（推荐）：
sudo apt update && sudo apt install -y python3-pandas python3-numpy \
  python3-matplotlib python3-seaborn python3-sklearn python3-jupyter \
  python3-notebook

方法B（虚拟环境）：
sudo apt install -y python3-venv python3-pip
cd /home/tong/projects/work/final/robot_navigation
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

验证安装：
python3 -c "import pandas, numpy, matplotlib; print('✅ 安装成功')"

或运行：
python3 code/setup_check.py

══════════════════════════════════════════════════════════════════
步骤2：下载数据集 ⭐ （必须完成）
══════════════════════════════════════════════════════════════════

方法A：自动下载（如果有Kaggle API）
python3 code/download_data.py

方法B：手动下载
1. 浏览器打开：
   https://www.kaggle.com/datasets/narayananpp/indoor-robot-navigation-dataset-irnd/data

2. 登录Kaggle账号（免费注册）

3. 点击 "Download" 按钮下载zip文件

4. 解压zip文件

5. 将CSV文件复制到项目data目录：

   # 假设下载到 ~/Downloads/indoor-robot-navigation-dataset-irnd.zip
   cd ~/Downloads
   unzip indoor-robot-navigation-dataset-irnd.zip

   # 复制CSV文件到项目data目录
   cp *.csv /home/tong/projects/work/final/robot_navigation/data/

   # 或者如果在子目录中
   cp */*.csv /home/tong/projects/work/final/robot_navigation/data/

6. 验证数据：
   ls -lh /home/tong/projects/work/final/robot_navigation/data/*.csv

应该看到CSV文件列表

══════════════════════════════════════════════════════════════════
步骤3：启动Jupyter Notebook分析
══════════════════════════════════════════════════════════════════

cd /home/tong/projects/work/final/robot_navigation/code

# 如果使用虚拟环境，先激活
# source ../venv/bin/activate

# 启动Jupyter Notebook
jupyter notebook robot_navigation_analysis.ipynb

# 或使用jupyter lab
# jupyter lab robot_navigation_analysis.ipynb

Jupyter将在浏览器中自动打开

══════════════════════════════════════════════════════════════════
步骤4：在Jupyter Notebook中运行分析
══════════════════════════════════════════════════════════════════

重要操作顺序：

1. 运行前3-4个单元格（导入库 + 加载数据）

2. 查看数据集结构：
   - 观察数据的shape
   - 查看列名：df.columns.tolist()
   - 查看前几行：df.head()

3. 检查目标变量列名：
   - 可能是 'surface', 'floor_type', 'label' 等
   - 如果不是'surface'，需要调整代码

4. 根据实际列名调整代码（在相关单元格中）：
   # 示例：如果目标列是 'floor_type' 而不是 'surface'
   # 修改所有 df['surface'] 为 df['floor_type']

5. 按顺序运行所有单元格（Shift + Enter）
   - 数据清洗
   - 探索性分析
   - 模型训练
   - 模型评估

6. 观察输出和图表
   - 所有图表会自动保存到 ../figures/
   - 结果文件保存到 ../report/

预期运行时间：30分钟 - 2小时（取决于数据量和电脑性能）

══════════════════════════════════════════════════════════════════
步骤5：记录关键结果
══════════════════════════════════════════════════════════════════

在运行过程中记录以下数据（用于填写报告）：

数据集信息：
□ 总样本数：_______
□ 特征数量：_______
□ 目标类别：_______
□ 类别分布：_______

模型性能（逻辑回归）：
□ 准确率：_______%
□ 精确率：_______%
□ 召回率：_______%
□ F1分数：_______

模型性能（随机森林）：
□ 准确率：_______%
□ 精确率：_______%
□ 召回率：_______%
□ F1分数：_______

模型性能（SVM）：
□ 准确率：_______%
□ 精确率：_______%
□ 召回率：_______%
□ F1分数：_______

最佳模型：_______
AUC值：_______

Top 5 重要特征：
1. ____________
2. ____________
3. ____________
4. ____________
5. ____________

══════════════════════════════════════════════════════════════════
步骤6：撰写报告
══════════════════════════════════════════════════════════════════

cd /home/tong/projects/work/final/robot_navigation/report

# 使用文本编辑器打开模板
nano report_template.md
# 或使用其他编辑器：vim, gedit, code等

填写内容：
1. 个人信息（姓名、学号、班级）
2. 摘要（100-200字，概括研究内容和结果）
3. 数据描述（使用记录的数据）
4. 数据预处理（描述清洗过程）
5. 分析结果（插入发现和洞察）
6. 模型性能（填入记录的指标）
7. 结论和建议

══════════════════════════════════════════════════════════════════
步骤7：插入图表
══════════════════════════════════════════════════════════════════

报告中需要插入的图表（从 ../figures/ 目录）：

□ 01_missing_values_heatmap.png - 缺失值热图
□ 02_outlier_detection.png - 异常值检测
□ 03_correlation_heatmap.png - 相关性热图
□ 04_surface_comparison_boxplot.png - 表面类型对比
□ 05_surface_distribution_hist.png - 分布直方图
□ 06_direction_surface_analysis.png - 方向分析
□ 07_feature_importance_preliminary.png - 初步特征重要性
□ 08_model_comparison.png - 模型对比
□ 09_confusion_matrices.png - 混淆矩阵
□ 10_roc_curves.png - ROC曲线
□ 11_final_feature_importance.png - 最终特征重要性

在Markdown中插入图片：
![图片说明](../figures/文件名.png)

或转换为Word后手动插入

══════════════════════════════════════════════════════════════════
步骤8：转换为Word格式
══════════════════════════════════════════════════════════════════

# 安装pandoc（如果还没有）
sudo apt install pandoc

# 转换为Word
cd /home/tong/projects/work/final/robot_navigation/report
pandoc report_template.md -o Python数据分析报告_姓名_学号.docx

# 在Word中打开并：
# - 调整格式
# - 插入图表（如果Markdown中没有正确显示）
# - 调整页眉页脚
# - 生成目录
# - 最终审核

══════════════════════════════════════════════════════════════════
步骤9：最终检查
══════════════════════════════════════════════════════════════════

提交前检查清单：

文档内容：
□ 个人信息填写正确
□ 摘要完整（包含关键词）
□ 所有章节都已填写
□ 数据和结果准确
□ 图表都已插入且清晰
□ 参考文献格式正确
□ 字数达到要求（8000+字）

代码文件：
□ Notebook运行无错误
□ 代码有详细注释
□ 输出结果完整

文件准备：
□ Word报告文档
□ Jupyter Notebook文件
□ 生成的图表文件
□ 压缩包（如果需要）

══════════════════════════════════════════════════════════════════
步骤10：提交
══════════════════════════════════════════════════════════════════

电子版提交：
1. 登录学习通平台
2. 找到课程作业提交入口
3. 上传以下文件：
   - Word报告文档
   - Jupyter Notebook文件（.ipynb）
   - 可选：压缩包含所有文件

纸质版提交：
1. 打印报告（双面打印节省纸张）
2. 装订（左侧装订）
3. 交给课代表
4. 课代表统一送到学院418办公室

提交截止时间：
⏰ 2025年11月14日（第十周周二）23:59

══════════════════════════════════════════════════════════════════

快速命令参考：
══════════════════════════════════════════════════════════════════

# 完整流程（按顺序执行）
cd /home/tong/projects/work/final/robot_navigation

# 1. 验证环境
python3 code/setup_check.py

# 2. 下载数据
python3 code/download_data.py

# 3. 启动分析
cd code && jupyter notebook robot_navigation_analysis.ipynb

# 4. 转换报告
cd ../report
pandoc report_template.md -o Python数据分析报告_姓名_学号.docx

══════════════════════════════════════════════════════════════════

现在开始执行步骤1：确认Python包安装！

══════════════════════════════════════════════════════════════════
EOF
