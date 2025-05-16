---
title: "Stage 1: Feature Extraction"
author: "Anna Troisi"
date: 2025-05-15
description: "Extracting pitch and onset features from speech audio to support musical composition."
tags: [speech-to-score, feature extraction, python, librosa, methodology]
---

## Stage 1: Feature Extraction from Speech

This document outlines the methodology and implementation details for Stage 1 of the *speech-to-score* project, which aims to transform speech recordings into data structures that can inform musical composition. This step involves extracting pitch contours and onset times from a speech audio file, and saving those features in a structured format for further creative processing.

---

## 🎯 Objective

To extract low-level audio features from a spoken `.wav` file:
**Pitch contour** (the melodic shape of speech)
**Onset times** (timing of syllables or stressed phonemes)

These features serve as the basis for later stages of musical mapping and symbolic composition.

---

## 🧰 Tools and Environment

- Python 3.9+
- [`librosa`](https://librosa.org/) (v0.11+)
- `numpy`
- `matplotlib` (optional, for visualization)

**Project structure:**
speech-to-score/
├── data/ # contains input .wav file
├── output/ # will contain extracted features in JSON
├── src/
│ └── extract_features.py
├── run_analysis.py # main script to run Stage 1
└── requirements.txt # dependencies

---

## 📥 Input Format

- Audio file: `.wav` format
- Requirements: monophonic speech, 16kHz or 44.1kHz preferred

Example path: `data/sample_speech.wav`

---

## ⚙️ Feature Extraction Pipeline

### `extract_pitch_and_onsets(audio_path)`

Extracts:

- `pitch_contour`: a list of fundamental frequency values (in Hz) over time
- `onset_times`: a list of detected rhythmic attacks (in seconds)
- `sample_rate`: the original sample rate of the audio file

#### Pitch Extraction

- Method: `librosa.piptrack()`
- We select the pitch with the highest magnitude per frame.
- Frames with no voiced pitch are stored as `NaN`, later converted to `None`.

#### Onset Detection

- Method: `librosa.onset.onset_strength()` + `onset_detect()`
- Peaks are converted to time in seconds via `librosa.frames_to_time()`

#### Output

A Python dictionary that looks like this:

``` json
{
  "sample_rate": 22050,
  "pitch_contour": [300.5, 310.2, null, 280.1, ...],
  "onset_times": [0.12, 0.34, 0.56, ...]
}
```

💾 Saving Output
The output is saved to output/features.json. To ensure compatibility with JSON, all NaN values are converted to None, and all NumPy floats are converted to native Python float.

### Example serialization block

```python
os.makedirs("output", exist_ok=True)
with open("output/features.json", "w") as f:
    json.dump(data, f, indent=2)
```

📈 Optional: Plotting the Pitch Contour
The pitch contour can be visualized with:

```python
plot_pitch(pitch_contour, output_file="pitch_contour.png")
```

This produces a simple time-series graph for manual inspection.

🔁 Reproducibility Notes
Python version used: 3.9.12 (Homebrew)

Key libraries:

- librosa==0.11.0
- numpy==2.0.2
- matplotlib==3.9.4

Run from terminal with:
python3 run_analysis.py

Ensure data/ contains a valid .wav file, and output/ exists (or is created by the script).
