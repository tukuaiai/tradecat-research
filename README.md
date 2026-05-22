# TradeCat Research

TradeCat Research 是一个面向量化交易研究的开源知识库，用于沉淀市场机制、数据工程、策略研究、回测验证、风险控制、交易执行与工程化实践。

本仓库默认采用 Docs as Code 工作流：资料以 Markdown 管理，通过 MkDocs Material 构建站点，并使用 GitHub Pull Request 完成审阅、溯源和持续改进。

## 仓库定位

- 记录可复用的量化研究资料，而不是发布投资建议。
- 优先沉淀可验证来源、研究假设、实验记录和风险边界。
- 将策略想法、数据说明、实验结果和复盘拆成独立文档，避免知识混在聊天记录或临时笔记里。
- 让贡献者能按统一模板提交资料，降低后续维护成本。

## 快速开始

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

本地站点默认运行在 `http://127.0.0.1:8000`。

## 知识索引

字数按 Markdown 源文件去除空白字符后统计，中文按字计，英文和数字按字符计。

### 入门

| 文章 | 文件大小（字数） | 说明 |
|---|---:|---|
| [入门总览](docs/getting-started/index.md) | 245 | 知识库适合人群和第一批阅读入口。 |
| [量化交易知识点线面体](docs/getting-started/quant-trading-knowledge-system.md) | 7608 | 从知识点、知识线、知识面到知识体，建立量化交易学习和研究的总框架。 |
| [知识地图](docs/getting-started/knowledge-map.md) | 289 | 按市场基础、数据、研究、策略、风险、执行和工程复现组织阅读路径。 |
| [贡献路线](docs/getting-started/contribution-path.md) | 413 | 新增研究资料、策略主题和数据源的贡献路径。 |

### 基础

| 文章 | 文件大小（字数） | 说明 |
|---|---:|---|
| [基础总览](docs/foundations/index.md) | 112 | 量化交易基础知识入口。 |
| [市场微观结构](docs/foundations/market-microstructure.md) | 219 | 订单、撮合、流动性、市场机制和交易成本。 |
| [统计基础](docs/foundations/statistics.md) | 176 | 描述统计、假设检验、回归、多重检验和分布风险。 |
| [时间序列](docs/foundations/time-series.md) | 204 | 收益率、平稳性、自相关、波动率和结构突变。 |

### 数据

| 文章 | 文件大小（字数） | 说明 |
|---|---:|---|
| [数据总览](docs/data/index.md) | 109 | 数据源、字段语义、质量控制和使用边界入口。 |
| [数据源](docs/data/data-sources.md) | 166 | 数据源登记表和授权、质量、偏差记录规则。 |
| [数据质量](docs/data/data-quality.md) | 143 | 缺失值、异常值、复权、时区、幸存者偏差等检查项。 |
| [数据字典](docs/data/data-dictionary.md) | 318 | 行情字段、类型、单位、含义和质量约束模板。 |

### 研究

| 文章 | 文件大小（字数） | 说明 |
|---|---:|---|
| [研究总览](docs/research/index.md) | 103 | 从想法到验证的研究入口。 |
| [研究流程](docs/research/research-process.md) | 158 | 从交易假设到数据验证、策略规则、回测和复盘的流程。 |
| [回测框架](docs/research/backtesting.md) | 206 | 回测必须回答的问题、最低指标和常见风险。 |
| [实验记录](docs/research/experiment-log.md) | 151 | 实验编号、问题、假设、数据、方法、结果和后续动作。 |

### 策略

| 文章 | 文件大小（字数） | 说明 |
|---|---:|---|
| [策略总览](docs/strategies/index.md) | 172 | 策略类型、适用市场、实现方式和风险边界入口。 |
| [趋势跟随](docs/strategies/trend-following.md) | 128 | 趋势延续假设、常见实现和震荡市场风险。 |
| [均值回归](docs/strategies/mean-reversion.md) | 144 | 均衡偏离、回归交易和关系失效风险。 |
| [统计套利](docs/strategies/statistical-arbitrage.md) | 133 | 配对、协整、截面中性化和拥挤交易风险。 |
| [执行算法](docs/strategies/execution.md) | 147 | TWAP、VWAP、POV、智能路由和成交建模入口。 |

### 风险

| 文章 | 文件大小（字数） | 说明 |
|---|---:|---|
| [风险总览](docs/risk/index.md) | 110 | 仓位、回撤、组合暴露和尾部风险入口。 |
| [仓位管理](docs/risk/position-sizing.md) | 152 | 固定金额、波动率目标、风险预算和 Kelly 类方法。 |
| [回撤管理](docs/risk/drawdown.md) | 133 | 最大回撤、回撤持续时间、暂停恢复和回撤归因。 |
| [组合风险](docs/risk/portfolio-risk.md) | 126 | 相关性、协方差、风险贡献、因子暴露和压力测试。 |

### 工程化

| 文章 | 文件大小（字数） | 说明 |
|---|---:|---|
| [工程化总览](docs/engineering/index.md) | 120 | 研究复现、审阅和自动化入口。 |
| [研究流水线](docs/engineering/research-pipeline.md) | 124 | 数据采集、校验、特征、信号、回测、风险审查和归档链路。 |
| [可复现研究](docs/engineering/reproducibility.md) | 129 | 数据版本、依赖版本、随机种子、配置和运行命令。 |
| [观测与复盘](docs/engineering/observability.md) | 130 | 研究阶段和实盘阶段的关键观测指标。 |

### 合规与参考

| 文章 | 文件大小（字数） | 说明 |
|---|---:|---|
| [合规总览](docs/compliance/index.md) | 80 | 免责声明、引用规范和公开资料边界入口。 |
| [免责声明](docs/compliance/disclaimer.md) | 172 | 投资、交易、法律和税务建议边界。 |
| [引用规范](docs/compliance/citation-policy.md) | 172 | 论文、书籍、网页和数据源引用规则。 |
| [参考总览](docs/references/index.md) | 104 | 术语、书目、论文和外部资源入口。 |
| [术语表](docs/references/glossary.md) | 205 | Alpha、Beta、Drawdown、Slippage 等核心术语。 |
| [书目与论文](docs/references/bibliography.md) | 178 | 书籍、论文、公开课程和资料索引。 |
| [工具资源](docs/tools/resources.md) | 375 | 文档构建工具和量化研究工具资源。 |

### 原始素材

| 文章 | 文件大小（字数） | 说明 |
|---|---:|---|
| [原始素材目录](docs/source/quant-popular-science/index.md) | 250 | 外部科普素材按原文主题拆分后的存档区。 |
| [AI 量化编程该怎么学](docs/source/quant-popular-science/01-AI量化编程该怎么学-？.md) | 3825 | AI 时代量化编程学习路径。 |
| [量化策略英雄池](docs/source/quant-popular-science/02-量化策略英雄池.md) | 8097 | 按波动和择时维度划分策略类型。 |
| [量化私募的两种模式](docs/source/quant-popular-science/03-量化私募的两种模式.md) | 1926 | 因子工厂模式和 PM 团队模式。 |
| [交易的部署模式](docs/source/quant-popular-science/04-交易的部署模式.md) | 763 | 本地、单节点托管和两地分仓。 |
| [如何用期权合成期货](docs/source/quant-popular-science/05-如何用期权合成期货.md) | 1773 | 用看涨、看跌期权构造合成期货。 |
| [通俗理解期权平价公式](docs/source/quant-popular-science/06-通俗理解期权平价公式.md) | 1399 | 用组合收益结构解释 `S + P = C + PV`。 |
| [算法交易：TWAP、VWAP 与 POV](docs/source/quant-popular-science/07-算法交易：TWAP、VWAP-与-POV.md) | 3808 | 三类常见算法交易执行方式。 |

### 投稿模板

| 模板 | 文件大小（字数） | 说明 |
|---|---:|---|
| [模板总览](docs/contribution-templates/index.md) | 164 | 统一资料结构和审阅入口。 |
| [研究笔记模板](docs/contribution-templates/research-note.md) | 177 | 研究问题、假设、数据、方法、结果和风险模板。 |
| [策略卡片模板](docs/contribution-templates/strategy-card.md) | 211 | Alpha 假设、交易规则、风控、回测和失效条件模板。 |
| [数据集卡片模板](docs/contribution-templates/dataset-card.md) | 174 | 数据来源、覆盖范围、字段、质量和使用限制模板。 |
| [实验记录模板](docs/contribution-templates/experiment-record.md) | 119 | 实验输入、方法、输出、结论和后续动作模板。 |
| [来源卡片模板](docs/contribution-templates/source-card.md) | 127 | 外部来源摘要、可引用内容和授权风险模板。 |

## 主要目录

| 路径 | 职责 |
|---|---|
| `docs/` | 面向读者的知识库正文。 |
| `docs/contribution-templates/` | 研究笔记、策略卡片、数据集卡片等投稿模板。 |
| `assets/docs/governance/` | 项目治理包，记录长期标准、门禁、流程和代理协作规则。 |
| `.github/` | GitHub Actions、Issue 模板、PR 模板和协作入口。 |
| `assets/` | 图片、示例数据、notebook 与辅助脚本的占位目录。 |

## 资料质量原则

1. 可追溯：关键结论必须附来源、数据版本或实验记录。
2. 可复现：策略研究要说明输入、假设、参数、样本期和验证方法。
3. 可审阅：每次贡献只解决一个清晰主题，避免一次 PR 混合多个方向。
4. 风险优先：任何交易相关内容必须说明适用边界、失效条件和风险。

## 许可

- 文档内容默认使用 `CC BY 4.0`，见 [LICENSE-CONTENT.md](LICENSE-CONTENT.md)。
- 仓库中的脚本、配置和代码片段默认使用 `MIT`，见 [LICENSE-CODE.md](LICENSE-CODE.md)。

## 重要声明

本仓库内容仅用于研究、教育和工程交流，不构成投资建议、交易建议、法律建议或税务建议。交易有风险，任何实盘决策都必须由使用者独立承担责任。
