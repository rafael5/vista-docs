"""
Pure YAML frontmatter rewriter.

rewrite_frontmatter(md, new_fields) → updated markdown string.
No I/O. Takes a markdown string, returns a markdown string.
"""

from __future__ import annotations

import re

_FRONTMATTER_RE = re.compile(r"^(---\n)(.*?)(---\n)", re.DOTALL)


def _quote(value: str) -> str:
    """Double-quote a YAML string value if it contains a colon."""
    if ":" in value:
        return '"' + value.replace('"', '\\"') + '"'
    return value


def _serialize_value(value: object) -> str:
    """Serialize a Python value to a YAML scalar or block."""
    if isinstance(value, list):
        if not value:
            return "[]"
        items = "\n".join(f"  - {v}" for v in value)
        return "\n" + items
    if isinstance(value, int):
        return str(value)
    if isinstance(value, str):
        return _quote(value) if ":" in value else value
    return str(value)


def parse_frontmatter(md: str) -> dict:
    """
    Extract the YAML frontmatter from a markdown string as a dict.

    Only handles simple key: value pairs and list blocks (- item).
    Returns empty dict if no frontmatter found.
    """
    m = _FRONTMATTER_RE.match(md)
    if not m:
        return {}

    result: dict = {}
    yaml_block = m.group(2)
    current_key: str | None = None
    current_list: list | None = None

    for line in yaml_block.splitlines():
        if line.startswith("  - "):
            if current_key and current_list is not None:
                current_list.append(line[4:].strip())
        elif ": " in line or line.endswith(":"):
            if current_key and current_list is not None:
                result[current_key] = current_list
            parts = line.split(": ", 1)
            current_key = parts[0].strip().rstrip(":")
            if len(parts) == 1 or parts[1].strip() == "":
                current_list = []
                result[current_key] = current_list
            else:
                val = parts[1].strip().strip('"')
                result[current_key] = val
                current_list = None
        elif line.strip() == "":
            continue

    if current_key and current_list is not None:
        result[current_key] = current_list

    return result


def rewrite_frontmatter(md: str, new_fields: dict) -> str:
    """
    Merge new_fields into the existing YAML frontmatter and return updated markdown.

    Existing fields are preserved; new_fields are appended or overwrite matching keys.
    If no frontmatter exists, a new block is created.
    """
    m = _FRONTMATTER_RE.match(md)
    if m:
        existing_yaml = m.group(2)
        body_after = md[m.end() :]
    else:
        existing_yaml = ""
        body_after = md

    # Parse existing fields preserving order
    existing_lines = existing_yaml.splitlines()
    existing_keys: list[str] = []
    seen: set[str] = set()
    for line in existing_lines:
        if ": " in line and not line.startswith(" "):
            key = line.split(": ", 1)[0].strip()
            if key not in seen:
                existing_keys.append(key)
                seen.add(key)

    # Build merged YAML: existing first, then new fields not already present
    yaml_lines = list(existing_lines)

    for key, value in new_fields.items():
        serialized = _serialize_value(value)
        new_line = f"{key}: {serialized}"
        if key in seen:
            # Overwrite existing — find and replace the block
            new_yaml_lines = []
            skip_list = False
            for line in yaml_lines:
                if line.startswith(f"{key}: ") or line == f"{key}:":
                    new_yaml_lines.append(new_line)
                    skip_list = isinstance(value, list)
                elif skip_list and line.startswith("  - "):
                    continue
                else:
                    skip_list = False
                    new_yaml_lines.append(line)
            yaml_lines = new_yaml_lines
        else:
            yaml_lines.append(new_line)
            seen.add(key)

    new_yaml = "\n".join(yaml_lines)
    if new_yaml and not new_yaml.endswith("\n"):
        new_yaml += "\n"

    return f"---\n{new_yaml}---\n{body_after}"
