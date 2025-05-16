from src.structure_parts import load_mapped_notes, assign_instruments

# Load mapped pitch-time pairs
notes = load_mapped_notes()

# Assign notes to instruments based on pitch
instrument_parts = assign_instruments(notes)

# Print a sample of the results
for name, part in instrument_parts.items():
    print(f"\n🎻 {name}: {len(part)} notes")
    for note in part[:5]:  # show only first 5 notes
        print(f"  {note}")
