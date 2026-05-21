# 贡献路线

## 新增一篇研究资料

1. 从 `docs/contribution-templates/research-note.md` 复制模板。
2. 填写问题、假设、数据来源、方法、结论和风险。
3. 把新文档放到最匹配的主题目录。
4. 更新 `mkdocs.yml` 导航。
5. 提交 Pull Request。

## 新增一个策略主题

1. 从 `docs/contribution-templates/strategy-card.md` 复制模板。
2. 写清 alpha 假设、交易标的、入场、出场、风控和交易成本。
3. 如果包含回测结果，补充样本期、费用、滑点、数据频率和样本外验证。
4. 把风险和失效条件放在策略正文中，不要单独藏在附录。

## 新增一个数据源

1. 从 `docs/contribution-templates/dataset-card.md` 复制模板。
2. 写清授权方式、字段、频率、覆盖范围、延迟、质量问题和不可用场景。
3. 不提交无法再分发的原始数据。
