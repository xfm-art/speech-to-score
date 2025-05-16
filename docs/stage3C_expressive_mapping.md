---
title: "Stage 3C: Gesture-Level Expressive Mapping"
author: "Anna Troisi"
date: 2025-05-16
description: "Embedding expressivity and temporal phrasing into speech-derived score materials."
tags: [speech-to-score, expressive mapping, articulation, dynamics, music21, algorithmic composition]
---

## Stage 3C: Gesture-Level Expressive Mapping Method (Interdisciplinary Framework)

This stage builds on temporally grouped phrases (Stage 3B) by enriching each phrase with expressive detail. Drawing on rhythmic density, phrase length, and pacing, musical parameters such as dynamics, articulation, duration, and velocity are embedded into the symbolic representation.

Rather than attempting semantic or phonetic interpretation, this method treats each phrase as a gesture and derives musicality from timing and shape. It introduces performative nuance, rhetorical inflection, and breath-informed contour—positioning this stage at the boundary between algorithmic scoring and compositional agency.

---

## 🎯 Objective

To map speech-driven phrase gestures into expressive musical parameters:

- **Phrase length** → dynamic range (`p`, `mf`, `f`)
- **Phrase density** → articulation style (`staccato`, `tenuto`, or none)
- **Phrase start** → accented first note
- **Phrasal pacing** → symbolic duration (short = clipped, slow = sustained)
- **Velocity** → mapped from dynamic label for MIDI playback contrast

---

## 🧰 Tools and Environment

- Python 3.9+
- [`music21`](https://web.mit.edu/music21/) v6+
- `stage3B_grouped_phrases.json` as input
- `stage3C_expressive_score.mid` as MIDI output

---

## 📥 Input Format

```json
[
  [
    {"midi": 91, "onset": 0.0},
    {"midi": 89, "onset": 0.25},
    ...
  ],
  [
    {"midi": 58, "onset": 10.5},
    ...
  ]
]

Each top-level list represents a phrase of notes grouped by temporal proximity.

🎼 Expressive Mapping Process
Phrase Analysis

Phrase length → symbolic dynamic (p, mf, f)

Phrase duration → calculate phrase density (notes/sec)

Note Rendering

First note: accented

All notes: assigned MIDI velocity based on dynamic

All notes: assigned quarterLength based on density

Sparse phrases → longer notes (0.5)

Dense phrases → shorter (0.2)

Intermediate → (0.33)

Articulation Assignment

Dense → staccato

Sparse → tenuto

Intermediate → no marking

MIDI Export

Constructed in music21 as a single-part piano score

Exported as output/stage3C_expressive_score.mid

🔁 Reproducibility Notes
Python version: 3.9.12 (Homebrew)

All phrase data loaded from: output/stage3B_grouped_phrases.json

Script: src/expressive_rendering.py

MIDI saved to: output/stage3C_expressive_score.mid

🎧 Observations from Playback
The output reveals gestural clusters reflective of speech pacing. Short phrases yield percussive ideas; longer phrases feel sustained and rhetorical. Though rendered monophonically, the variation in articulation and dynamics introduces depth, serving as both analytical output and musical prompt.

🧭 Next Steps
Potential to add slurs/rests from silence gaps

Option to assign expressive functions to instruments in 3D

Explore data from phoneme/energy parsing for prosodic enrichment
