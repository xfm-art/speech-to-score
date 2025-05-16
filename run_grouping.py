from src.phrase_grouping import load_mapped_notes, group_by_silence_gap

notes = load_mapped_notes()
phrases = group_by_silence_gap(notes, gap_threshold=1.0)

print(f"🧩 Total phrases found: {len(phrases)}\n")

for i, phrase in enumerate(phrases[:5]):
    print(f"Phrase {i + 1} ({len(phrase)} notes):")
    for note in phrase:
        print(f"  MIDI: {note['midi']}, Onset: {note['onset']}")
    print()
    
import json
import os

# Save phrases to a JSON file
os.makedirs("output", exist_ok=True)

with open("output/stage3B_grouped_phrases.json", "w") as f:
    json.dump(phrases, f, indent=2)

print("📁 Grouped phrases saved to output/stage3B_grouped_phrases.json")