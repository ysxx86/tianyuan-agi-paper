# 论文目录

本目录包含论文相关的所有文件。

## 目录结构

```
paper/
├── README.md           # 本说明文件
├── pdf/                # 论文PDF文件
├── latex/              # LaTeX源文件
│   ├── main.tex        # 主文件
│   ├── sections/       # 章节文件
│   └── bibliography.bib # 参考文献
└── figures/            # 图表文件
    ├── png/            # PNG格式图片
    ├── pdf/            # PDF格式图片
    └── svg/            # SVG格式图片
```

## 文件说明

### PDF文件
- 论文的最终版本PDF文件
- 包含投稿版本和最终发表版本

### LaTeX源文件
- 论文的LaTeX源代码
- 包含所有章节、公式、图表源码
- 可直接编译生成PDF

### 图表文件
- 论文中使用的所有图表
- 按格式分类存储
- 建议使用矢量格式（PDF/SVG）以保证打印质量

## 使用说明

1. 编译LaTeX源文件需安装完整的TeX发行版
2. 推荐使用XeLaTeX或LuaLaTeX编译
3. 图表文件路径已在LaTeX中配置好，无需手动修改
