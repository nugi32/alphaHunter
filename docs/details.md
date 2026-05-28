# AlphaHunter Detailed Operating Guide

This document explains the full runtime behavior of AlphaHunter, including command usage, data preparation, search-space generation, and result structure.

## 1. Data inputs

AlphaHunter expects raw candle data in CSV format with at least the following columns:

- `UTC`
- `Open`
- `High`
- `Low`
- `Close`
- `Volume`

The data loader uses the `data/` repository structure and timeframe-specific files under `data/<symbol>/`.

## 2. Runtime commands

### Prepare mode

`python main.py prepare --tf <timeframe>` loads data for the requested timeframe, enriches it with indicators and candle patterns, and writes `payload_<timeframe>.csv`.

Optional arguments:

- `--output` to override the CSV path.
- `--limit` to cap the number of rows loaded.

### Run mode

`python main.py run --tf <timeframe>` reads the enriched CSV, loads the payload from `payload.json`, runs the search space, measures reactions, and writes ranked outputs into `results/`.

Useful options:

- `--csv` to override the enriched input file.
- `--payload` to point to another payload file.
- `--out` to change the output root.
- `--lookaheads` to run a sweep across multiple forward horizons.

### All mode

`python main.py all --tf <timeframe>` runs `prepare` and `run` sequentially in a single command.

## 3. Payload structure

`payload.json` defines both the condition library and analysis thresholds.

### Condition definitions

Each entry in `conditions` should define:

- `name` — human-readable condition name
- `type` — condition style such as threshold, cross, or ratio
- column references (`col`, `col2`) and numeric values (`val`, `factor`)

Examples include RSI thresholds, moving-average cross conditions, volume spikes, and candle pattern flags.

### Global thresholds

The payload also contains global parameters:

- `max_depth` — maximum condition combination depth
- `min_samples` — minimum match count to keep a candidate
- `lookahead` — forward horizon used for reaction measurement
- `validation_split` — chronological split used during overfit checks
- `min_direction_pct`, `max_mag_cv`, `min_freq_pct`, `max_freq_pct` — filtering thresholds
- `dir_grace` — tolerance used in direction consistency logic

## 4. Analysis flow

The pipeline follows these stages:

1. **Prepare**: enrich candles with indicators and pattern flags.
2. **Build search space**: generate candidate combinations from payload conditions.
3. **Scan**: evaluate every candidate over the dataset.
4. **Measure reactions**: compute forward movement and magnitude for each matched event.
5. **Consistency filter**: keep only stable directional reactions.
6. **Validate**: apply overfit checks and minimum frequency thresholds.
7. **Rank and report**: rank surviving candidates and generate outputs.

## 5. Output files

### Enriched CSV

`payload_<timeframe>.csv` contains the raw features plus generated indicators and pattern columns.

### Analysis results

The `results/` folder contains ranked candidates, summary tables, and generated reports.

When a sweep is run, each lookahead creates a subfolder such as `results/la3/`, `results/la5/`, or `results/la10/`.

### Sweep summary

A sweep writes `results/sweep_summary.csv`, summarizing the number of valid conditions and top scores by lookahead.

## 6. Example workflow

```bash
python main.py all --tf H1 --lookaheads 3 5 10
python main.py all --tf D1 --limit 5000 --lookaheads 5
```

This creates enriched CSV outputs, runs the analysis pipeline across the requested horizons, and writes results into the output tree.

## 7. Recommended next steps

- Read `docs/flow.md` for the conceptual pipeline.
- Read `docs/param.md` for payload parameter behavior.
- Adjust `payload.json` before running broader sweeps.
