#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
JSON数据转CSV脚本 - 室内机器人导航数据集
将Kaggle下载的JSON格式数据转换为适合分析的CSV格式

输入: data/archive/outputs/*.json 和 data/archive/outputs_2/*.json
输出: data/sensor_readings_2.csv
"""

import json
import pandas as pd
import numpy as np
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

def extract_features_from_json(json_file):
    """
    从单个JSON文件中提取特征

    参数:
        json_file: JSON文件路径

    返回:
        list: 每条记录的特征字典列表
    """
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)

        records = []

        # 遍历每条记录
        for record in data.get('data', []):
            feature_dict = {}

            # 1. 基础信息
            feature_dict['direction'] = record.get('direction', 'unknown')
            feature_dict['brake'] = record.get('brake', 0)
            feature_dict['horn'] = record.get('horn', 0)

            # 2. 位置信息
            pose = record.get('pose', {})
            feature_dict['x'] = pose.get('x', 0)
            feature_dict['y'] = pose.get('y', 0)
            feature_dict['theta'] = pose.get('theta', 0)

            # 3. 距离传感器数据统计特征
            dists = record.get('dists', [])
            if dists:
                feature_dict['dist_mean'] = np.mean(dists)
                feature_dict['dist_std'] = np.std(dists)
                feature_dict['dist_min'] = np.min(dists)
                feature_dict['dist_max'] = np.max(dists)
                feature_dict['dist_median'] = np.median(dists)
                feature_dict['dist_q25'] = np.percentile(dists, 25)
                feature_dict['dist_q75'] = np.percentile(dists, 75)
                feature_dict['dist_range'] = np.max(dists) - np.min(dists)
                feature_dict['dist_iqr'] = np.percentile(dists, 75) - np.percentile(dists, 25)

                # 分区统计（前、左、右、后）
                n = len(dists)
                front = dists[:n//4]
                left = dists[n//4:n//2]
                right = dists[n//2:3*n//4]
                back = dists[3*n//4:]

                feature_dict['dist_front_mean'] = np.mean(front) if front else 0
                feature_dict['dist_left_mean'] = np.mean(left) if left else 0
                feature_dict['dist_right_mean'] = np.mean(right) if right else 0
                feature_dict['dist_back_mean'] = np.mean(back) if back else 0

                feature_dict['dist_front_min'] = np.min(front) if front else 0
                feature_dict['dist_left_min'] = np.min(left) if left else 0
                feature_dict['dist_right_min'] = np.min(right) if right else 0
                feature_dict['dist_back_min'] = np.min(back) if back else 0
            else:
                # 如果没有距离数据,填充0
                for key in ['dist_mean', 'dist_std', 'dist_min', 'dist_max', 'dist_median',
                           'dist_q25', 'dist_q75', 'dist_range', 'dist_iqr',
                           'dist_front_mean', 'dist_left_mean', 'dist_right_mean', 'dist_back_mean',
                           'dist_front_min', 'dist_left_min', 'dist_right_min', 'dist_back_min']:
                    feature_dict[key] = 0

            # 4. 角度传感器数据统计特征
            angles = record.get('angles', [])
            if angles:
                feature_dict['angle_mean'] = np.mean(angles)
                feature_dict['angle_std'] = np.std(angles)
                feature_dict['angle_min'] = np.min(angles)
                feature_dict['angle_max'] = np.max(angles)
                feature_dict['angle_range'] = np.max(angles) - np.min(angles)
            else:
                for key in ['angle_mean', 'angle_std', 'angle_min', 'angle_max', 'angle_range']:
                    feature_dict[key] = 0

            # 5. 计数器
            feature_dict['counts_left'] = record.get('counts_left', 0)
            feature_dict['counts_right'] = record.get('counts_right', 0)

            # 6. 文件名作为ID（用于区分不同地面）
            file_id = Path(json_file).stem
            feature_dict['file_id'] = file_id

            records.append(feature_dict)

        return records

    except Exception as e:
        print(f"处理文件 {json_file} 时出错: {e}")
        return []


def determine_surface_type(file_id):
    """
    根据文件ID判断地面类型

    根据Kaggle数据集说明:
    - outputs文件夹: 平滑表面 (smooth surface)
    - outputs_2文件��: 粗糙表面 (rough surface)

    参数:
        file_id: 文件编号

    返回:
        str: 'smooth' 或 'rough'
    """
    # 这里需要根据实际数据集的组织方式来判断
    # 暂时返回unknown,后续根据文件夹路径判断
    return 'unknown'


def main():
    """主函数:处理所有JSON文件并合并为CSV"""

    print("="*80)
    print("室内机器人导航数据集 - JSON到CSV转换工具")
    print("="*80)

    # 设置路径
    base_dir = Path(__file__).parent.parent
    data_dir = base_dir / 'data' / 'archive'
    output_file = base_dir / 'data' / 'sensor_readings_2.csv'

    # 查找所有JSON文件
    outputs_dir = data_dir / 'outputs'
    outputs_2_dir = data_dir / 'outputs_2'

    json_files_smooth = list(outputs_dir.glob('*.json')) if outputs_dir.exists() else []
    json_files_rough = list(outputs_2_dir.glob('*.json')) if outputs_2_dir.exists() else []

    print(f"\n📂 数据文件统计:")
    print(f"  - 平滑表面数据 (outputs): {len(json_files_smooth)} 个文件")
    print(f"  - 粗糙表面数据 (outputs_2): {len(json_files_rough)} 个文件")
    print(f"  - 总计: {len(json_files_smooth) + len(json_files_rough)} 个文件")

    if not json_files_smooth and not json_files_rough:
        print("\n❌ 错误: 未找到JSON数据文件!")
        print(f"   请检查路径: {data_dir}")
        return

    # 处理所有文件
    all_records = []

    print("\n🔄 处理平滑表面数据...")
    for i, json_file in enumerate(json_files_smooth, 1):
        if i % 20 == 0 or i == len(json_files_smooth):
            print(f"  进度: {i}/{len(json_files_smooth)}")
        records = extract_features_from_json(json_file)
        for record in records:
            record['surface'] = 'smooth'  # 标记为平滑表面
        all_records.extend(records)

    print("🔄 处理粗糙表面数据...")
    for i, json_file in enumerate(json_files_rough, 1):
        if i % 20 == 0 or i == len(json_files_rough):
            print(f"  进度: {i}/{len(json_files_rough)}")
        records = extract_features_from_json(json_file)
        for record in records:
            record['surface'] = 'rough'  # 标记为粗糙表面
        all_records.extend(records)

    # 转换为DataFrame
    print("\n📊 生成DataFrame...")
    df = pd.DataFrame(all_records)

    # 数据统计
    print(f"\n✅ 数据处理完成!")
    print(f"  - 总记录数: {len(df):,}")
    print(f"  - 特征数量: {len(df.columns)}")
    print(f"\n📋 特征列表:")
    for i, col in enumerate(df.columns, 1):
        print(f"  {i:2d}. {col}")

    print(f"\n🏷️  地面类型分布:")
    print(df['surface'].value_counts())
    print(f"\n比例:")
    print(df['surface'].value_counts(normalize=True))

    # 保存CSV
    print(f"\n💾 保存CSV文件到: {output_file}")
    output_file.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_file, index=False, encoding='utf-8')

    # 数据质量检查
    print(f"\n🔍 数据质量检查:")
    print(f"  - 缺失值总数: {df.isnull().sum().sum()}")
    print(f"  - 重复行数: {df.duplicated().sum()}")

    if df.isnull().sum().sum() > 0:
        print("\n⚠️  存在缺失值的列:")
        missing = df.isnull().sum()
        missing = missing[missing > 0].sort_values(ascending=False)
        for col, count in missing.items():
            print(f"    - {col}: {count} ({count/len(df)*100:.2f}%)")

    print(f"\n📈 数值特征统计摘要:")
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    print(df[numeric_cols].describe().round(3))

    print("\n" + "="*80)
    print("✅ 转换完成! 现在可以运行 Jupyter Notebook 进行分析了")
    print("="*80)
    print(f"\n下一步:")
    print(f"  1. 检查生成的CSV文件: {output_file}")
    print(f"  2. 运行命令: cd code && jupyter notebook robot_navigation_analysis.ipynb")


if __name__ == '__main__':
    main()
