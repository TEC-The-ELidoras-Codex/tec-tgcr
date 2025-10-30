#!/usr/bin/env python3
"""Parse brain_dump/gpt103025 and extract user 'You said' blocks into anonymized assets.

Outputs:
- assets/tec_tcgr_samples.json (array of records)
- assets/tec_tcgr_samples.csv  (CSV with headers)

Conservative defaults: composite_gender='non-disclosed', age_range='non-disclosed', status='unverified'
"""
import re
import os
import json
import csv
import uuid
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(__file__))
BRAIN = os.path.join(ROOT, 'brain_dump', 'gpt103025')
OUT_DIR = os.path.join(ROOT, 'assets')
JSON_OUT = os.path.join(OUT_DIR, 'tec_tcgr_samples.json')
CSV_OUT = os.path.join(OUT_DIR, 'tec_tcgr_samples.csv')


def read_brain():
    with open(BRAIN, 'r', encoding='utf-8', errors='replace') as f:
        return f.read()


def extract_you_said_blocks(text):
    # Match sections that start with 'You said:' (or variants) and capture until the next marker
    pattern = re.compile(r"(?s)(?:^|\n)(?:You said:|You asked:|You wrote:)\s*(.*?)\s*(?=(?:\n(?:You said:|ChatGPT said:|You asked:|You wrote:)|\Z))")
    matches = pattern.findall(text)
    return [m.strip() for m in matches if m.strip()]


def build_records(blocks, source_mtime=None):
    records = []
    for blk in blocks:
        rec = {
            'id': str(uuid.uuid4()),
            'date': source_mtime or datetime.utcnow().isoformat() + 'Z',
            'composite_gender': 'non-disclosed',
            'age_range': 'non-disclosed',
            'status': 'unverified',
            'raw_text': blk
        }
        records.append(rec)
    return records


def write_outputs(records):
    os.makedirs(OUT_DIR, exist_ok=True)
    # JSON
    with open(JSON_OUT, 'w', encoding='utf-8') as jf:
        json.dump(records, jf, ensure_ascii=False, indent=2)
    # CSV
    with open(CSV_OUT, 'w', encoding='utf-8', newline='') as cf:
        writer = csv.DictWriter(cf, fieldnames=['id','date','composite_gender','age_range','status','raw_text'])
        writer.writeheader()
        for r in records:
            writer.writerow(r)


def main():
    if not os.path.exists(BRAIN):
        print('Brain dump file not found:', BRAIN)
        return 1
    st = os.stat(BRAIN)
    mtime = datetime.utcfromtimestamp(st.st_mtime).isoformat() + 'Z'
    text = read_brain()
    blocks = extract_you_said_blocks(text)
    print(f'Found {len(blocks)} user blocks (You said / You asked / You wrote)')
    records = build_records(blocks, source_mtime=mtime)
    write_outputs(records)
    print('Wrote', JSON_OUT, 'and', CSV_OUT)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
#!/usr/bin/env python3
"""Parse brain_dump/gpt103025 into TEC_TCGR sample JSON and CSV records.

Creates:
- assets/tec_tcgr_samples.json
- assets/tec_tcgr_samples.csv

This script is idempotent and safe to run multiple times.
"""
import re
import json
import csv
import uuid
from datetime import date

SRC = "brain_dump/gpt103025"
IN = SRC
OUT_JSON = "assets/tec_tcgr_samples.json"
OUT_CSV = "assets/tec_tcgr_samples.csv"

def detect_offensive(text):
    # crude list of tokens that likely indicate offensive language
    toks = ["crackhead", "crackheads", "junkie", "addict", "fuck", "shit"]
    t = text.lower()
    return any(tok in t for tok in toks)

def detect_owner_narrative(text):
    t = text
    if "kaznak" in t.lower():
        return True
    if re.search(r"i\W*'?m\W*a\W*addict", t.lower()):
        return True
    if "i made my own word" in t.lower():
        return True
    return False

def parse(content):
    # Split on 'You said:' blocks, capturing user and assistant
    pattern = re.compile(r"You said:\n(.*?)\nChatGPT said:\n(.*?)(?=\nYou said:|\Z)", re.S)
    matches = pattern.findall(content)
    records = []
    for i, (user_text, assistant_text) in enumerate(matches, start=1):
        uid = str(uuid.uuid4())
        raw_text = user_text.strip()
        assistant = assistant_text.strip()
        combined_raw = "USER:\n" + raw_text + "\n\nASSISTANT:\n" + assistant
        offensive = detect_offensive(raw_text) or detect_offensive(assistant)
        owner_flag = detect_owner_narrative(raw_text) or detect_owner_narrative(assistant)
        # guess composite status
        status = "non-disclosed"
        if re.search(r"addict|junkie|substance use|drug", raw_text, re.I):
            status = "status:past_substance_use"
        rec = {
            "id": uid,
            "source_file": SRC,
            "date_collected": date.today().isoformat(),
            "speaker_id": f"speaker_{i:03d}",
            "raw_text": combined_raw,
            "sanitized_text": "",
            "offensive_language_flag": offensive,
            "offensive_intent": "reclaimed" if owner_flag else "unknown",
            "owner_narrative_flag": owner_flag,
            "composite_gender": "non-disclosed",
            "composite_age_range": "non-disclosed",
            "composite_status": status,
            "notes": "Auto-parsed record. Manual review recommended before publication."
        }
        records.append(rec)
    return records

def main():
    with open(IN, "r", encoding="utf-8") as f:
        content = f.read()
    records = parse(content)
    # write JSON
    with open(OUT_JSON, "w", encoding="utf-8") as j:
        json.dump(records, j, ensure_ascii=False, indent=2)
    # write CSV header
    fieldnames = [
        "id","source_file","date_collected","speaker_id",
        "composite_gender","composite_age_range","composite_status",
        "offensive_language_flag","owner_narrative_flag","raw_text","notes"
    ]
    with open(OUT_CSV, "w", encoding="utf-8", newline="") as c:
        writer = csv.DictWriter(c, fieldnames=fieldnames)
        writer.writeheader()
        for r in records:
            writer.writerow({k: r.get(k, "") for k in fieldnames})
    print(f"Wrote {len(records)} records to {OUT_JSON} and {OUT_CSV}")

if __name__ == "__main__":
    main()
