"""Stop: warn (never block) when code changed but the task's plan.md / result.md are missing (AGENTS.md steps 3-4)."""

import json
import subprocess
import sys

import plan_dir

event = json.load(sys.stdin)
path = plan_dir.find(event["session_id"])
changed = subprocess.run(
    ["git", "status", "--porcelain", "--", ".", ":!.agents"], capture_output=True, text=True,
    cwd=plan_dir.PLANS.parent.parent,
).stdout.strip()
if path is None or not changed:
    sys.exit(0)  # only discussion so far

missing = [name for name in ("plan.md", "result.md")
           if not (path / name).exists()]
if missing:
    print(json.dumps(
        {"systemMessage": f"AGENTS.md: {path.name} is missing {' and '.join(missing)}."}))
