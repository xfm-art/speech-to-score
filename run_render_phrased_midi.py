from music21 import stream, note, instrument, midi

import json

# Load phrases
with open("output/stage3B_grouped_phrases.json", "r") as f:
    phrases = json.load(f)

# Create a part
part = stream.Part()
part.insert(0, instrument.Piano())

# Initial offset
current_offset = 0.0

for i, phrase in enumerate(phrases):
    if not phrase:
        continue

    # Sort phrase by onset (in case it's unordered)
    phrase = sorted(phrase, key=lambda n: n["onset"])
    phrase_start = phrase[0]["onset"]

    for j, n in enumerate(phrase):
        m = note.Note(n["midi"])

        # Optional: duration = time to next onset or default
        if j < len(phrase) - 1:
            next_onset = phrase[j + 1]["onset"]
            duration = max(0.25, next_onset - n["onset"])
        else:
            duration = 0.5  # Last note in phrase

        m.quarterLength = duration
        m.offset = current_offset + (n["onset"] - phrase_start)
        part.append(m)

    # Add a rest between phrases
    if i < len(phrases) - 1:
        next_phrase_start = phrases[i + 1][0]["onset"]
        gap = next_phrase_start - phrase[-1]["onset"]
        r = note.Rest()
        r.quarterLength = max(0.5, gap)
        r.offset = part.highestOffset + 0.01
        part.append(r)

    current_offset = part.highestOffset + 0.01

# Score and export
score = stream.Score()
score.insert(0, part)

mf = midi.translate.streamToMidiFile(score)
mf.open("output/stage3B_phrased_score.mid", "wb")
mf.write()
mf.close()

print("🎧 MIDI with real rests saved: output/stage3B_phrased_score.mid")
