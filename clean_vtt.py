import re

input_file = "Elon Musk： A Different Conversation w⧸ Nikhil Kamath ｜ Full Episode ｜ People by WTF Ep. 16 [Rni7Fz7208c].en.vtt"
output_file = "transcript.txt"

cleaned = []

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

current_timestamp = None

for line in lines:
    line = line.strip()

    # Capture timestamps
    if "-->" in line:
        current_timestamp = line.split(" --> ")[0]
        continue

    # Skip metadata
    if (
        not line
        or line.startswith("WEBVTT")
        or line.startswith("Kind:")
        or line.startswith("Language:")
    ):
        continue

    # Remove HTML tags
    line = re.sub(r"<[^>]+>", "", line)

    if current_timestamp and len(line) > 2:
        cleaned.append(f"[{current_timestamp}] {line}")

with open(output_file, "w", encoding="utf-8") as f:
    for item in cleaned:
        f.write(item + "\n")

print("Transcript cleaned successfully!")