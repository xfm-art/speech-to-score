import librosa
import numpy as np
import os

def extract_pitch_and_onsets(audio_path):
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")
    
    y, sr = librosa.load(audio_path)
    
    # Extract pitch
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
    pitch_contour = []
    for t in range(pitches.shape[1]):
        index = magnitudes[:, t].argmax()
        pitch = pitches[index, t]
        pitch_contour.append(pitch if pitch > 0 else np.nan)

    # Extract onsets
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    onset_frames = librosa.onset.onset_detect(onset_envelope=onset_env, sr=sr)
    onset_times = librosa.frames_to_time(onset_frames, sr=sr)

    return pitch_contour, onset_times.tolist(), sr
