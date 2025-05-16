# speech-to-score

This repository transforms a spoken `.wav` file into an expressive musical score using a multi-stage compositional pipeline.

## Quick Start

```bash
python3 run_full_pipeline.py data/your_speech.wav

Outputs will be saved in /output/ with your filename as prefix.

Project Structure
run_full_pipeline.py – one-command script

src/ – modular processing code

docs/ – detailed methodology (Markdown per stage)

data/ – input .wav files

output/ – extracted features, MIDI files, grouped phrases

yaml
Copy
Edit
