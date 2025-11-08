#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数据下载和环境检查辅助脚本
Indoor Robot Navigation Dataset
"""

import os
import sys

def check_environment():
    """检查Python环境和必要的库"""
    print("=" * 60)
    print("环境检查")
    print("=" * 60)

    # 检查Python版本
    print(f"\nPython版本: {sys.version}")
    if sys.version_info < (3, 8):
        print("⚠️  警告：建议使用Python 3.8或更高版本")
    else:
        print("✅ Python版本符合要求")

    # 检查必要的库
    required_packages = [
        'pandas', 'numpy', 'matplotlib', 'seaborn',
        'sklearn', 'jupyter', 'joblib'
    ]

    missing_packages = []

    print("\n检查必要的Python包:")
    for package in required_packages:
        try:
            if package == 'sklearn':
                __import__('sklearn')
                print(f"  ✅ {package}")
            else:
                __import__(package)
                print(f"  ✅ {package}")
        except ImportError:
            print(f"  ❌ {package} - 未安装")
            missing_packages.append(package)

    if missing_packages:
        print(f"\n⚠️  缺少以下包: {', '.join(missing_packages)}")
        print("\n请运行以下命令安装:")
        print("  pip install -r requirements.txt")
        return False
    else:
        print("\n✅ 所有必要的包都已安装")
        return True

def check_data():
    """检查数据文件是否存在"""
    print("\n" + "=" * 60)
    print("数据文件检查")
    print("=" * 60)

    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')

    if not os.path.exists(data_dir):
        print(f"❌ 数据目录不存在: {data_dir}")
        return False

    # 检查可能的数据文件
    possible_files = [
        'sensor_readings_2.csv',
        'sensor_readings_24.csv',
        'dataset.csv',
    ]

    found_files = []
    for root, dirs, files in os.walk(data_dir):
        for file in files:
            if file.endswith('.csv'):
                found_files.append(os.path.join(root, file))

    if found_files:
        print(f"\n✅ 找到以下数据文件:")
        for f in found_files:
            size = os.path.getsize(f) / (1024 * 1024)  # MB
            print(f"  - {os.path.basename(f)} ({size:.2f} MB)")
        return True
    else:
        print(f"\n❌ 在 {data_dir} 中未找到CSV数据文件")
        print("\n请按照以下步骤下载数据集:")
        print("  1. 访问 https://www.kaggle.com/datasets/mrisdal/indoor-robot-navigation-dataset")
        print("  2. 点击 'Download' 按钮下载数据集")
        print("  3. 解压后将CSV文件放到 robot_navigation/data/ 目录")
        return False

def download_with_kaggle():
    """使用Kaggle API下载数据集（如果已安装）"""
    try:
        import kaggle
        print("\n检测到Kaggle API，尝试自动下载...")

        # 检查Kaggle配置
        kaggle_json = os.path.expanduser("~/.kaggle/kaggle.json")
        if not os.path.exists(kaggle_json):
            print("❌ 未找到Kaggle API配置文件")
            print("\n请按照以下步骤配置:")
            print("  1. 访问 https://www.kaggle.com/account")
            print("  2. 点击 'Create New API Token'")
            print("  3. 将下载的 kaggle.json 放到 ~/.kaggle/ 目录")
            print("  4. 运行: chmod 600 ~/.kaggle/kaggle.json")
            return False

        # 下载数据集
        data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
        os.makedirs(data_dir, exist_ok=True)

        print(f"下载数据集到: {data_dir}")
        # 注意：需要根据实际的Kaggle数据集路径调整
        # kaggle.api.dataset_download_files('mrisdal/indoor-robot-navigation-dataset',
        #                                   path=data_dir, unzip=True)
        print("⚠️  请手动确认数据集的Kaggle路径并取消上面代码的注释")
        return False

    except ImportError:
        print("\n未安装Kaggle API")
        print("如需使用Kaggle API下载，请运行: pip install kaggle")
        return False

def create_directory_structure():
    """确保目录结构完整"""
    base_dir = os.path.join(os.path.dirname(__file__), '..')

    directories = [
        'data',
        'code',
        'report',
        'figures'
    ]

    print("\n" + "=" * 60)
    print("目录结构检查")
    print("=" * 60)

    for dir_name in directories:
        dir_path = os.path.join(base_dir, dir_name)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            print(f"  ✅ 创建目录: {dir_name}/")
        else:
            print(f"  ✅ 目录已存在: {dir_name}/")

def main():
    """主函数"""
    print("\n" + "=" * 60)
    print("室内机器人导航数据分析 - 环境准备检查")
    print("=" * 60)

    # 创建目录结构
    create_directory_structure()

    # 检查环境
    env_ok = check_environment()

    # 检查数据
    data_ok = check_data()

    # 如果数据不存在，尝试用Kaggle下载
    if not data_ok:
        download_with_kaggle()

    # 总结
    print("\n" + "=" * 60)
    print("检查总结")
    print("=" * 60)

    if env_ok and data_ok:
        print("\n✅ 环境准备完成！可以开始分析了")
        print("\n运行以下命令启动Jupyter Notebook:")
        print("  cd robot_navigation/code")
        print("  jupyter notebook robot_navigation_analysis.ipynb")
    else:
        print("\n⚠️  还有一些准备工作需要完成")
        if not env_ok:
            print("  - 安装缺失的Python包")
        if not data_ok:
            print("  - 下载并放置数据集文件")

    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
