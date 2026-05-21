# AGENTS.md

`docs/getting-started/` 是读者进入 TradeCat Research 的第一层入口，负责解释知识库的阅读路径、学习框架和贡献路径。

## 目录结构

```text
getting-started/
├── AGENTS.md
├── index.md
├── knowledge-map.md
├── quant-trading-knowledge-system.md
└── contribution-path.md
```

## 文件职责

- `index.md`：入门页，给出第一批建议阅读链接。
- `knowledge-map.md`：用七层结构组织量化研究全局知识地图。
- `quant-trading-knowledge-system.md`：用点、线、面、体结构说明量化交易学习和研究系统。
- `contribution-path.md`：说明新增研究资料、策略主题和数据源的贡献路径。

## 维护规则

- 新加入门级核心文档时，必须同步更新 `index.md` 和根目录 `README.md` 的知识索引。
- 入门文档只负责总览、路径和框架，不承载具体策略细节；具体策略应进入 `docs/strategies/`。
- 涉及风险、投资建议或实盘边界时，必须链接或引用 `docs/compliance/disclaimer.md`。
