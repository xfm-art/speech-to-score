---
title: "Stage 2: Feature Mapping and Pre-Compositional Structuring"
author: "Anna Troisi"
date: 2025-05-15
description: "Mapping speech-derived pitch and onset features into symbolic musical structures for generative composition."
tags: [speech-to-score, feature mapping, midi, rhythm quantization, algorithmic composition]
---

This document describes the second stage in the speech-to-score pipeline. It builds upon the extracted pitch and onset features to create structured musical materials suitable for further compositional development. The goal of this stage is to transform raw speech-derived data into normalized and quantized musical values that can be assigned to instruments, rendered symbolically, or further manipulated algorithmically.

🎯 Objective

To convert speech-derived pitch and onset data into musically meaningful representations:

- MIDI note values (transformed from pitch in Hz)
- Quantized onset times (aligned to rhythmic grids)

🧰 Tools and Environment

- Python 3.9+
- numpy
- json
- Manual implementation of pitch-to-MIDI mapping and temporal quantization

The output from Stage 1 (features.json) is used as input for this mapping process.

📥 Input Format

Input file: output/features.json

Format: includes pitch_contour, onset_times, and sample_rate

Example structure:

```{
  "sample_rate": 22050,
  "pitch_contour": [300.5, 310.2, null, 280.1, ...],
  "onset_times": [0.12, 0.34, 0.56, ...]
}```

🔁 Mapping Process

Pitch Mapping: Hz to MIDI

- Input pitch values (Hz) are filtered to remove nulls
- Each valid frequency is converted to a MIDI pitch number using:

```midi = 69 + 12 * log2(hz / 440.0)```

- Values are rounded to the nearest integer

Onset Quantization

- Onset times (seconds) are mapped to a fixed rhythmic grid
- Example: rounding to the nearest 0.25 seconds (approx. 16th-note grid)

💾 Output Format

The mapped data is saved as a list of pitch-time pairs in output/mapped_notes.json:

```[
  { "midi": 91, "onset": 0.0 },
  { "midi": 89, "onset": 0.25 },
  ...
]```

Each object represents a musical event.

📈 Optional: Printing for Debugging

MIDI values and quantized onsets are printed to the console for inspection:
python```
print(f"MIDI Notes: {midi_notes[:10]}")
print(f"Quantized Onsets: {quantized_onsets[:10]}")
```

🔁 Reproducibility Notes

Python version used: 3.9.12

Key functions implemented manually:

hz_to_midi()

quantize_onsets()

Run using:

python3 run_mapping.py

Output: output/mapped_notes.json

🧭 Next Steps

In Stage 3, these mapped musical primitives will be assigned to instruments, structured into multi-part score data, and optionally rendered via symbolic notation tools such as music21.
