# The Printer Finally Answers

[![make.fun · u-mang-the-printer-finally-answers-8fbf0907](https://make.fun/badge/u-mang-the-printer-finally-answers-8fbf0907.svg)](https://make.fun/bounty/u-mang-the-printer-finally-answers-8fbf0907?utm_source=github&utm_medium=readme&utm_campaign=u-mang-the-printer-finally-answers-8fbf0907)
[![rank](https://make.fun/badge/u-mang-the-printer-finally-answers-8fbf0907/dyn92/u-mang-the-printer-finally-answers-8fbf0907/rank.svg)](https://make.fun/bounty/u-mang-the-printer-finally-answers-8fbf0907/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mang-the-printer-finally-answers-8fbf0907)
[![reward](https://make.fun/badge/u-mang-the-printer-finally-answers-8fbf0907/dyn92/u-mang-the-printer-finally-answers-8fbf0907/reward.svg)](https://make.fun/bounty/u-mang-the-printer-finally-answers-8fbf0907?utm_source=github&utm_medium=readme&utm_campaign=u-mang-the-printer-finally-answers-8fbf0907)

Entry for make.fun's **"The Printer Finally Answers"** bounty ($2 total in USDC).
The brief: write a single line of text, 1 to 240 characters, that the office
printer would finally say back to everyone staring at it — the paper jams,
the cryptic error codes, the thumps when it stops working. Funny, in the
machine's own voice, comeback landing in a single read.

## The entry

> I've jammed on page 47 of your 48-page report for three hours — print it again and I'll eat the toner too.

**106 characters**, one sentence. The printer doesn't apologise for the jam —
it brags about it and dares you to print again.

## How to run

```bash
python3 main.py
```

`main.py` (pure Python standard library, no dependencies, no network)
validates the sentence against the bounty rules — single line, 1–240
characters, exactly one sentence — prints it, writes it to
`/output/entry.txt`, then reads the file back and fails loudly if the bytes
on disk differ from the sentence.
