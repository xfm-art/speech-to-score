from music21 import stream, note, midi, instrument
import json

# Load flat list of notes from Stage 2
with open("output/mapped_notes.json", "r") as f:
    note_data = json.load(f)

# Create a single instrument part (e.g. flute)
part = stream.Part()
part.insert(0, instrument.Flute())  # You can change this to Viola(), Oboe(), etc.

for n in note_data:
    m = note.Note(n["midi"])
    m.quarterLength = 0.25  # fixed duration for simplicity
    m.offset = n["onset"]
    part.append(m)

# Assemble the score
score = stream.Score()
score.insert(0, part)

# Save as MIDI
mf = midi.translate.streamToMidiFile(score)
mf.open("output/stage2_flat_playback.mid", "wb")
mf.write()
mf.close()

print("🎧 MIDI file saved to output/stage2_flat_playback.mid")
