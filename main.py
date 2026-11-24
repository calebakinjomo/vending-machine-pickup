"""Write one vending-machine pickup line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Reads no environment variable except MAKEFUN_OUTPUT_DIR (default /output).
Also prints exactly the line, nothing else.
"""

import os

LINE = (
    "Hey beautiful, I've got forty snacks behind this glass, "
    "and you're the only one I can't dispense."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")

print(LINE)
