# 🚀 立即执行 - 3步完成数据分析

**当前时间**: 2025-11-02  
**虚拟环境**: ✅ 已创建 (~/venvs/jupyter-env)  
**Jupyter**: ✅ 已安装  
**项目代码**: ✅ 已准备

---

## 📋 接下来的3个命令（按顺序执行）

### 命令1️⃣：安装数据分析包（5分钟）

```bash
source ~/venvs/jupyter-env/bin/activate && pip install pandas numpy matplotlib seaborn scikit-learn joblib
```

**预期输出**：看到 "Successfully installed pandas-x.x.x numpy-x.x.x..." 表示成功

---

### 命令2️⃣：下载数据集（15-30分钟）

```bash
cd /home/tong/projects/work/final/robot_navigation
python code/download_data.py
```

**如果自动下载失败，手动下载**：
1. 浏览器打开：https://www.kaggle.com/datasets/narayananpp/indoor-robot-navigation-dataset-irnd/data
2. 点击 "Download" 按钮
3. 解压zip文件
4. 将CSV文件复制到 `data/` 目录

**验证**：
```bash
ls -lh data/*.csv
```
应该看到CSV文件列表

---

### 命令3️⃣：启动Jupyter Notebook（立即分析）

```bash
cd code
jupyter notebook robot_navigation_analysis.ipynb
```

**浏览器会自动打开，地址类似**：http://localhost:8888

---

## 📝 Jupyter中的操作（1-2小时）

### 基本操作
- **运行单元格**：Shift + Enter
- **保存**：Ctrl + S
- **停止运行**：Kernel → Interrupt

### 运行顺序
1. ✅ 运行第1个单元格 - 导入库
2. ✅ 运行第2个单元格 - 加载数据
3. ✅ 查看数据列名 - `print(df.columns.tolist())`
4. ⚠️ **检查目标变量名** - 如果不是'surface'需要调整
5. ✅ 依次运行所有单元格

### 需要记录的关键数据
- [ ] 总样本数：_______
- [ ] 特征数量：_______
- [ ] 目标类别：_______
- [ ] 逻辑回归准确率：_______%
- [ ] 随机森林准确率：_______%
- [ ] SVM准确率：_______%
- [ ] 最佳模型：_______
- [ ] Top 5重要特征：_______

---

## ✅ 运行完成后检查

```bash
# 检查图表（应该有11张）
ls -lh ../figures/*.png | wc -l

# 检查结果文件
ls -lh ../report/*.csv

# 检查模型文件
ls -lh *.pkl
```

---

## 📅 后续步骤时间表

| 日期 | 任务 | 预计时间 |
|-----|------|---------|
| **今天（11.02）** | 完成上述3个命令 + 运行分析 | 3小时 |
| **明天（11.03）** | 理解结果，优化代码 | 2小时 |
| **11.04-11.08** | 撰写报告 | 每天2小时 |
| **11.09-11.13** | 修改完善报告 | 每天1小时 |
| **11.14 23:59** | ⏰ **提交截止** | - |

---

## 📚 参考文档

- **VENV_GUIDE.md** - 完整虚拟环境使用指南
- **REMAINING_STEPS.md** - 详细后续步骤
- **TODO.md** - 待办清单总览

---

## 💡 重要提示

1. **每次使用前激活虚拟环境**：
   ```bash
   source ~/venvs/jupyter-env/bin/activate
   ```

2. **遇到错误**：
   - 查看错误信息
   - 检查代码注释
   - 查看VENV_GUIDE.md

3. **时间不够**：
   - 减少模型复杂度（降低n_estimators）
   - 使用数据采样（sample函数）

---

## 🎯 今天的目标

- [x] 虚拟环境创建
- [x] Jupyter安装
- [ ] 数据分析包安装 ← **现在执行命令1**
- [ ] 数据集下载
- [ ] 运行完整分析
- [ ] 生成所有图表

---

**现在开始！复制命令1到终端执行** 👇

```bash
source ~/venvs/jupyter-env/bin/activate && pip install pandas numpy matplotlib seaborn scikit-learn joblib
```

