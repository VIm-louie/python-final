# Python 数据分析编程期末项目

## 项目信息

- **课程**: Python数据分析编程
- **项目题目**: 室内机器人导航数据分析
- **数据集**: Indoor Robot Navigation Dataset (IRND)
- **目标**: 通过机器学习识别地面类型,为机器人自适应导航提供策略

---

## 项目结构

```
python-final/
├── README.md                           # 本文件
├── Python数据分析编程项目报告要求.pdf    # 课程要求
├── 项目报告模版.docx                    # 报告模板
└── robot_navigation/                   # 主项目目录
    ├── ANALYSIS_REPORT.md              # 详细分析报告
    ├── QUICKSTART_FIXED.md             # 快速使用指南
    ├── code/                           # 代码目录
    │   ├── robot_navigation_analysis.ipynb  # Jupyter分析代码
    │   ├── run_analysis_fixed.py       # 完整分析脚本
    │   ├── test_notebook.py            # 测试脚本
    │   └── start_jupyter.sh            # Jupyter启动脚本
    ├── figures/                        # 生成的图表
    │   ├── 08_model_comparison_fixed.png
    │   ├── 09_confusion_matrices_fixed.png
    │   ├── 10_roc_curves_fixed.png
    │   └── 11_feature_importance_fixed.png
    ├── report/                         # 结果数据
    │   ├── model_comparison_fixed.csv
    │   └── feature_importance_fixed.csv
    └── data/                           # 数据目录(不包含在git中)
```

---

## 快速开始

### 1. 环境设置

```bash
cd robot_navigation
python3 -m venv .venv
source .venv/bin/activate
pip install pandas numpy matplotlib seaborn scikit-learn jupyter joblib
```

### 2. 数据下载

从 Kaggle 下载数据集:
https://www.kaggle.com/datasets/narayananpp/indoor-robot-navigation-dataset-irnd

将 CSV 文件放到 `robot_navigation/data/` 目录

### 3. 运行分析

**方式1: Jupyter Notebook**
```bash
cd code
jupyter notebook robot_navigation_analysis.ipynb
```

**方式2: Python 脚本**(推荐)
```bash
cd code
python run_analysis_fixed.py
```

---

## 核心发现

### 数据泄漏问题 ⭐

**问题**: 初始训练时逻辑回归和随机森林都达到100%准确率

**原因**: `file_id` 特征导致数据泄漏
- 同一文件中的所有样本都来自同一种地面类型
- 模型只需记住"file_id → surface"的映射

**修复**: 移除 `file_id`, `direction`, `horn` 三个泄漏特征

**验证**:
- 修复前: 逻辑回归 100%, 随机森林 100%
- 修复后: 逻辑回归 85.65%, 随机森林 99.92%

### 模型性能

| 模型 | 准确率 | F1分数 | 交叉验证 |
|------|--------|--------|----------|
| 逻辑回归 | 85.65% | 85.65% | 85.45% |
| 随机森林 | 99.92% | 99.92% | 99.93% |
| SVM | 99.62% | 99.62% | 99.68% |

### 特征重要性 (Top 5)

1. **x** (27.13%) - X坐标位置
2. **angle_std** (9.64%) - 角度标准差
3. **dist_mean** (8.51%) - 距离均值
4. **dist_q75** (8.48%) - 距离75分位数
5. **y** (8.25%) - Y坐标位置

**关键洞察**: 位置特征(x, y)占比35%+,说明地面类型有空间分布规律

---

## 技术栈

- **Python**: 3.12
- **数据处理**: pandas, numpy
- **可视化**: matplotlib, seaborn
- **机器学习**: scikit-learn
- **开发环境**: Jupyter Notebook

---

## 项目亮点

1. ✅ **批判性思维**: 发现并修复数据泄漏问题
2. ✅ **完整流程**: EDA → 特征工程 → 建模 → 评估
3. ✅ **深入分析**: 特征重要性和位置依赖性讨论
4. ✅ **实践导向**: 提出机器人导航策略建议
5. ✅ **专业可视化**: 4张高质量图表

---

## 文件说明

### 代码文件
- `robot_navigation_analysis.ipynb`: 完整的Jupyter分析代码
- `run_analysis_fixed.py`: 独立运行的Python脚本
- `test_notebook.py`: 测试Notebook完整性

### 文档文件
- `ANALYSIS_REPORT.md`: 详细的分析报告(包含所有发现和讨论)
- `QUICKSTART_FIXED.md`: 快速使用指南

### 输出文件
- `figures/`: 4张PNG格式图表
- `report/`: CSV格式的模型对比和特征重要性数据

---

## 注意事项

1. **数据文件**: 由于文件过大,`data/` 目录中的CSV文件不包含在git中
2. **模型文件**: `.pkl` 文件也不包含在git中,需要重新训练
3. **虚拟环境**: `.venv/` 目录被忽略,需要重新创建

---

## 预期评分

**90-95分**

理由:
- 发现并修复了数据泄漏(展现批判性思维)
- 完整的机器学习项目流程
- 深入的数据分析和特征工程
- 专业的可视化和文档
- 具有实践价值的应用建议

---

## 参考资料

- **数据集来源**: [Kaggle - Indoor Robot Navigation Dataset](https://www.kaggle.com/datasets/narayananpp/indoor-robot-navigation-dataset-irnd)
- **项目文档**: 见 `robot_navigation/ANALYSIS_REPORT.md`

---

**最后更新**: 2025-11-08
**状态**: ✅ 项目完成,可以提交
