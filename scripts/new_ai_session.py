#!/usr/bin/env python3
import sys, os, datetime, re
from pathlib import Path

BASE = Path(__file__).resolve().parents[1] / "docs" / "ai"
SESS_DIR = BASE / "sessions"
TPL = BASE / "templates" / "SESSION_TEMPLATE.md"
INDEX = BASE / "LOG_INDEX.md"

def sanitize(title: str) -> str:
    return re.sub(r'[^a-zA-Z0-9_\-]+', '-', title.strip()).strip('-').lower()

def main():
    title = "session"
    if len(sys.argv) >= 2:
        title = sanitize(' '.join(sys.argv[1:]))
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    existing = sorted(SESS_DIR.glob(f"{today}_session-*_*.md"))
    idx = len(existing) + 1
    session_id = f"{today}_session-{idx:03d}_{title}"
    SESS_DIR.mkdir(parents=True, exist_ok=True)
    content = TPL.read_text(encoding="utf-8")
    content = content.replace("YYYY-MM-DD_session-XXX_title", session_id)
    content = content.replace("YYYY-MM-DD", today)
    session_path = SESS_DIR / f"{session_id}.md"
    session_path.write_text(content, encoding="utf-8")
    print(f"[OK] Created {session_path}")

    rel = session_path.relative_to(BASE)
    line = f"- [{session_id}]({rel.as_posix()})\n"
    INDEX.parent.mkdir(parents=True, exist_ok=True)
    if not INDEX.exists():
        INDEX.write_text("# AI Collaboration Log Index\n\n## Sessions\n", encoding="utf-8")
    idx_content = INDEX.read_text(encoding="utf-8")
    if session_id not in idx_content:
        with INDEX.open("a", encoding="utf-8") as f:
            f.write(line)
        print(f"[OK] Updated {INDEX}")
    else:
        print("[SKIP] Already in index")

if __name__ == "__main__":
    main()
