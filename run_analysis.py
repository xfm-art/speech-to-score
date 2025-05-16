# --------------------------------------------
# Imports
# --------------------------------------------
from src.extract_features import extract_pitch_and_onsets, plot_pitch
from math import isnan
import json

# --------------------------------------------
# File Input
# --------------------------------------------
# Set the path to the audio file you want to analyze.
# The file should be located in the /data folder.
audio_path = "data/sample_speech.wav"

# --------------------------------------------
# Feature Extraction
# --------------------------------------------
# Extracts the pitch contour, onset times (in seconds),
# and the audio sample rate from the speech file.
pitch_contour, onset_times, sample_rate = extract_pitch_and_onsets(audio_path)

# --------------------------------------------
# Console Output for Diagnostics
# --------------------------------------------
# Print sample rate and the number of valid (non-NaN) pitch values.
# Also print the onset times to inspect the rhythmic structure.
print(f"Sample rate: {sample_rate}")
print(f"Pitch values: {len([p for p in pitch_contour if not isnan(p)])}")
print(f"Onset times (in seconds): {onset_times}")

# --------------------------------------------
# Optional: Save a Visual Plot of the Pitch Contour
# --------------------------------------------
# This will generate a PNG file showing how the pitch evolves over time.
# Comment this out if you only want the raw numbers.
plot_pitch(pitch_contour, output_file="pitch_contour.png")

# --------------------------------------------
# Save Extracted Features to a JSON File
# --------------------------------------------
import os
os.makedirs("output", exist_ok=True)  # Ensure the folder exists

# Replace NaN values with None for JSON compatibility
data = {
    "sample_rate": int(sample_rate),
    "pitch_contour": [float(p) if not isnan(p) else None for p in pitch_contour],
    "onset_times": [float(t) for t in onset_times]
}

# Write the features to a file
with open("output/features.json", "w") as f:
    json.dump(data, f, indent=2)

print("Features saved to output/features.json")
