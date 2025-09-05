# Vocab Pipeline — **single file**

Generate **definitions + examples** with your local **LM Studio (Gemma 12B)**, export **JSON/Anki**, make **TTS**, mix **BGM**, and compress to **MP3** — all from one script: `vocab_pipeline.py`.

---

## Prereqs

* **LM Studio** → Developer → **Start Local Server** (default `http://localhost:1234/v1`)
* For audio: **ffmpeg** (`brew install ffmpeg`)

## Install

```bash
# Core
pip install "openai>=1.40.0"

# TTS (only if you use --make-tts)
pip install "TTS>=0.22.0" "torch>=2.1.0" "torchaudio>=2.1.0"

# Mixing/MP3 (only if you use --mix-bgm or --to-mp3)
pip install "pydub>=0.25.1" "simpleaudio>=1.0.4"
```

## Quick start

```bash
# JSON only (from .txt; skip 2 header lines)
python3 vocab_pipeline.py words.txt --skip-header-lines 2 --out-json word_info.json

# JSON + Anki TSV (from CSV with 'Words' column)
python3 vocab_pipeline.py word_list.csv --out-json word_info.json --anki-tsv anki.tsv

# Full: TTS → mix BGM → MP3 (then delete WAV)
python3 vocab_pipeline.py words.txt \
  --out-json word_info.json \
  --make-tts --speaker-wav charlie.wav --tts-out vocab.wav \
  --mix-bgm --bgm-path music.mp3 --mixed-out vocab_mix.wav \
  --to-mp3 --mp3-bitrate 160k --rm-wav
```

## Key flags (most used)

* Input: `.txt` (one word/line) or `.csv` (`--csv-column`, default `Words`)
* Model/server: `--model gemma-2-12b-it`, `--base-url`, `--temperature 0.2`, `--max-tokens 350`
* Outputs: `--out-json`, `--anki-tsv`
* TTS: `--make-tts`, `--speaker-wav`, `--tts-out`
* BGM: `--mix-bgm`, `--bgm-path`, `--mixed-out`, `--bgm-gain-db -18`, `--bgm-fade-ms 800`
* MP3: `--to-mp3`, `--mp3-out`, `--mp3-bitrate 128k`, `--rm-wav`

## Anki (1-liner)

Import `anki.tsv` → map **Field 1 → Front**, **Field 2 → Back (HTML)** → tick **Update existing notes**.
