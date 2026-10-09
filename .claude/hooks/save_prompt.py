"""UserPromptSubmit: save the user's prompt verbatim (AGENTS.md steps 1-2, AI policy prompt declaration).

The first prompt of a session opens a new plan directory as initial-prompt.md;
later prompts are appended to follow-up-prompts.md. One session = one task.
"""

import json
import sys

import plan_dir

event = json.load(sys.stdin)
path = plan_dir.find(event["session_id"])
if path is None:
    path = plan_dir.create(event["session_id"])
    (path / "initial-prompt.md").write_text(event["prompt"] + "\n")
else:
    with open(path / "follow-up-prompts.md", "a") as log:
        log.write(event["prompt"] + "\n\n---\n\n")

# Printed text is added to Claude's context.
print(
    f"AGENTS.md plan directory for this task: {path}. The prompt is already saved there. "
    "Write plan.md before writing code and result.md after implementing."
)
