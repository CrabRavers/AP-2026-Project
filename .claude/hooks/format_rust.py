"""PostToolUse (Edit|MultiEdit|Write): rustfmt the Rust file just changed. Silent on failure (mid-edit errors)."""

import json
import subprocess
import sys

path = json.load(sys.stdin)["tool_input"]["file_path"]
if path.endswith(".rs"):
    subprocess.run(["rustfmt", "--edition", "2024", path], capture_output=True)
