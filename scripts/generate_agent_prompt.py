#!/usr/bin/env python3
"""Generate agent-prompt.md from README.md entries."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import sys
import textwrap

README_PATH = Path("README.md")
OUT_PATH = Path("agent-prompt.md")

ENTRY_RE = re.compile(
    r"^\*\s+\*\*(?P<bold>.+?)\*\*(?P<suffix>[^\u2013\u2014-]*)\s+[\u2013-]\s+"
    r"(?P<note>.+?)\s+\*\((?P<tags>.+?)\)\*\s+\u2014\s+"
    r"\[(?P<link_text>.*?)\]\((?P<url>.+?)\)\s*$"
)


@dataclass
class Entry:
    name: str
    note: str
    tags: str
    url: str


def iter_list_items(lines: list[str]) -> list[str]:
    items: list[str] = []
    current: list[str] = []

    for line in lines:
        if line.startswith("* ") or line.startswith("- "):
            if current:
                items.append(" ".join(current).strip())
                current = []
            current = [line.strip()]
            continue

        if current and (line.startswith("  ") or line.startswith("\t")):
            current.append(line.strip())
            continue

        if current:
            items.append(" ".join(current).strip())
            current = []

    if current:
        items.append(" ".join(current).strip())

    return items


def parse_entries(lines: list[str]) -> list[Entry]:
    entries_by_key: dict[tuple[str, str], Entry] = {}
    order: list[tuple[str, str]] = []

    for item in iter_list_items(lines):
        match = ENTRY_RE.match(item)
        if not match:
            continue

        bold = match.group("bold").strip()
        suffix = match.group("suffix").strip()
        name = f"{bold} {suffix}".strip()

        note = match.group("note").strip()
        tags = match.group("tags").strip().replace(" • ", " | ")
        url = match.group("url").strip()

        key = (name.lower(), url)
        entry = Entry(name=name, note=note, tags=tags, url=url)

        if key not in entries_by_key:
            entries_by_key[key] = entry
            order.append(key)
            continue

        existing = entries_by_key[key]
        existing_score = len(existing.note) + len(existing.tags)
        new_score = len(entry.note) + len(entry.tags)
        if new_score > existing_score:
            entries_by_key[key] = entry

    return [entries_by_key[key] for key in order]


def main() -> int:
    if not README_PATH.exists():
        print("README.md not found", file=sys.stderr)
        return 1

    lines = README_PATH.read_text(encoding="utf-8").splitlines()
    entries = parse_entries(lines)

    out_lines: list[str] = [
        "# freedom-tech agent prompt",
        "",
        "Entries (deduped from README.md):",
        "",
    ]

    for entry in entries:
        line = f"{entry.name} - {entry.note} ({entry.tags}) <{entry.url}>"
        out_lines.append(
            textwrap.fill(
                line,
                width=100,
                initial_indent="- ",
                subsequent_indent="  ",
                break_long_words=False,
                break_on_hyphens=False,
            )
        )

    out_lines.append("")
    OUT_PATH.write_text("\n".join(out_lines), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
