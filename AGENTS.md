# AGENTS.md

本仓库是量化交易知识型文档仓库。所有代理和维护者应优先保持资料可追溯、结构稳定、风险表达清楚。

## 目录结构

```text
.
├── .github/                  # GitHub 协作、模板与自动发布
├── assets/                   # 图片、数据、notebook、脚本等辅助资产
│   └── docs/governance/      # 项目治理包与长期工程记忆
├── docs/                     # 面向读者的知识库正文
│   ├── getting-started/      # 入门、阅读路径、贡献导航
│   ├── foundations/          # 市场、统计、时间序列等基础知识
│   ├── data/                 # 数据源、数据质量、数据字典
│   ├── research/             # 研究流程、回测、实验记录
│   ├── strategies/           # 策略分类与策略卡片
│   ├── risk/                 # 风险、组合、仓位与回撤管理
│   ├── engineering/          # 研究工程化、复现、观测与自动化
│   ├── compliance/           # 免责声明、合规边界与引用规范
│   ├── references/           # 书目、论文、链接和术语索引
│   ├── source/               # 外部素材按原文标题机械拆分后的存档区
│   ├── contribution-templates/ # 投稿和研究模板
│   └── tools/                # 工具链与资源清单
├── mkdocs.yml                # MkDocs Material 站点配置
└── requirements.txt          # 文档构建依赖
```

## 职责边界

- `docs/` 只放面向读者的稳定资料，不放临时任务记录。
- `docs/source/` 放外部素材的原文拆分存档；原则上只做切分、归档和来源保留，不在该目录内改写观点。
- `docs/contribution-templates/` 只放可复制的标准模板，不放具体研究结论。
- `assets/docs/governance/` 只维护工程治理、门禁、ADR、QA 和代理协作规则，不替代 `docs/` 正文。
- `.github/` 只维护 GitHub 协作入口，不承载知识库正文。
- `assets/datasets/` 只允许放小型示例数据或说明文件，不放专有、付费、受限或无法再分发的数据。

## 内容规范

- 文档、注释、Issue 和 PR 文案使用中文。
- 文件名、目录名、配置键和脚本变量优先使用简洁英文。
- 策略、数据和实验相关内容必须写清来源、假设、适用边界和风险。
- 禁止把未验证结论写成事实；不确定内容必须标记为假设、推断或待验证。
- 不重复造轮子：文档构建优先使用 MkDocs Material，流程自动化优先使用 GitHub Actions。

## 变更要求

- 新增一级或二级知识目录时，必须同步更新 `mkdocs.yml` 和本文件。
- 调整仓库架构或职责边界时，必须同步更新本文件。
- 新增研究主题时，优先从 `docs/contribution-templates/` 复制模板。
- 高风险内容变更必须更新 `docs/compliance/disclaimer.md` 或相关风险说明。
