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
