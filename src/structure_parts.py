import json
import os

def load_mapped_notes(path="output/mapped_notes.json"):
    with open(path, "r") as f:
        notes = json.load(f)
    return notes

def assign_instruments(notes):
    """
    Assigns notes to 4 instruments based on pitch range.
    Returns a dict of lists: {instr_1: [...], instr_2: [...], ...}
    """
    parts = {
        "instrument_1": [],
        "instrument_2": [],
        "instrument_3": [],
        "instrument_4": []
    }

    for note in notes:
        midi = note["midi"]
        onset = note["onset"]

        if midi < 60:
            parts["instrument_1"].append(note)
        elif 60 <= midi < 72:
            parts["instrument_2"].append(note)
        elif 72 <= midi < 84:
            parts["instrument_3"].append(note)
        else:
            parts["instrument_4"].append(note)

    return parts

