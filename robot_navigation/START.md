# 🚀 开始使用 - 室内机器人导航数据分析项目

欢迎！这是一个完整的Python数据分析课程报告项目。

---

## ⚡ 最快开始方式

只需3个命令：

```bash
cd /home/tong/projects/work/final/robot_navigation
bash start.sh
```

脚本会引导您完成所有设置步骤！

---

## 📚 项目文档索引

| 文档 | 用途 | 推荐阅读顺序 |
|-----|------|------------|
| **START.md** | 本文件 - 快速入门 | 1️⃣ 首先阅读 |
| **QUICKSTART.md** | 详细操作指南 | 2️⃣ 深入了解 |
| **PROJECT_STATUS.md** | 项目进度跟踪 | 3️⃣ 了解进度 |
| **README.md** | 项目总体说明 | 4️⃣ 技术细节 |

---

## 🎯 三步完成项目

### 第一步：环境准备（30分钟）

#### 选项A：使用自动脚本（推荐）

```bash
cd /home/tong/projects/work/final/robot_navigation
bash install.sh
```

#### 选项B：手动安装

```bash
# 安装pip
sudo apt update
sudo apt install -y python3-pip

# 安装Python包
pip3 install --user pandas numpy matplotlib seaborn scikit-learn jupyter notebook
```

#### 验证安装

```bash
python3 code/setup_check.py
```

应该看到 "✅ 所有必要的包都已安装"

---

### 第二步：获取数据（15分钟）

#### 选项A：使用下载工具

```bash
python3 code/download_data.py
```

#### 选项B：手动下载

1. 访问：https://www.kaggle.com/datasets/narayananpp/indoor-robot-navigation-dataset-irnd/data
2. 点击 "Download" 按钮（需要Kaggle账号，免费注册）
3. 下载后解压zip文件
4. 将CSV文件放到 `data/` 目录

#### 验证数据

```bash
ls -lh data/*.csv
```

应该看到数据文件

---

### 第三步：运行分析（1-2小时）

```bash
cd code
jupyter notebook robot_navigation_analysis.ipynb
```

**操作步骤**：
1. Jupyter会在浏览器打开
2. 按顺序运行每个单元格（Shift + Enter）
3. 观察输出和图表
4. 所有图表会自动保存到 `../figures/` 目录

**重要提示**：
- 第一次运行时，注意查看数据集的实际列名
- 如果列名不匹配，需要调整代码（查看单元格注释）
- 运行完成后会生成11张图表和多个结果文件

---

## 📝 撰写报告（3-4小时）

### 1. 打开模板

```bash
cd report
# 用编辑器打开 report_template.md
```

### 2. 填充内容

报告模板已经提供了完整框架，您需要：

- ✅ 填写个人信息
- ✅ 根据Notebook输出填写数据
- ✅ 复制粘贴关键统计结果
- ✅ 插入生成的图表
- ✅ 补充分析洞察

### 3. 转换为Word

```bash
# 安装pandoc（如果还没安装）
sudo apt install pandoc

# 转换
pandoc report_template.md -o Python数据分析报告_姓名_学号.docx
```

然后在Word中调整格式和插入图片。

---

## 🗂️ 项目结构

```
robot_navigation/
├── START.md                 ← 你在这里
├── start.sh                 ← 一键启动脚本
├── install.sh               ← 自动安装脚本
├── QUICKSTART.md            ← 详细指南
├── PROJECT_STATUS.md        ← 进度跟踪
├── README.md                ← 项目说明
├── requirements.txt         ← 依赖列表
│
├── data/                    ← 数据文件
│   └── [下载的CSV文件]
│
├── code/                    ← 代码
│   ├── robot_navigation_analysis.ipynb  ← 主分析文件 ⭐
│   ├── setup_check.py       ← 环境检查
│   └── download_data.py     ← 数据下载工具
│
├── figures/                 ← 生成的图表
│   └── [运行后自动生成11张图]
│
└── report/                  ← 报告
    ├── report_template.md   ← 报告模板 ⭐
    ├── model_comparison.csv
    └── feature_importance.csv
```

---

## 🆘 常见问题

### Q: Python包安装失败？

**A**: 尝试使用系统包管理器：
```bash
sudo apt install python3-pandas python3-numpy python3-matplotlib python3-seaborn python3-sklearn
```

### Q: Jupyter Notebook无法启动？

**A**: 检查安装状态：
```bash
python3 -m jupyter --version
```

如果未安装：
```bash
pip3 install --user jupyter notebook
```

### Q: 数据集列名和代码不匹配？

**A**: 在Notebook中先运行：
```python
print(df.columns.tolist())
```

查看实际列名，然后修改相应代码。

### Q: 图表中文显示乱码？

**A**: 在Notebook开头确保有：
```python
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
```

### Q: 模型训练太慢？

**A**: 减少模型复杂度：
```python
rf_model = RandomForestClassifier(
    n_estimators=50,    # 减少树的数量
    max_depth=10,       # 限制深度
    n_jobs=-1           # 使用所有CPU
)
```

---

## ⏰ 时间规划

| 任务 | 建议时间 | 截止提醒 |
|-----|---------|---------|
| 今天（11.02） | 环境+数据 | 完成准备工作 |
| 11.03-11.04 | 运行分析 | 理解结果 |
| 11.05-11.08 | 撰写报告 | 第一稿 |
| 11.09-11.13 | 修改完善 | 多次迭代 |
| 11.14 前 | 最终提交 | ⏰ 23:59截止 |

---

## ✅ 提交清单

提交前确保：

- [ ] 报告内容完整（8000+字）
- [ ] 所有图表都已插入
- [ ] 数据准确无误
- [ ] 个人信息正确
- [ ] Jupyter Notebook代码有注释
- [ ] 电子版和纸质版都准备好

**提交方式**：
1. 电子版：学习通平台
2. 纸质版：课代表收集→学院418办公室

---

## 🎯 预期成果

完成后您将获得：

✨ **一份完整的分析报告**（8000+字）
- 包含摘要、引言、方法、结果、讨论、结论

✨ **11张专业图表**
- 相关性热图、箱线图、ROC曲线、混淆矩阵等

✨ **3个机器学习模型**
- 逻辑回归、随机森林、SVM及性能对比

✨ **可重现的代码**
- Jupyter Notebook，详细注释

✨ **实践建议**
- 基于数据分析的机器人导航优化策略

**预期评分：85-95分** 📈

---

## 🎓 学习建议

1. **不要只运行代码**：理解每一步在做什么
2. **多尝试调参**：观察参数对结果的影响
3. **深入分析**：不要只列数据，要有洞察
4. **创新思考**：提出独特见解可以加分
5. **及时保存**：经常保存Notebook和报告

---

## 📞 获取帮助

遇到问题时：

1. **查看文档**：QUICKSTART.md 有详细说明
2. **运行检查**：`python3 code/setup_check.py`
3. **查看注释**：代码中有详细的中文注释
4. **搜索错误**：复制错误信息搜索解决方案

---

## 🚀 现在开始！

```bash
# 方法1：使用一键启动脚本
bash start.sh

# 方法2：手动执行步骤
python3 code/setup_check.py      # 检查环境
python3 code/download_data.py    # 下载数据
cd code && jupyter notebook robot_navigation_analysis.ipynb  # 分析
```

祝您顺利完成课程报告！💪

---

**最后更新**：2025-11-02
**下一步**：运行 `bash start.sh` 开始！
