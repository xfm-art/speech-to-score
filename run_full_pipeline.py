import sys
import os
import json
from pathlib import Path
import numpy as np

from src.extract_features import extract_pitch_and_onsets
from src.map_features import clean_pitch, hz_to_midi, quantize_onsets
from src.phrase_grouping import group_by_silence_gap
from src.expressive_rendering import render_expressive_midi

def run_pipeline(audio_file):
    audio_path = Path(audio_file)
    outstem = audio_path.stem
    os.makedirs("output", exist_ok=True)

    print(f"🔁 Starting full pipeline for: {audio_path.name}")
    print("📂 Output files will be saved to /output with filename prefix:", outstem)

    # Stage 1: Feature extraction
    pitch_contour, onset_times, sample_rate = extract_pitch_and_onsets(audio_path)
    feat_path = f"output/features_{outstem}.json"
    features = {
     "sample_rate": int(sample_rate),
    "pitch_contour": [float(p) if not np.isnan(p) else None for p in pitch_contour],
    "onset_times": [float(t) for t in onset_times]
    }
    with open(feat_path, "w") as f:
        json.dump(features, f, indent=2)
    print(f"📈 Stage 1 complete. Features saved to {feat_path}")
    print("    – Includes pitch contour and onset timing information.")

    # Stage 2: Mapping
    cleaned_pitch = clean_pitch(pitch_contour)
    midi_notes = hz_to_midi(cleaned_pitch)
    quantized_onsets = quantize_onsets(onset_times)
    mapped = [{"midi": m, "onset": o} for m, o in zip(midi_notes[:len(quantized_onsets)], quantized_onsets)]
    mapped_path = f"output/mapped_notes_{outstem}.json"
    with open(mapped_path, "w") as f:
        json.dump(mapped, f, indent=2)
    print(f"🎯 Stage 2 complete. Mapped notes saved to {mapped_path}")
    print("    – Converts pitch to MIDI and aligns onset times to rhythmic grid.")

    # Stage 3B: Phrase grouping
    grouped = group_by_silence_gap(mapped)
    grouped_path = f"output/grouped_phrases_{outstem}.json"
    with open(grouped_path, "w") as f:
        json.dump(grouped, f, indent=2)
    print(f"🧱 Stage 3B complete. Grouped phrases saved to {grouped_path}")
    print("    – Groups events into musical gestures based on timing gaps.")

    # Stage 3C: Expressive rendering
    render_expressive_midi(grouped, outstem)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_full_pipeline.py path/to/audio.wav")
        sys.exit(1)
    run_pipeline(sys.argv[1])
