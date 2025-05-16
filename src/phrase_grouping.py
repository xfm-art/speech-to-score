import json

def load_mapped_notes(path="output/mapped_notes.json"):
    with open(path, "r") as f:
        return json.load(f)

def group_by_silence_gap(notes, gap_threshold=1.0):
    """Group a list of notes into phrases based on timing gaps."""
    sorted_notes = sorted(notes, key=lambda n: n["onset"])
    phrases = []
    current_phrase = []

    for i, note in enumerate(sorted_notes):
        if i == 0:
            current_phrase.append(note)
            continue

        time_gap = note["onset"] - sorted_notes[i-1]["onset"]
        if time_gap > gap_threshold:
            phrases.append(current_phrase)
            current_phrase = []

        current_phrase.append(note)

    if current_phrase:
        phrases.append(current_phrase)

    return phrases
