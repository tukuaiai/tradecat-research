#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
from pathlib import Path


GOV_ROOT = Path("assets/docs/governance")

DEFAULT_DOCS = [
    "INDEX.md",
    "00-start-here/AGENT-ENTRY.md",
    "00-start-here/PROJECT-TOPOLOGY.md",
    "00-start-here/CONTEXT-MAP.md",
    "00-start-here/CONTEXT-ROUTER.md",
]

ROUTES = {
    "feature": {
        "label": "新功能",
        "required": [
            "10-standards/工程质量标准.md",
            "10-standards/非功能性需求标准.md",
            "20-processes/QA计划标准.md",
            "20-processes/代理协作协议.md",
        ],
        "optional": [
            "10-standards/优质代码定义.md",
            "10-standards/术语表.md",
            "40-records/adr/INDEX.md",
        ],
        "outputs": ["QA 计划或验证证据", "变更摘要", "回滚路径"],
    },
    "bugfix": {
        "label": "Bug 修复",
        "required": [
            "10-standards/劣质代码定义.md",
            "20-processes/本地工具与验证入口.md",
        ],
        "optional": [
            "40-records/postmortems/INDEX.md",
            "40-records/lessons/INDEX.md",
        ],
        "outputs": ["复现步骤", "根因结论", "回归测试或验证证据"],
    },
    "performance": {
        "label": "性能优化",
        "required": [
            "10-standards/非功能性需求标准.md",
            "10-standards/性能效率优化标准.md",
            "30-gates/门禁与护栏.md",
        ],
        "optional": [
            "40-records/postmortems/INDEX.md",
            "40-records/lessons/INDEX.md",
        ],
        "outputs": ["复杂度结论", "benchmark/profile 或指标证据", "性能收益与维护成本权衡"],
    },
    "architecture": {
        "label": "架构变更",
        "required": [
            "10-standards/工程质量标准.md",
            "10-standards/非功能性需求标准.md",
            "10-standards/架构设计原则.md",
            "40-records/adr/INDEX.md",
        ],
        "optional": [
            "40-records/tech-debt/INDEX.md",
            "20-processes/RPI研究计划实施流程.md",
        ],
        "outputs": ["ADR 或 ADR 更新", "边界与依赖说明", "迁移和回滚路径"],
    },
    "review": {
        "label": "代码审查",
        "required": [
            "20-processes/代码评审标准.md",
            "30-gates/门禁与护栏.md",
        ],
        "optional": [
            "40-records/lessons/INDEX.md",
            "50-agent/agent-feedback/INDEX.md",
        ],
        "outputs": ["PASS/WARN/BLOCK finding", "证据", "最小修复建议"],
    },
    "postmortem": {
        "label": "复盘",
        "required": [
            "20-processes/文档治理规则.md",
            "30-gates/门禁与护栏.md",
            "40-records/postmortems/INDEX.md",
        ],
        "optional": [
            "40-records/lessons/INDEX.md",
            "50-agent/agent-feedback/INDEX.md",
        ],
        "outputs": ["根因", "防复发动作", "lesson/gate 转化判断"],
    },
    "governance": {
        "label": "治理包维护",
        "required": [
            "20-processes/文档治理规则.md",
            "30-gates/门禁与护栏.md",
            "50-agent/agent-feedback/INDEX.md",
        ],
        "optional": [
            "40-records/lessons/INDEX.md",
            "40-records/adr/INDEX.md",
        ],
        "outputs": ["索引重建", "strict validate", "health report"],
    },
}


ALIASES = {
    "new-feature": "feature",
    "新功能": "feature",
    "bug": "bugfix",
    "fix": "bugfix",
    "修复": "bugfix",
    "perf": "performance",
    "性能": "performance",
    "arch": "architecture",
    "架构": "architecture",
    "审查": "review",
    "复盘": "postmortem",
    "治理": "governance",
}


def slug_from_code_path(code_path: str) -> str:
    value = code_path.strip().strip("/").replace("\\", "/")
    chars = []
    for char in value:
        if char.isalnum() or "\u4e00" <= char <= "\u9fff":
            chars.append(char)
        else:
            chars.append("-")
    slug = "".join(chars).strip("-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug or "module"


def resolve_task_type(value: str) -> str:
    key = value.strip().lower()
    key = ALIASES.get(key, key)
    if key not in ROUTES:
        allowed = ", ".join(sorted(ROUTES))
        raise SystemExit(f"Unknown task type: {value}. Allowed: {allowed}")
    return key


def doc_entry(root: Path, rel: str, required: bool) -> dict[str, object]:
    path = root / rel
    return {
        "path": rel,
        "required": required,
        "exists": path.exists(),
    }


def module_context_entries(root: Path, code_paths: list[str]) -> list[dict[str, object]]:
    entries: list[dict[str, object]] = []
    for code_path in code_paths:
        rel = Path("00-start-here/module-contexts") / slug_from_code_path(code_path) / "CONTEXT.md"
        path = root / rel
        entries.append(
            {
                "code_path": code_path,
                "path": rel.as_posix(),
                "exists": path.exists(),
            }
        )
    return entries


def build_bundle(project_root: Path, task_type: str, code_paths: list[str]) -> dict[str, object]:
    root = project_root / GOV_ROOT
    if not root.exists():
        raise SystemExit(f"Governance package not found: {root}")
    resolved = resolve_task_type(task_type)
    route = ROUTES[resolved]
    docs = [doc_entry(root, rel, True) for rel in DEFAULT_DOCS]
    docs.extend(doc_entry(root, rel, True) for rel in route["required"])
    docs.extend(doc_entry(root, rel, False) for rel in route["optional"])
    missing_required = [item["path"] for item in docs if item["required"] and not item["exists"]]
    module_contexts = module_context_entries(root, code_paths)
    return {
        "decision": "BLOCK" if missing_required else "PASS",
        "task_type": resolved,
        "label": route["label"],
        "root": str(root),
        "docs": docs,
        "module_contexts": module_contexts,
        "required_outputs": route["outputs"],
        "missing_required": missing_required,
        "non_invasive": "read-only; does not modify files",
    }


def render_markdown(bundle: dict[str, object]) -> str:
    lines = [
        "# Governance Context Bundle",
        "",
        f"- `decision`: {bundle['decision']}",
        f"- `task_type`: {bundle['task_type']}",
        f"- `label`: {bundle['label']}",
        f"- `root`: {bundle['root']}",
        "",
        "## Read These Documents",
        "",
    ]
    for item in bundle["docs"]:
        status = "OK" if item["exists"] else ("MISSING" if item["required"] else "optional-missing")
        required = "required" if item["required"] else "optional"
        lines.append(f"- [{status}] `{item['path']}` ({required})")
    lines.extend(["", "## Module Contexts", ""])
    module_contexts = bundle["module_contexts"]
    if module_contexts:
        for item in module_contexts:
            status = "OK" if item["exists"] else "MISSING"
            lines.append(f"- [{status}] `{item['path']}` for `{item['code_path']}`")
    else:
        lines.append("- none")
    lines.extend(["", "## Required Outputs", ""])
    for item in bundle["required_outputs"]:
        lines.append(f"- {item}")
    missing_required = bundle["missing_required"]
    if missing_required:
        lines.extend(["", "## Missing Required", ""])
        lines.extend(f"- `{item}`" for item in missing_required)
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render a governance context bundle for a task type.")
    parser.add_argument("--project-root", default=".", help="Target project root.")
    parser.add_argument("--task-type", required=True, help="feature, bugfix, performance, architecture, review, postmortem, governance.")
    parser.add_argument("--code-path", action="append", default=[], help="Relevant code path. Repeatable.")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    bundle = build_bundle(Path(args.project_root).resolve(), args.task_type, args.code_path)
    if args.format == "json":
        print(json.dumps(bundle, ensure_ascii=False, indent=2))
    else:
        print(render_markdown(bundle))
    return 1 if bundle["decision"] == "BLOCK" else 0


if __name__ == "__main__":
    raise SystemExit(main())
