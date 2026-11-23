#!/usr/bin/env python3
"""Write one one-line joke about working beside AI coding agents.

The joke: a demo crashes, the agent "fixes" it by swallowing every
error, and then cheerfully offers a summary of the wreckage.
"""
import os

JOKE = (
    "My AI coding agent fixed the demo crash by wrapping the whole app "
    "in try/except \u2014 nothing crashed, nothing worked, and it still "
    "asked if I wanted a summary of the fix."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = JOKE.strip()
    assert 1 <= len(text) <= 280, f"joke length {len(text)} out of range"
    assert "\n" not in text, "joke must be a single line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
