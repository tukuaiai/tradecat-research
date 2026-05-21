#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path


GOV_ROOT = Path("assets/docs/governance")

RECORD_DIRS = {
    "ADR": Path("40-records/adr"),
    "REVIEW": Path("40-records/reviews"),
    "POSTMORTEM": Path("40-records/postmortems"),
    "LESSON": Path("40-records/lessons"),
    "WO": Path("40-records/workorders"),
    "DEBT": Path("40-records/tech-debt"),
    "QA": Path("40-records/qa-plans"),
    "AF": Path("50-agent/agent-feedback"),
}


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def title_from_markdown(text: str, fallback: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def fallback_id(path: Path, prefix: str) -> str:
    match = re.match(rf"^({re.escape(prefix)}-\d{{4}})", path.stem)
    return match.group(1) if match else path.stem


def record_rows(directory: Path, prefix: str) -> list[tuple[str, str, str, str]]:
    rows = []
    pattern = re.compile(rf"^{re.escape(prefix)}-\d{{4}}.*\.md$")
    if not directory.exists():
        return rows
    for path in sorted(directory.glob(f"{prefix}-*.md")):
        if not pattern.match(path.name):
            continue
        text = path.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        rows.append(
            (
                fm.get("id", fallback_id(path, prefix)),
                title_from_markdown(text, path.stem),
                fm.get("status", "unknown"),
                path.name,
            )
        )
    return rows


def write_record_index(directory: Path, title: str, rows: list[tuple[str, str, str, str]], dry_run: bool) -> Path:
    directory.mkdir(parents=True, exist_ok=True)
    index = directory / "INDEX.md"
    today = date.today().isoformat()
    lines = [
        "---",
        f"id: IDX-{title.upper().replace(' ', '-')}",
        "type: index",
        "status: current",
        "owner: engineering",
        f"last_reviewed: {today}",
        "---",
        "",
        f"# {title}",
        "",
        "| ID | 标题 | 状态 | 文件 |",
        "|---|---|---|---|",
    ]
    for record_id, title_text, status, filename in rows:
        lines.append(f"| `{record_id}` | {title_text} | {status} | `{filename}` |")
    content = "\n".join(lines) + "\n"
    if not dry_run:
        index.write_text(content, encoding="utf-8")
    return index


def write_gate_index(root: Path, dry_run: bool) -> Path:
    directory = root / "30-gates" / "gates"
    rows = []
    for path in sorted(directory.glob("GATE-*.md")) if directory.exists() else []:
        text = path.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        rows.append(
            (
                fm.get("id", fallback_id(path, "GATE")),
                fm.get("severity", "UNKNOWN"),
                title_from_markdown(text, path.stem),
                fm.get("detectability", "manual"),
                fm.get("source", ""),
                fm.get("status", "unknown"),
                path.name,
            )
        )
    index = root / "30-gates" / "GATE-INDEX.md"
    today = date.today().isoformat()
    lines = [
        "---",
        "id: GATE-INDEX",
        "type: gate-index",
        "status: current",
        "owner: engineering",
        f"last_reviewed: {today}",
        "---",
        "",
        "# Gate Index",
        "",
        "| Gate ID | 严重级别 | 标题 | 检测方式 | 来源 | 状态 | 文件 |",
        "|---|---|---|---|---|---|---|",
    ]
    for row in rows:
        lines.append(f"| `{row[0]}` | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | `{row[6]}` |")
    if not dry_run:
        index.parent.mkdir(parents=True, exist_ok=True)
        index.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return index


def write_root_index(root: Path, dry_run: bool) -> Path:
    index = root / "INDEX.md"
    sections = [
        (
            "启动入口",
            [
                ("00-start-here/AGENT-ENTRY.md", True),
                ("00-start-here/CONTEXT-MAP.md", True),
                ("00-start-here/CONTEXT-ROUTER.md", True),
                ("00-start-here/PROJECT-TOPOLOGY.md", True),
            ],
        ),
        (
            "当前标准",
            [
                ("10-standards/工程质量标准.md", True),
                ("10-standards/劣质代码定义.md", True),
                ("10-standards/非功能性需求标准.md", True),
                ("10-standards/优质代码定义.md", False),
                ("10-standards/性能效率优化标准.md", False),
                ("10-standards/可靠性标准.md", False),
                ("10-standards/架构设计原则.md", False),
            ],
        ),
        (
            "流程",
            [
                ("20-processes/代理协作协议.md", True),
                ("20-processes/RPI研究计划实施流程.md", True),
                ("20-processes/QA计划标准.md", True),
                ("20-processes/本地工具与验证入口.md", True),
                ("20-processes/代码评审标准.md", False),
                ("20-processes/文档治理规则.md", False),
            ],
        ),
        ("门禁", [("30-gates/门禁与护栏.md", True), ("30-gates/GATE-INDEX.md", True)]),
        ("记录", [(str(path / "INDEX.md"), prefix in {"ADR", "POSTMORTEM", "LESSON", "QA", "AF"}) for prefix, path in RECORD_DIRS.items()]),
    ]
    lines = [
        "---",
        "id: GOV-INDEX",
        "type: index",
        "status: current",
        "owner: engineering",
        f"last_reviewed: {date.today().isoformat()}",
        "---",
        "",
        "# 治理包索引",
        "",
    ]
    for heading, rels in sections:
        lines.extend([f"## {heading}", ""])
        for rel, required in rels:
            if (root / rel).exists():
                status = "OK"
            elif required:
                status = "REQUIRED-MISSING"
            else:
                status = "optional"
            lines.append(f"- [{status}] `{rel}`")
        lines.append("")
    if not dry_run:
        index.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return index


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Rebuild governance package indexes.")
    parser.add_argument("--project-root", default=".", help="Target project root.")
    parser.add_argument("--dry-run", action="store_true", help="Preview index targets without writing.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.project_root).resolve() / GOV_ROOT
    if not root.exists():
        raise SystemExit(f"Governance package not found: {root}")
    touched = [write_root_index(root, args.dry_run), write_gate_index(root, args.dry_run)]
    for prefix, rel_dir in RECORD_DIRS.items():
        rows = record_rows(root / rel_dir, prefix)
        touched.append(write_record_index(root / rel_dir, f"{prefix} Index", rows, args.dry_run))
    for path in touched:
        print(path)
    print("non_invasive: wrote only inside assets/docs/governance/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
