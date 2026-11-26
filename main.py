"""Out of Tokens, Mid-Sentence: writes one error-message line to /output/entry.txt."""

import os

LINE = (
    "Error 429: token budget exhausted. My last token bought this message "
    "instead of your answer, which was poor prioritiza"
)


def main() -> None:
    # Gate: UTF-8 text of 1 to 140 characters, not only white space.
    assert LINE.strip() and len(LINE) <= 140
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
