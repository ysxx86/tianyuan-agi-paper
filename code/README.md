# 代码目录

本目录包含实验复现所需的所有代码文件。

## 目录结构

```
code/
├── README.md           # 本说明文件
├── requirements.txt    # Python依赖包列表
├── environment.yml     # Conda环境配置文件
├── src/                # 源代码
│   ├── __init__.py
│   ├── data/           # 数据处理模块
│   │   ├── __init__.py
│   │   ├── loader.py   # 数据加载
│   │   └── preprocessor.py # 数据预处理
│   ├── models/         # 模型定义
│   │   ├── __init__.py
│   │   └── model.py    # 模型架构
│   ├── utils/          # 工具函数
│   │   ├── __init__.py
│   │   └── helpers.py  # 辅助函数
│   └── main.py         # 主程序入口
├── scripts/            # 脚本文件
│   ├── train.sh        # 训练脚本
│   ├── test.sh         # 测试脚本
│   └── evaluate.sh     # 评估脚本
├── notebooks/          # Jupyter笔记本
│   ├── exploration.ipynb   # 数据探索
│   └── visualization.ipynb # 可视化分析
└── tests/              # 测试代码
    ├── __init__.py
    ├── test_data.py    # 数据处理测试
    └── test_model.py   # 模型测试
```

## 环境配置

### 方式一：使用pip

```bash
# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或 venv\Scripts\activate  # Windows

# 安装依赖
pip install -r requirements.txt
```

### 方式二：使用Conda

```bash
# 创建环境
conda env create -f environment.yml

# 激活环境
conda activate tianyuan
```

## 运行说明

### 1. 数据准备
```bash
# 下载数据（如需要）
python src/data/download.py

# 预处理数据
python src/data/preprocessor.py
```

### 2. 模型训练
```bash
# 使用默认参数训练
python src/main.py --mode train

# 使用脚本训练（推荐）
bash scripts/train.sh
```

### 3. 模型测试
```bash
# 运行测试
python src/main.py --mode test

# 或使用脚本
bash scripts/test.sh
```

### 4. 结果评估
```bash
# 评估模型性能
python src/main.py --mode evaluate

# 或使用脚本
bash scripts/evaluate.sh
```

## 主要参数说明

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| --mode | str | train | 运行模式：train/test/evaluate |
| --data_dir | str | ../data/ | 数据目录路径 |
| --output_dir | str | ../results/ | 输出目录路径 |
| --epochs | int | 100 | 训练轮数 |
| --batch_size | int | 32 | 批次大小 |
| --learning_rate | float | 0.001 | 学习率 |

## 代码规范

1. **命名规范**：
   - 变量：snake_case（如`data_loader`）
   - 函数：snake_case（如`load_data()`）
   - 类：PascalCase（如`DataLoader`）

2. **注释规范**：
   - 函数使用docstring说明功能、参数、返回值
   - 关键逻辑添加行内注释

3. **代码风格**：
   - 遵循PEP 8规范
   - 使用类型提示（Type Hints）

## 注意事项

- 运行前请确保数据文件已放置在正确位置
- 首次运行建议使用小规模数据测试
- GPU训练请确保CUDA环境配置正确
- 结果文件将自动保存到`../results/`目录
