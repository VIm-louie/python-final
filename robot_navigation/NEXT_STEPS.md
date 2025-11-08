#!/bin/bash
# 下一步执行指南
# 由于需要管理员权限安装包，请按以下步骤手动执行

echo "=========================================="
echo "  待办事项执行指南"
echo "=========================================="
echo ""

cat << 'EOF'
当前状态：
  ✅ 项目框架已完成
  ⏳ 需要安装Python环境
  ⏳ 需要下载数据集

下一步操作（请依次执行）：
========================================

第1步：安装Python依赖包
----------------------------------------

选项A：使用系统包管理器（推荐）

  sudo apt update
  sudo apt install -y python3-pip python3-pandas python3-numpy \
                      python3-matplotlib python3-seaborn \
                      python3-sklearn python3-jupyter python3-notebook

选项B：使用pip用户安装

  # 首先安装pip（如果还没有）
  sudo apt install -y python3-pip

  # 然后安装Python包到用户目录
  pip3 install --user pandas numpy matplotlib seaborn \
                      scikit-learn jupyter notebook jupyterlab joblib

选项C：使用虚拟环境（推荐用于开发）

  # 安装venv
  sudo apt install -y python3-venv python3-pip

  # 创建虚拟环境
  cd /home/tong/projects/work/final/robot_navigation
  python3 -m venv venv

  # 激活虚拟环境
  source venv/bin/activate

  # 安装依赖
  pip install -r requirements.txt

验证安装：
  python3 code/setup_check.py

========================================

第2步：下载数据集
----------------------------------------

选项A：使用自动下载工具

  python3 code/download_data.py

选项B：手动下载（如果Kaggle API不可用）

  1. 在浏览器中打开：
     https://www.kaggle.com/datasets/narayananpp/indoor-robot-navigation-dataset-irnd/data

  2. 登录Kaggle账号（如果没有，免费注册一个）

  3. 点击页面上的 "Download" 按钮

  4. 下载后会得到一个zip文件，解压它

  5. 将CSV文件复制到项目的data目录：
     cp <下载路径>/*.csv /home/tong/projects/work/final/robot_navigation/data/

验证下载：
  ls -lh data/*.csv

========================================

第3步：运行数据分析
----------------------------------------

  cd /home/tong/projects/work/final/robot_navigation/code
  jupyter notebook robot_navigation_analysis.ipynb

操作提示：
  1. Jupyter会在浏览器中自动打开
  2. 依次运行每个单元格（Shift + Enter）
  3. 第一次运行时注意查看数据集的列名
  4. 如果列名不匹配，根据提示调整代码
  5. 观察输出结果和图表
  6. 所有图表会自动保存到 ../figures/ 目录

预期结果：
  - 生成11张PNG格式的图表
  - 生成2个CSV结果文件
  - 生成3个模型文件（.pkl）

========================================

第4步：撰写报告
----------------------------------------

  1. 打开报告模板：
     cd /home/tong/projects/work/final/robot_navigation/report
     # 使用文本编辑器打开 report_template.md

  2. 根据Notebook运行结果填充模板：
     - 填写个人信息（姓名、学号、班级）
     - 复制粘贴关键统计数据
     - 记录模型性能指标
     - 补充分析洞察

  3. 插入图表：
     - 从 ../figures/ 目录获取生成的图表
     - 在报告中插入图片引用

  4. 转换为Word格式：

     # 安装pandoc（如果还没有）
     sudo apt install pandoc

     # 转换为Word
     pandoc report_template.md -o Python数据分析报告_姓名_学号.docx

  5. 在Word中调整格式并插入图片

========================================

第5步：最终检查与提交
----------------------------------------

提交前检查清单：

  ✓ 报告内容完整（8000+字）
  ✓ 所有图表都已插入
  ✓ 数据准确无误
  ✓ 个人信息正确
  ✓ 代码有详细注释
  ✓ 文字通顺无错别字

准备提交材料：

  1. 电子版：
     - 报告（Word或PDF格式）
     - Jupyter Notebook文件（.ipynb）
     - 压缩所有文件打包

  2. 纸质版：
     - 打印报告
     - 装订整齐

提交方式：

  1. 电子版 → 学习通平台
  2. 纸质版 → 课代表 → 学院418办公室

提交截止时间：
  ⏰ 第十周 周二（2025.11.14）23:59

========================================

常见问题处理
========================================

Q1: Jupyter Notebook无法启动？
A1: 尝试使用 jupyter lab 替代：
    jupyter lab robot_navigation_analysis.ipynb

Q2: 数据集列名不匹配？
A2: 在Notebook中先运行：
    print(df.columns.tolist())
    然后根据实际列名调整代码

Q3: 图表中文显示乱码？
A3: 确保Notebook开头有：
    plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
    plt.rcParams['axes.unicode_minus'] = False

Q4: 模型训练太慢？
A4: 减少模型复杂度：
    rf_model = RandomForestClassifier(
        n_estimators=50,  # 减少树的数量
        max_depth=10,     # 限制深度
        n_jobs=-1
    )

Q5: 内存不足？
A5: 如果数据集太大，可以：
    - 使用数据采样：df = df.sample(frac=0.5)
    - 减少模型复杂度
    - 关闭其他程序

========================================

时间规划参考
========================================

  今天 (11.02)  : 2小时  - 环境安装 + 数据下载
  11.03         : 2小时  - 运行代码，理解结果
  11.04         : 2小时  - 调试代码，生成图表
  11.05-11.06   : 6小时  - 撰写报告初稿
  11.07-11.08   : 4小时  - 修改完善报告
  11.09-11.13   : 每天1小时 - 润色和准备
  11.14         : 1小时  - 最终检查和提交

总计约：20小时

========================================

获取帮助
========================================

遇到问题时：
  1. 查看 QUICKSTART.md 中的详细说明
  2. 查看代码中的注释
  3. 搜索错误信息
  4. 咨询同学或老师

========================================

现在开始执行！
========================================

从第1步开始，选择一个安装选项：

  # 推荐：使用系统包管理器
  sudo apt update
  sudo apt install -y python3-pip python3-pandas python3-numpy \
                      python3-matplotlib python3-seaborn \
                      python3-sklearn python3-jupyter python3-notebook

然后运行验证：
  python3 code/setup_check.py

祝您顺利完成！🚀

EOF
