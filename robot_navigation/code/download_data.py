#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数据集下载辅助脚本
Indoor Robot Navigation Dataset (IRND)
"""

import os
import sys
import subprocess
from pathlib import Path

# 数据集信息
DATASET_URL = "https://www.kaggle.com/datasets/narayananpp/indoor-robot-navigation-dataset-irnd"
DATASET_SLUG = "narayananpp/indoor-robot-navigation-dataset-irnd"
DATA_DIR = Path(__file__).parent.parent / "data"

def print_header(text):
    """打印标题"""
    print("\n" + "=" * 60)
    print(text)
    print("=" * 60 + "\n")

def check_kaggle_api():
    """检查Kaggle API是否可用"""
    try:
        import kaggle
        return True
    except ImportError:
        return False

def check_kaggle_config():
    """检查Kaggle API配置"""
    kaggle_json = Path.home() / ".kaggle" / "kaggle.json"
    return kaggle_json.exists()

def install_kaggle_api():
    """安装Kaggle API"""
    print("正在安装Kaggle API...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "--user", "kaggle"],
                      check=True)
        print("✅ Kaggle API安装成功")
        return True
    except subprocess.CalledProcessError:
        print("❌ Kaggle API安装失败")
        return False

def setup_kaggle_config():
    """设置Kaggle API配置"""
    print_header("Kaggle API配置向导")

    print("要使用Kaggle API，您需要：")
    print("1. 拥有Kaggle账户（https://www.kaggle.com）")
    print("2. 下载API Token（kaggle.json文件）\n")

    print("📝 获取API Token的步骤：")
    print("   1. 访问 https://www.kaggle.com/account")
    print("   2. 向下滚动到 'API' 部分")
    print("   3. 点击 'Create New API Token'")
    print("   4. 下载得到 kaggle.json 文件\n")

    kaggle_dir = Path.home() / ".kaggle"
    kaggle_json = kaggle_dir / "kaggle.json"

    if kaggle_json.exists():
        print(f"✅ 已找到配置文件: {kaggle_json}")
        return True

    # 提示用户输入kaggle.json的位置
    print(f"\n请将下载的 kaggle.json 文件放到: {kaggle_dir}")
    print("或者输入 kaggle.json 的当前路径：")

    source_path = input("文件路径（回车跳过手动配置）: ").strip()

    if source_path:
        source_path = Path(source_path).expanduser()
        if source_path.exists():
            # 创建.kaggle目录
            kaggle_dir.mkdir(exist_ok=True)

            # 复制文件
            import shutil
            shutil.copy(source_path, kaggle_json)

            # 设置权限
            kaggle_json.chmod(0o600)

            print(f"✅ 配置文件已复制到: {kaggle_json}")
            return True
        else:
            print(f"❌ 文件不存在: {source_path}")
            return False
    else:
        print("\n⚠️  跳过自动配置")
        print(f"请手动将 kaggle.json 复制到: {kaggle_dir}")
        print(f"然后运行: chmod 600 {kaggle_json}")
        return False

def download_with_kaggle_api():
    """使用Kaggle API下载数据集"""
    print_header("使用Kaggle API下载数据集")

    # 确保数据目录存在
    DATA_DIR.mkdir(exist_ok=True)

    print(f"下载目录: {DATA_DIR.absolute()}")
    print(f"数据集: {DATASET_SLUG}\n")

    try:
        import kaggle

        # 下载数据集
        print("正在下载数据集...")
        kaggle.api.dataset_download_files(
            DATASET_SLUG,
            path=str(DATA_DIR),
            unzip=True
        )

        print("\n✅ 数据集下载成功！")

        # 列出下载的文件
        files = list(DATA_DIR.glob("*.csv"))
        if files:
            print(f"\n已下载的文件:")
            for f in files:
                size_mb = f.stat().st_size / (1024 * 1024)
                print(f"  - {f.name} ({size_mb:.2f} MB)")

        return True

    except Exception as e:
        print(f"\n❌ 下载失败: {e}")
        return False

def manual_download_guide():
    """显示手动下载指南"""
    print_header("手动下载指南")

    print("📥 手动下载数据集步骤：\n")
    print("1. 访问数据集页面：")
    print(f"   {DATASET_URL}\n")
    print("2. 点击页面上的 'Download' 按钮")
    print("   （如果没有Kaggle账户，需要先注册）\n")
    print("3. 下载完成后，解压zip文件\n")
    print("4. 将解压后的CSV文件复制到：")
    print(f"   {DATA_DIR.absolute()}\n")
    print("5. 验证安装：")
    print("   python3 code/setup_check.py\n")

def main():
    """主函数"""
    print_header("室内机器人导航数据集下载工具")

    print("本工具将帮助您下载Indoor Robot Navigation Dataset (IRND)\n")
    print("请选择下载方式：")
    print("  1) 使用Kaggle API自动下载（推荐）")
    print("  2) 查看手动下载指南")
    print("  3) 退出")

    choice = input("\n请选择 [1-3]: ").strip()

    if choice == "1":
        # 使用Kaggle API
        print()

        # 检查是否已安装
        if not check_kaggle_api():
            print("⚠️  未安装Kaggle API")
            install_choice = input("是否现在安装? [y/n]: ").strip().lower()
            if install_choice == 'y':
                if not install_kaggle_api():
                    print("\n安装失败，请使用手动下载方式")
                    manual_download_guide()
                    return
            else:
                manual_download_guide()
                return

        # 检查配置
        if not check_kaggle_config():
            print("\n⚠️  Kaggle API未配置")
            if not setup_kaggle_config():
                print("\n配置失败，请使用手动下载方式")
                manual_download_guide()
                return

        # 下载
        if download_with_kaggle_api():
            print("\n" + "=" * 60)
            print("✅ 完成！数据集已准备就绪")
            print("=" * 60)
            print("\n下一步：运行数据分析")
            print("  cd code")
            print("  jupyter notebook robot_navigation_analysis.ipynb")
        else:
            print("\n自动下载失败，请使用手动下载方式")
            manual_download_guide()

    elif choice == "2":
        # 手动下载指南
        manual_download_guide()

    elif choice == "3":
        print("\n退出")
        return

    else:
        print("\n无效选择")
        return

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n操作已取消")
        sys.exit(0)
