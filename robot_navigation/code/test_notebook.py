#!/usr/bin/env python3
"""
测试Notebook是否能完整运行
按顺序执行所有关键cell的代码
"""

import sys
sys.path.insert(0, '..')

print("=" * 80)
print("测试 Notebook 完整性")
print("=" * 80)
print()

# Cell 2: 导入库
print("[1/10] 导入库...")
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, f1_score
np.random.seed(42)
print("✅ 完成")

# Cell 4: 加载数据
print("\n[2/10] 加载数据...")
df = pd.read_csv('../data/sensor_readings_2.csv')
print(f"✅ 完成: {df.shape}")

# Cell 14: 标签编码
print("\n[3/10] 标签编码...")
df_clean = df.copy()
le = LabelEncoder()
df_clean['surface_encoded'] = le.fit_transform(df_clean['surface'])
print(f"✅ 完成: {list(le.classes_)}")

# Cell 23: 特征选择 (关键!)
print("\n[4/10] 特征选择...")
leakage_features = ['file_id', 'direction', 'horn']
print(f"  移除泄漏特征: {leakage_features}")

feature_cols = [col for col in df_clean.columns
               if col not in ['surface', 'surface_encoded'] + leakage_features
               and df_clean[col].dtype in [np.int64, np.float64]]

X = df_clean[feature_cols].values
y = df_clean['surface_encoded'].values

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print(f"✅ 完成: {len(feature_cols)}个特征")

# Cell 27: 划分数据集
print("\n[5/10] 划分数据集...")
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y
)
print(f"✅ 完成: 训练集{X_train.shape}, 测试集{X_test.shape}")

# Cell 29: 逻辑回归
print("\n[6/10] 训练逻辑回归...")
lr_model = LogisticRegression(max_iter=1000, random_state=42)
lr_model.fit(X_train, y_train)
y_pred_lr = lr_model.predict(X_test)
acc_lr = accuracy_score(y_test, y_pred_lr)
print(f"✅ 完成: 准确率 {acc_lr:.4f}")

# Cell 31: 随机森林
print("\n[7/10] 训练随机森林...")
rf_model = RandomForestClassifier(n_estimators=200, max_depth=20,
                                 min_samples_split=5, random_state=42, n_jobs=-1)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)
acc_rf = accuracy_score(y_test, y_pred_rf)
print(f"✅ 完成: 准确率 {acc_rf:.4f}")

# Cell 33: SVM
print("\n[8/10] 训练SVM...")
svm_model = SVC(kernel='rbf', C=1.0, gamma='scale', probability=True, random_state=42)
svm_model.fit(X_train, y_train)
y_pred_svm = svm_model.predict(X_test)
acc_svm = accuracy_score(y_test, y_pred_svm)
print(f"✅ 完成: 准确率 {acc_svm:.4f}")

# Cell 41: 特征重要性
print("\n[9/10] 计算特征重要性...")
feature_importance = pd.DataFrame({
    'Feature': feature_cols,
    'Importance': rf_model.feature_importances_
}).sort_values('Importance', ascending=False)
print(f"✅ 完成: Top特征是 {feature_importance.iloc[0]['Feature']}")

# Cell 47: 项目总结
print("\n[10/10] 生成项目总结...")
print(f"  - 样本总数: {len(df)}")
print(f"  - 清洗后样本数: {len(df_clean)}")
print(f"  - 特征数量: {len(feature_cols)}")
print(f"  - 目标类别数: {len(le.classes_)}")
print(f"  - 类别: {', '.join(le.classes_)}")
print("✅ 完成")

# 最终验证
print("\n" + "=" * 80)
print("✅ Notebook 完整性测试通过!")
print("=" * 80)
print()
print("📊 模型性能:")
print(f"  逻辑回归: {acc_lr:.4f} (应该约85%)")
print(f"  随机森林: {acc_rf:.4f} (应该约99%)")
print(f"  SVM:      {acc_svm:.4f} (应该约99%)")
print()

if acc_lr > 0.95:
    print("⚠️  警告: 逻辑回归准确率太高,可能数据泄漏未修复!")
    print("   请检查feature_cols是否包含file_id")
elif acc_rf > 0.995 and acc_lr < 0.90 and acc_lr > 0.80:
    print("✅ 结果正常! 数据泄漏已修复,模型性能合理!")
else:
    print("⚠️  结果异常,请检查代码")

print()
print("🎉 可以在Jupyter中运行了!")
