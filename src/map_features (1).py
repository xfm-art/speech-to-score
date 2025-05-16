import numpy as np

def clean_pitch(pitch_contour):
    return [float(p) for p in pitch_contour if not np.isnan(p)]

def hz_to_midi(pitches):
    return [int(round(69 + 12 * np.log2(p / 440.0))) for p in pitches if p > 0]

def quantize_onsets(onsets, step=0.25):
    return [round(t / step) * step for t in onsets]
