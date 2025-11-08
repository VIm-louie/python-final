# 项目启动指南

## 📋 项目概览

本项目是一个完整的**室内机器人导航数据分析**项目，用于完成Python数据分析课程报告。

**选题**：室内机器人导航数据分析（选题4）
**数据集**：Indoor Robot Navigation Dataset (IRND)
**技术栈**：Python, pandas, scikit-learn, matplotlib, seaborn

---

## ⚠️ 当前状态

✅ **已完成**：
- 项目目录结构创建完成
- 完整的Jupyter Notebook分析代码已准备好
- 报告模板已创建
- 环境检查脚本已就绪

❌ **待完成**：
1. **安装Python依赖包**（必需）
2. **下载数据集**（必需）
3. **运行分析代码**
4. **生成图表和结果**
5. **撰写完整报告**

---

## 🚀 快速开始

### 步骤1：安装Python依赖包

由于系统中未安装pip，您需要先安装pip和必要的Python包。

#### 方法1：在WSL/Ubuntu系统中安装

```bash
# 更新包管理器
sudo apt update

# 安装pip
sudo apt install python3-pip -y

# 安装依赖包
cd /home/tong/projects/work/final/robot_navigation
pip3 install -r requirements.txt
```

#### 方法2：使用conda（如果已安装Anaconda）

```bash
# 创建新环境
conda create -n robot_nav python=3.10 -y
conda activate robot_nav

# 安装依赖包
conda install pandas numpy matplotlib seaborn scikit-learn jupyter jupyterlab -y
pip install joblib
```

#### 方法3：使用系统自带的Python包管理器

```bash
sudo apt install python3-pandas python3-numpy python3-matplotlib \
                 python3-seaborn python3-sklearn python3-jupyter \
                 python3-notebook -y
```

### 步骤2：下载数据集

#### 选项A：手动下载（推荐）

1. **访问Kaggle数据集页面**：
   https://www.kaggle.com/datasets/narayananpp/indoor-robot-navigation-dataset-irnd/data

   或者搜索："Indoor Robot Navigation Dataset IRND"

2. **下载数据集**：
   - 如果没有Kaggle账户，先注册一个（免费）
   - 点击页面上的 "Download" 按钮
   - 下载得到一个zip文件

3. **解压并放置数据文件**：
   ```bash
   # 假设下载到了Windows的下载文件夹
   # 在WSL中访问路径类似于：/mnt/c/Users/你的用户名/Downloads/

   cd /home/tong/projects/work/final/robot_navigation/data

   # 从Windows下载目录复制（替换为实际路径）
   cp /mnt/c/Users/你的用户名/Downloads/indoor-robot-navigation-dataset.zip .

   # 解压
   unzip indoor-robot-navigation-dataset.zip
   ```

#### 选项B：使用Kaggle API

```bash
# 安装Kaggle CLI
pip3 install kaggle

# 配置API Token
# 1. 访问 https://www.kaggle.com/account
# 2. 点击 "Create New API Token" 下载 kaggle.json
# 3. 将kaggle.json放到正确位置

mkdir -p ~/.kaggle
cp /mnt/c/Users/你的用户名/Downloads/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json

# 下载数据集
cd /home/tong/projects/work/final/robot_navigation/data
kaggle datasets download -d mrisdal/indoor-robot-navigation-dataset
unzip indoor-robot-navigation-dataset.zip
```

### 步骤3：验证环境准备

```bash
cd /home/tong/projects/work/final/robot_navigation
python3 code/setup_check.py
```

如果显示"✅ 环境准备完成！"，说明可以开始分析了。

### 步骤4：运行分析

```bash
cd /home/tong/projects/work/final/robot_navigation/code
jupyter notebook robot_navigation_analysis.ipynb
```

浏览器会自动打开Jupyter Notebook界面。

**运行步骤**：
1. 依次执行每个单元格（Shift + Enter）
2. 注意查看输出和可视化图表
3. 根据实际数据集调整代码（主要是列名）
4. 所有图表会自动保存到 `../figures/` 目录

### 步骤5：撰写报告

1. 打开报告模板：
   ```bash
   cd /home/tong/projects/work/final/robot_navigation/report
   # 使用文本编辑器或Word打开 report_template.md
   ```

2. 根据分析结果填充模板：
   - 复制Notebook中的统计数据
   - 插入生成的图表
   - 补充分析洞察和建议

3. 转换为Word文档（如果需要）：
   ```bash
   # 使用pandoc转换（需要先安装）
   sudo apt install pandoc
   pandoc report_template.md -o 课程报告_姓名_学号.docx
   ```

---

## 📁 项目结构

```
robot_navigation/
├── README.md                    # 项目说明
├── QUICKSTART.md               # 本文件 - 快速开始指南
├── requirements.txt            # Python依赖列表
├── data/                       # 数据文件目录
│   └── [下载的CSV文件]
├── code/                       # 代码目录
│   ├── setup_check.py         # 环境检查脚本
│   └── robot_navigation_analysis.ipynb  # 主分析Notebook
├── figures/                    # 生成的图表
│   └── [自动生成的PNG图片]
└── report/                     # 报告文档
    ├── report_template.md     # 报告模板
    ├── model_comparison.csv   # 模型对比结果
    └── feature_importance.csv # 特征重要性

```

---

## 📊 预期输出

运行完整个Notebook后，您将获得：

### 图表（保存在figures/）
1. 缺失值分布热图
2. 异常值检测箱线图
3. 特征相关性热图
4. 不同表面类型传感器参数箱线图对比
5. 不同表面类型传感器参数分布直方图
6. 运动方向与表面类型关联分析
7. 特征重要性初步分析
8. 三种模型性能对比
9. 混淆矩阵
10. ROC曲线
11. 最终模型特征重要性

### 数据文件（保存在report/）
- model_comparison.csv - 模型性能对比
- feature_importance.csv - 特征重要性排名

### 模型文件（保存在code/）
- best_model.pkl - 最佳模型
- scaler.pkl - 数据标准化器
- label_encoder.pkl - 标签编码器

---

## ⏱️ 时间安排建议

| 任务 | 预计时间 | 优先级 |
|-----|---------|--------|
| 安装环境 | 30分钟 | 高 |
| 下载数据集 | 15分钟 | 高 |
| 运行Notebook | 1-2小时 | 高 |
| 理解和调整代码 | 2-3小时 | 中 |
| 撰写报告 | 3-4小时 | 高 |
| 最终审核 | 1小时 | 中 |
| **总计** | **1-2天** | - |

---

## ❓ 常见问题

### Q1: Jupyter Notebook无法启动怎么办？

```bash
# 尝试使用jupyter lab替代
jupyter lab robot_navigation_analysis.ipynb

# 或者直接在命令行中运行Python脚本版本
python3 robot_navigation_analysis.py  # 需要先转换
```

### Q2: 数据集列名和代码不匹配怎么办？

打开Notebook后，先运行前几个单元格查看数据集的列名，然后根据实际情况调整：

```python
# 查看所有列名
print(df.columns.tolist())

# 根据实际列名调整代码
# 例如，如果目标列叫 'floor_type' 而不是 'surface'
df_clean['surface_encoded'] = le.fit_transform(df_clean['floor_type'])
```

### Q3: 图表中文显示乱码怎么办？

```python
# 在Notebook开头添加
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
```

### Q4: 模型训练太慢怎么办？

```python
# 减少模型复杂度
rf_model = RandomForestClassifier(
    n_estimators=100,  # 从200降到100
    max_depth=15,      # 限制树的深度
    n_jobs=-1          # 使用所有CPU核心
)
```

---

## 📝 提交清单

在提交前，请确保准备好以下文件：

- [ ] 电子版报告（Word或PDF格式）
- [ ] 完整的Jupyter Notebook代码文件
- [ ] 所有生成的图表（figures/目录）
- [ ] 纸质版报告（由课代表收齐）

**截止时间**：第十周 周二（2025.11.14）23:59

**提交方式**：
1. 电子版：上传到学习通平台
2. 纸质版：交给课代表，统一送到学院418办公室

---

## 💡 提示

1. **及早开始**：数据分析需要时间理解和调试，不要等到最后一天
2. **保存进度**：经常保存Notebook，避免丢失工作成果
3. **理解代码**：不要只是运行代码，要理解每一步在做什么
4. **创新分析**：在完成基本要求后，可以尝试更深入的分析获得加分
5. **图表质量**：确保图表清晰、标签完整、有标题

---

## 🆘 获取帮助

如果遇到问题：
1. 查看代码中的注释和文档
2. 检查setup_check.py的输出信息
3. 搜索相关错误信息
4. 咨询同学或老师

---

**祝您顺利完成课程报告！** 🎉
