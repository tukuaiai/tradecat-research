# 工具资源

## 文档构建

- MkDocs Material：用于构建知识库站点。
- GitHub Pages：用于发布静态文档站点。
- GitHub Actions：用于构建和发布自动化。

## 量化研究工具

| 名称 | 类型 | 用途 | 备注 |
|---|---|---|---|
| pandas | Python 库 | 表格和时间序列处理 | 适合研究原型 |
| NumPy | Python 库 | 数值计算 | 基础依赖 |
| statsmodels | Python 库 | 统计建模 | 回归和时间序列 |
| vectorbt | Python 库 | 向量化回测 | 适合快速实验 |
| Zipline Reloaded | Python 框架 | 事件驱动回测 | 适合复杂回测 |
| Backtrader | Python 框架 | 回测与策略原型 | 社区资料较多 |

## 选型原则

优先复用成熟工具。只有当现有工具无法满足数据模型、执行语义或可复现要求时，才自研核心能力。
