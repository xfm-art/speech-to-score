from src.map_features import load_features, clean_pitch, hz_to_midi, quantize_onsets
print("✅ run_mapping.py has started")
# Load raw features
pitch_contour, onset_times, sr = load_features()

# Clean and map pitch
cleaned_pitch = clean_pitch(pitch_contour)
midi_notes = hz_to_midi(cleaned_pitch)

# Quantize rhythm
quantized_onsets = quantize_onsets(onset_times, step=0.25)

# Output to console
print(f"MIDI Notes: {midi_notes[:10]}")
print(f"Quantized Onsets: {quantized_onsets[:10]}")

import os
import json

# Combine pitch and rhythm into note events
note_events = [{"midi": midi, "onset": onset} for midi, onset in zip(midi_notes, quantized_onsets)]

# Make sure output folder exists
os.makedirs("output", exist_ok=True)

# Save the data
with open("output/mapped_notes.json", "w") as f:
    json.dump(note_events, f, indent=2)

print("✅ Mapped notes saved to output/mapped_notes.json")

print(f"Length of MIDI Notes: {len(midi_notes)}")
print(f"Length of Quantized Onsets: {len(quantized_onsets)}")

