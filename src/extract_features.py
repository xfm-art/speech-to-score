# --------------------------------------------
# Imports
# --------------------------------------------

import librosa                          # Library for audio analysis and feature extraction
import numpy as np                      # Numerical computing, especially for handling NaN
import matplotlib.pyplot as plt         # For plotting the pitch contour
import os                               # For file path and existence checks

# --------------------------------------------
# Feature Extraction Function
# --------------------------------------------

def extract_pitch_and_onsets(audio_path):
    """
    Load a speech audio file and extract pitch contour and onset times.

    Args:
        audio_path (str): Path to the input audio file (.wav format recommended)

    Returns:
        pitch_contour (list of float or NaN): Fundamental frequency in Hz for each frame.
                                              NaN values represent silence or unvoiced frames.
        onsets (list of float): Times (in seconds) where rhythmic onsets occur.
        sr (int): Sample rate of the loaded audio file.
    """
    
    # Check if file exists
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")
    
    # Load the audio file using librosa's default settings
    y, sr = librosa.load(audio_path)

    # ----------------------------------------------------
    # Pitch Tracking
    # ----------------------------------------------------
    # Use probabilistic pitch tracking to get pitch + magnitude per time frame
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
    pitch_contour = []

    # For each time frame, extract the pitch with the highest energy
    for t in range(pitches.shape[1]):
        index = magnitudes[:, t].argmax()
        pitch = pitches[index, t]
        pitch_contour.append(pitch if pitch > 0 else np.nan)  # use NaN for silence

    # ----------------------------------------------------
    # Onset Detection
    # ----------------------------------------------------
    # Compute onset strength envelope and detect peaks
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    onset_frames = librosa.onset.onset_detect(onset_envelope=onset_env, sr=sr)
    
    # Convert detected frames into real time (seconds)
    onset_times = librosa.frames_to_time(onset_frames, sr=sr)

    return pitch_contour, onset_times.tolist(), sr

# --------------------------------------------
# Plotting Function
# --------------------------------------------

def plot_pitch(pitch_contour, output_file="pitch_contour.png"):
    """
    Visualize the pitch contour and save it as an image file.

    Args:
        pitch_contour (list of float or Na_N): Fundamental frequency in Hz for each time frame.
    onsets (list of float): Onset times in seconds.
    sr (int): Sample rate of the audio file.
"""
