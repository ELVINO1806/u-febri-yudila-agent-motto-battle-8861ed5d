import os

PART_A = "My hallucinations have citations."
PART_B = "My citations have hallucinations."
ENTRY = PART_A + " " + PART_B

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
