from music21 import stream, note, instrument, midi, dynamics, articulations, metadata
import json

# Load grouped phrases
with open("output/stage3B_grouped_phrases.json", "r") as f:
    phrases = json.load(f)

# Create a single instrument part (piano)
part = stream.Part()
part.insert(0, instrument.Piano())
part.partName = "Piano"
part.partAbbreviation = "Pno"

current_offset = 0.0

for phrase in phrases:
    if not phrase:
        continue

    phrase_length = len(phrase)

    # Assign dynamic based on phrase length
    if phrase_length <= 5:
        dyn = dynamics.Dynamic('p')
    elif phrase_length <= 12:
        dyn = dynamics.Dynamic('mf')
    else:
        dyn = dynamics.Dynamic('f')

    phrase_stream = stream.Voice()
    phrase_stream.insert(0, dyn)

    phrase_start = phrase[0]['onset']
    phrase_end = phrase[-1]['onset']
    phrase_duration = max(0.01, phrase_end - phrase_start)  # avoid div by zero
    phrase_density = phrase_length / phrase_duration

    # Determine articulation
    if phrase_density > 3.0:
        articulation = articulations.Staccato()
    elif phrase_density < 1.5:
        articulation = articulations.Tenuto()
    else:
        articulation = None

    for i, n in enumerate(phrase):
        m = note.Note(n['midi'])
        m.quarterLength = 0.25
        m.offset = n['onset'] - phrase_start

        # Add accent to first note
        if i == 0:
            accent = articulations.Accent()
            m.expressions.append(accent)

        if articulation:
            m.articulations.append(articulation)

        phrase_stream.insert(m)

    part.insert(current_offset, phrase_stream)

    # Add rest between phrases
    last_note_offset = max(n['onset'] for n in phrase) - phrase_start
    current_offset += last_note_offset + 1.0

# Build score
score = stream.Score()
score.insert(0, part)

# Add metadata
score.metadata = metadata.Metadata()
score.metadata.title = "Stage 3C – Expressive Mapping"
score.metadata.composer = "Anna Troisi"

# Format cleanly for playback (optional)
score.makeMeasures(inPlace=True)

# Export to MIDI (for playback testing)
mf = midi.translate.streamToMidiFile(score)
mf.open("output/stage3C_expressive_score.mid", 'wb')
mf.write()
mf.close()

print("🎧 Expressive MIDI saved: output/stage3C_expressive_score.mid")
