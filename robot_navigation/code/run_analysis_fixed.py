#!/usr/bin/env python3
"""
修复数据泄漏后的机器人导航数据分析脚本
移除file_id等泄漏特征,重新训练模型
"""

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

import matplotlib
matplotlib.use('Agg')  # 使用非交互式后端
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, roc_curve, roc_auc_score
)
import joblib

# 设置随机种子
np.random.seed(42)

plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

print("=" * 80)
print("室内机器人导航数据分析 - 修复版")
print("=" * 80)

# 1. 加载数据
print("\n[1/8] 加载数据...")
df = pd.read_csv('../data/sensor_readings_2.csv')
print(f"✅ 数据形状: {df.shape}")

# 2. 数据清洗
print("\n[2/8] 数据清洗...")
df_clean = df.copy()

# 标签编码
le = LabelEncoder()
df_clean['surface_encoded'] = le.fit_transform(df_clean['surface'])
print(f"✅ 目标类别: {list(le.classes_)}")
print(f"   类别分布: {df_clean['surface'].value_counts().to_dict()}")

# 3. 特征选择 - 移除数据泄漏特征
print("\n[3/8] 特征工程 - 移除数据泄漏特征...")

leakage_features = ['file_id', 'direction', 'horn']
print("⚠️  移除以下泄漏特征:")
for feat in leakage_features:
    if feat in df_clean.columns:
        print(f"   - {feat}")

feature_cols = [col for col in df_clean.columns
               if col not in ['surface', 'surface_encoded'] + leakage_features
               and df_clean[col].dtype in [np.int64, np.float64]]

X = df_clean[feature_cols].values
y = df_clean['surface_encoded'].values

print(f"✅ 特征数量: {len(feature_cols)}")
print(f"   特征列表: {feature_cols[:5]}...")

# 4. 标准化
print("\n[4/8] 数据标准化...")
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print("✅ 标准化完成")

# 5. 划分数据集
print("\n[5/8] 划分训练集和测试集...")
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y
)
print(f"✅ 训练集: {X_train.shape}, 测试集: {X_test.shape}")

# 6. 训练模型
print("\n[6/8] 训练模型...")
results = []

# 逻辑回归
print("  [1/3] 逻辑回归...")
lr_model = LogisticRegression(max_iter=1000, random_state=42)
lr_model.fit(X_train, y_train)
y_pred_lr = lr_model.predict(X_test)
y_pred_proba_lr = lr_model.predict_proba(X_test)
cv_scores_lr = cross_val_score(lr_model, X_train, y_train, cv=5, scoring='accuracy')

results.append({
    '模型': '逻辑回归',
    '准确率': accuracy_score(y_test, y_pred_lr),
    '精确率': precision_score(y_test, y_pred_lr, average='weighted'),
    '召回率': recall_score(y_test, y_pred_lr, average='weighted'),
    'F1分数': f1_score(y_test, y_pred_lr, average='weighted'),
    '交叉验证': cv_scores_lr.mean()
})

print(f"      准确率: {results[-1]['准确率']:.4f}")
print(f"      F1分数: {results[-1]['F1分数']:.4f}")
print(f"      交叉验证: {results[-1]['交叉验证']:.4f}")

# 随机森林
print("  [2/3] 随机森林...")
rf_model = RandomForestClassifier(n_estimators=200, max_depth=20,
                                 min_samples_split=5, random_state=42, n_jobs=-1)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)
y_pred_proba_rf = rf_model.predict_proba(X_test)
cv_scores_rf = cross_val_score(rf_model, X_train, y_train, cv=5, scoring='accuracy')

results.append({
    '模型': '随机森林',
    '准确率': accuracy_score(y_test, y_pred_rf),
    '精确率': precision_score(y_test, y_pred_rf, average='weighted'),
    '召回率': recall_score(y_test, y_pred_rf, average='weighted'),
    'F1分数': f1_score(y_test, y_pred_rf, average='weighted'),
    '交叉验证': cv_scores_rf.mean()
})

print(f"      准确率: {results[-1]['准确率']:.4f}")
print(f"      F1分数: {results[-1]['F1分数']:.4f}")
print(f"      交叉验证: {results[-1]['交叉验证']:.4f}")

# SVM
print("  [3/3] SVM...")
svm_model = SVC(kernel='rbf', C=1.0, gamma='scale', probability=True, random_state=42)
svm_model.fit(X_train, y_train)
y_pred_svm = svm_model.predict(X_test)
y_pred_proba_svm = svm_model.predict_proba(X_test)
cv_scores_svm = cross_val_score(svm_model, X_train, y_train, cv=5, scoring='accuracy')

results.append({
    '模型': 'SVM',
    '准确率': accuracy_score(y_test, y_pred_svm),
    '精确率': precision_score(y_test, y_pred_svm, average='weighted'),
    '召回率': recall_score(y_test, y_pred_svm, average='weighted'),
    'F1分数': f1_score(y_test, y_pred_svm, average='weighted'),
    '交叉验证': cv_scores_svm.mean()
})

print(f"      准确率: {results[-1]['准确率']:.4f}")
print(f"      F1分数: {results[-1]['F1分数']:.4f}")
print(f"      交叉验证: {results[-1]['交叉验证']:.4f}")

# 7. 生成图表
print("\n[7/8] 生成分析图表...")

# 模型对比图
results_df = pd.DataFrame(results)
fig, ax = plt.subplots(figsize=(12, 6))
x = np.arange(4)
width = 0.25
metrics = ['准确率', '精确率', '召回率', 'F1分数']
ax.bar(x - width, results_df.iloc[0][1:5], width, label='逻辑回归', alpha=0.8)
ax.bar(x, results_df.iloc[1][1:5], width, label='随机森林', alpha=0.8)
ax.bar(x + width, results_df.iloc[2][1:5], width, label='SVM', alpha=0.8)
ax.set_xlabel('Evaluation Metrics', fontsize=12)
ax.set_ylabel('Score', fontsize=12)
ax.set_title('Model Performance Comparison (Fixed)', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(metrics)
ax.legend()
ax.grid(True, alpha=0.3, axis='y')
ax.set_ylim([0.5, 1.0])
plt.tight_layout()
plt.savefig('../figures/08_model_comparison_fixed.png', dpi=300, bbox_inches='tight')
print("  ✅ 08_model_comparison_fixed.png")

# 混淆矩阵
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
models = [
    ('Logistic Regression', y_pred_lr),
    ('Random Forest', y_pred_rf),
    ('SVM', y_pred_svm)
]
for idx, (name, y_pred) in enumerate(models):
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
               xticklabels=le.classes_, yticklabels=le.classes_,
               ax=axes[idx])
    axes[idx].set_title(f'{name}\nConfusion Matrix', fontsize=12)
    axes[idx].set_ylabel('True Label')
    axes[idx].set_xlabel('Predicted Label')
plt.tight_layout()
plt.savefig('../figures/09_confusion_matrices_fixed.png', dpi=300, bbox_inches='tight')
print("  ✅ 09_confusion_matrices_fixed.png")

# ROC曲线
plt.figure(figsize=(10, 8))
models_proba = [
    ('Logistic Regression', y_pred_proba_lr[:, 1]),
    ('Random Forest', y_pred_proba_rf[:, 1]),
    ('SVM', y_pred_proba_svm[:, 1])
]
for name, y_score in models_proba:
    fpr, tpr, _ = roc_curve(y_test, y_score)
    auc_score = roc_auc_score(y_test, y_score)
    plt.plot(fpr, tpr, label=f'{name} (AUC = {auc_score:.3f})', linewidth=2)
plt.plot([0, 1], [0, 1], 'k--', label='Random Guess', linewidth=2)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate', fontsize=12)
plt.ylabel('True Positive Rate', fontsize=12)
plt.title('ROC Curves (Fixed)', fontsize=14)
plt.legend(loc="lower right", fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('../figures/10_roc_curves_fixed.png', dpi=300, bbox_inches='tight')
print("  ✅ 10_roc_curves_fixed.png")

# 特征重要性
feature_importance = pd.DataFrame({
    'Feature': feature_cols,
    'Importance': rf_model.feature_importances_
}).sort_values('Importance', ascending=False)

plt.figure(figsize=(10, 10))
top_n = min(20, len(feature_importance))
top_features = feature_importance.head(top_n)
plt.barh(range(len(top_features)), top_features['Importance'], color='steelblue', alpha=0.8)
plt.yticks(range(len(top_features)), top_features['Feature'])
plt.xlabel('Importance Score', fontsize=12)
plt.title(f'Top {top_n} Feature Importance (Random Forest)', fontsize=14)
plt.gca().invert_yaxis()
plt.grid(True, alpha=0.3, axis='x')
plt.tight_layout()
plt.savefig('../figures/11_feature_importance_fixed.png', dpi=300, bbox_inches='tight')
print("  ✅ 11_feature_importance_fixed.png")

# 8. 保存模型和结果
print("\n[8/8] 保存模型和结果...")
joblib.dump(rf_model, '../code/best_model_fixed.pkl')
joblib.dump(scaler, '../code/scaler_fixed.pkl')
joblib.dump(le, '../code/label_encoder_fixed.pkl')
print("  ✅ best_model_fixed.pkl")
print("  ✅ scaler_fixed.pkl")
print("  ✅ label_encoder_fixed.pkl")

results_df.to_csv('../report/model_comparison_fixed.csv', index=False, encoding='utf-8-sig')
feature_importance.to_csv('../report/feature_importance_fixed.csv', index=False, encoding='utf-8-sig')
print("  ✅ model_comparison_fixed.csv")
print("  ✅ feature_importance_fixed.csv")

# 最终总结
print("\n" + "=" * 80)
print("🎉 分析完成!")
print("=" * 80)
print("\n📊 模型性能对比:")
print(results_df.to_string(index=False))

print(f"\n🔑 Top 5 重要特征:")
for idx, row in feature_importance.head(5).iterrows():
    print(f"  {idx+1}. {row['Feature']}: {row['Importance']:.4f}")

print("\n✅ 所有图表已保存到 ../figures/ 目录")
print("✅ 所有模型已保存到 ../code/ 目录")
print("=" * 80)
