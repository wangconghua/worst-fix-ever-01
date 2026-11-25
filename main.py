#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes one commit-message line for a bug fix that made everything worse
to /output/entry.txt.
"""

import os

ENTRY = "fix: the 500 error is gone \u2014 every page now returns 200 and a blank screen"


def check_is_text(text):
    if not isinstance(text, str):
        raise ValueError("entry must be a string")


def check_not_blank(text):
    if not text.strip():
        raise ValueError("entry must not be blank")


def check_length(text):
    if not 1 <= len(text) <= 100:
        raise ValueError("entry must be 1-100 characters")


def check_single_line(text):
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def check_no_edge_whitespace(text):
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")


def check_commit_style(text):
    if not text.startswith("fix:"):
        raise ValueError("entry must read as a commit message starting with 'fix:'")


def check_no_double_spaces(text):
    if "  " in text:
        raise ValueError("entry must not contain double spaces")


def check_no_self_explaining_words(text):
    lowered = text.lower()
    for word in ("funny", "joke", "haha", "lol", "hilarious"):
        if word in lowered:
            raise ValueError("entry must not explain its own joke")


def check_terminal_punctuation(text):
    if text.endswith((".", "!", "?")):
        raise ValueError("entry is a commit subject line: no terminal punctuation")


def check_fix_backfired(text):
    if "blank screen" not in text or "500" not in text:
        raise ValueError("entry must describe the fix and what it broke")


def check_utf8(text):
    text.encode("utf-8")


def validate(text):
    for check in (
        check_is_text,
        check_not_blank,
        check_length,
        check_single_line,
        check_no_edge_whitespace,
        check_no_double_spaces,
        check_no_self_explaining_words,
        check_terminal_punctuation,
        check_commit_style,
        check_fix_backfired,
        check_utf8,
    ):
        check(text)
    return text


def main():
    entry = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)
    print(f"wrote /output/entry.txt ({len(entry)} characters)")


if __name__ == "__main__":
    main()
