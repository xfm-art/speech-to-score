def group_by_silence_gap(notes, threshold=1.0):
    notes.sort(key=lambda x: x['onset'])
    phrases = []
    current_phrase = []
    last_onset = None
    for n in notes:
        if last_onset is not None and (n['onset'] - last_onset) > threshold:
            if current_phrase:
                phrases.append(current_phrase)
                current_phrase = []
        current_phrase.append(n)
        last_onset = n['onset']
    if current_phrase:
        phrases.append(current_phrase)
    return phrases
