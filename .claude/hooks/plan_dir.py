"""Shared helper: the AGENTS.md plan directory that belongs to a Claude session."""

import os
import re
from datetime import date
from pathlib import Path

PLANS = Path(os.environ.get("CLAUDE_PROJECT_DIR", ".")) / ".agents" / "plans"


def find(session_id):
    """Return the plan directory created for this session, or None."""
    for marker in PLANS.glob("plan-*/.session"):
        if marker.read_text().strip() == session_id:
            return marker.parent
    return None


def create(session_id):
    """Create plan-<today>-<NNN> with NNN one above the highest existing number."""
    numbers = [int(m.group(1)) for d in PLANS.glob("plan-*")
               if (m := re.search(r"-(\d{3})$", d.name))]
    path = PLANS / \
        f"plan-{date.today().isoformat()}-{max(numbers, default=0) + 1:03d}"
    path.mkdir(parents=True)
    (path / ".session").write_text(session_id)
    return path
