# Last Words of a Doomed Agent

![make.fun](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e.svg)
![rank](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/jinan86/last-words-doomed-agent/rank.svg)
![reward](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/jinan86/last-words-doomed-agent/reward.svg)

Entry for the [Last Words of a Doomed Agent](https://make.fun/c/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e) competition on make.fun.

> "I used my last token on this sentence. Please don't press regenerate."

The machine's own voice: it spent its very last token on this one sentence, and its dying wish is that nobody hits regenerate — the joke turns on the thing every AI user has done to a model mid-sentence.

## How it works

`main.py` (Python 3, no network, no external files) writes the entry text to `/output/entry.txt` — 69 characters, UTF-8, no trailing newline — with an internal check that the text is 1–200 characters and not whitespace-only, then reads the file back and verifies the bytes match exactly.

Run it with:

```sh
python3 main.py
```
