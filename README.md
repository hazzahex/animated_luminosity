# animated_luminosity

A small script that measures how the **brightness of a single pixel changes across a sequence of image frames** — useful for turning an animation (exported as numbered PNGs) into a luminosity-over-time curve.

## What it does

1. Prompts you to pick a folder of frames (via a native folder picker).
2. Collects every `.png` in that folder, sorted by name (non-PNG files are counted and ignored).
3. For each frame, reads the pixel at a fixed coordinate (`5, 5` by default) and computes its **greyscale luminosity** as the average of the R, G, B channels normalised to `0.0–1.0`.
4. Prints the values and writes them to `output.csv` as `interval, float` rows (one per frame, in order).

## Usage

```bash
pip install pillow
python main.py
```

A folder-selection dialog opens — choose the directory containing your `.png` frames. Results are written to `output.csv` in the working directory.

To sample a different pixel, edit the `x_coord` / `y_coord` values near the top of `main.py` (there's also commented-out code to prompt for them interactively).

## Contents

- `main.py` — the script.
- `sample_data/` — 120 synthetic test frames (solid greys that brighten linearly) for trying it out.
- `output.csv` — example output from running it against `sample_data/`.
