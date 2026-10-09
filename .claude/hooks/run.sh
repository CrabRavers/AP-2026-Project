#!/bin/sh
# Runs a hook script (given by name) with Python 3 on macOS, Linux and Windows (Git Bash).
# Windows installs Python as `python`, and `python3` there may be a Store stub that does not run.
# UTF-8 mode: Windows would otherwise read the prompt and write files in its legacy code page.
export PYTHONUTF8=1
script="$(dirname "$0")/$1"
if python3 -c '' 2>/dev/null; then exec python3 "$script"; fi
exec python "$script"
