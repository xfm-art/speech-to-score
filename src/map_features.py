import json
import numpy as np

def load_features(path="output/features.json"):
    with open(path, "r") as f:
        data = json.load(f)
    
    pitch_contour = data["pitch_contour"]
    onset_times = data["onset_times"]
    sample_rate = data["sample_rate"]
    
    return pitch_contour, onset_times, sample_rate


def clean_pitch(pitch_contour):
    return [float(p) for p in pitch_contour if p is not None]

def hz_to_midi(pitches, base_note=60):
    """Map pitch in Hz to MIDI numbers centered around a base note."""
    midi_notes = []
    for hz in pitches:
        if hz > 0:
            midi = 69 + 12 * np.log2(hz / 440.0)
            midi_notes.append(int(round(midi)))
    return midi_notes

def quantize_onsets(onsets, step=0.25):
    """Quantize onsets (in seconds) to a rhythmic grid, e.g. 0.25 sec ~ 1/16 note."""
    return [round(t / step) * step for t in onsets]