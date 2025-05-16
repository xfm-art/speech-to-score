from music21 import stream, note, instrument, midi, dynamics, articulations, metadata

def render_expressive_midi(phrases, outstem):
    part = stream.Part()
    part.insert(0, instrument.Piano())
    part.partName = "Piano"
    part.partAbbreviation = "Pno"
    current_offset = 0.0

    for phrase in phrases:
        if not phrase:
            continue

        phrase_length = len(phrase)
        dyn = dynamics.Dynamic('p') if phrase_length <= 5 else dynamics.Dynamic('mf') if phrase_length <= 12 else dynamics.Dynamic('f')
        velocity = 50 if dyn.value == 'p' else 80 if dyn.value == 'mf' else 110

        phrase_stream = stream.Voice()
        phrase_stream.insert(0, dyn)

        phrase_start = phrase[0]['onset']
        phrase_end = phrase[-1]['onset']
        phrase_duration = max(0.01, phrase_end - phrase_start)
        phrase_density = phrase_length / phrase_duration
        articulation = articulations.Staccato() if phrase_density > 3.0 else articulations.Tenuto() if phrase_density < 1.5 else None

        for i, n in enumerate(phrase):
            m = note.Note(n['midi'])
            m.quarterLength = 0.5 if phrase_density < 1.5 else 0.2 if phrase_density > 3.0 else 0.33
            m.offset = n['onset'] - phrase_start
            m.volume.velocity = velocity
            if i == 0:
                m.expressions.append(articulations.Accent())
            if articulation:
                m.articulations.append(articulation)
            phrase_stream.insert(m)

        part.insert(current_offset, phrase_stream)
        last_note_offset = max(n['onset'] for n in phrase) - phrase_start
        current_offset += last_note_offset + 1.0

    score = stream.Score()
    score.insert(0, part)
    score.metadata = metadata.Metadata()
    score.metadata.title = f"{outstem} – Expressive Mapping"
    score.metadata.composer = "Anna Troisi"
    score.makeMeasures(inPlace=True)

    midipath = f"output/{outstem}_expressive_score.mid"
    mf = midi.translate.streamToMidiFile(score)
    mf.open(midipath, 'wb')
    mf.write()
    mf.close()
    print(f"✅ Expressive MIDI saved: {midipath}")
