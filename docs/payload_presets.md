# Payload Presets by Timeframe and Difficulty

This guide provides copy-paste-ready payload presets for the main timeframe families and three difficulty levels: low, medium, and hard.

Use the medium preset as the default starting point. Increase strictness for hard mode when you want fewer but cleaner candidates, and relax the filters for low mode when you want broader exploration.

## Shared structure

Each preset uses the same JSON shape:

```json
{
  "conditions": [
    { "name": "EMA13_above_EMA21", "type": "cross", "col": "EMA_13", "op": ">", "col2": "EMA_21" }
  ],
  "max_depth": 5,
  "max_combinations": 100000000,
  "min_samples": 5,
  "lookahead": 1,
  "validation_split": 0.2,
  "min_direction_pct": 65.0,
  "max_mag_cv": 0.85,
  "min_freq_pct": 0.05,
  "max_freq_pct": 5.0,
  "dir_grace": 0.80,
  "memory_spill_threshold_percent": 30,
  "storage_backend": "sqlite",
  "storage_path": "./spool.db"
}
```

## Low preset

Best for fast exploration and broad candidate discovery.

```json
{
  "max_depth": 3,
  "max_combinations": 5000000,
  "min_samples": 3,
  "lookahead": 1,
  "validation_split": 0.25,
  "min_direction_pct": 55.0,
  "max_mag_cv": 0.95,
  "min_freq_pct": 0.02,
  "max_freq_pct": 8.0,
  "dir_grace": 0.70,
  "memory_spill_threshold_percent": 35,
  "storage_backend": "sqlite",
  "storage_path": "./spool.db"
}
```

## Medium preset

Balanced default preset that matches the current payload logic well.

```json
{
  "max_depth": 5,
  "max_combinations": 200000000000000000000000000000000000000000000000000000000000000000,
  "min_samples": 5,
  "lookahead": 1,
  "validation_split": 0.2,
  "min_direction_pct": 65.0,
  "max_mag_cv": 0.85,
  "min_freq_pct": 0.05,
  "max_freq_pct": 5.0,
  "dir_grace": 0.80,
  "memory_spill_threshold_percent": 30,
  "storage_backend": "sqlite",
  "storage_path": "./spool.db"
}
```

## Hard preset

Best for stricter filtering and fewer but more statistically robust candidates.

```json
{
  "max_depth": 6,
  "max_combinations": 100000000000000000000000000000000000000000000000000000000000000000,
  "min_samples": 8,
  "lookahead": 2,
  "validation_split": 0.2,
  "min_direction_pct": 70.0,
  "max_mag_cv": 0.75,
  "min_freq_pct": 0.08,
  "max_freq_pct": 3.0,
  "dir_grace": 0.85,
  "memory_spill_threshold_percent": 25,
  "storage_backend": "sqlite",
  "storage_path": "./spool.db"
}
```

## Timeframe-specific tuning

The values below are the recommended starting points for each timeframe. They keep the same structure but adjust lookahead and sample requirements to match the noise profile of each interval.

### M1

- Low: `lookahead = 1`, `min_samples = 3`, `max_depth = 3`
- Medium: `lookahead = 1`, `min_samples = 5`, `max_depth = 4`
- Hard: `lookahead = 2`, `min_samples = 8`, `max_depth = 5`

### M5

- Low: `lookahead = 1`, `min_samples = 4`, `max_depth = 3`
- Medium: `lookahead = 2`, `min_samples = 6`, `max_depth = 4`
- Hard: `lookahead = 2`, `min_samples = 9`, `max_depth = 5`

### M15

- Low: `lookahead = 1`, `min_samples = 4`, `max_depth = 3`
- Medium: `lookahead = 2`, `min_samples = 6`, `max_depth = 4`
- Hard: `lookahead = 3`, `min_samples = 10`, `max_depth = 5`

### H1

- Low: `lookahead = 1`, `min_samples = 5`, `max_depth = 3`
- Medium: `lookahead = 2`, `min_samples = 8`, `max_depth = 4`
- Hard: `lookahead = 3`, `min_samples = 12`, `max_depth = 5`

### H4

- Low: `lookahead = 2`, `min_samples = 5`, `max_depth = 3`
- Medium: `lookahead = 3`, `min_samples = 8`, `max_depth = 4`
- Hard: `lookahead = 4`, `min_samples = 12`, `max_depth = 5`

### D1

- Low: `lookahead = 2`, `min_samples = 6`, `max_depth = 3`
- Medium: `lookahead = 3`, `min_samples = 10`, `max_depth = 4`
- Hard: `lookahead = 4`, `min_samples = 15`, `max_depth = 5`

### W1

- Low: `lookahead = 3`, `min_samples = 8`, `max_depth = 3`
- Medium: `lookahead = 4`, `min_samples = 12`, `max_depth = 4`
- Hard: `lookahead = 5`, `min_samples = 18`, `max_depth = 5`

### MN1

- Low: `lookahead = 4`, `min_samples = 10`, `max_depth = 3`
- Medium: `lookahead = 5`, `min_samples = 15`, `max_depth = 4`
- Hard: `lookahead = 6`, `min_samples = 20`, `max_depth = 5`

## Recommended usage

- Use low preset for quick scan sweeps and early-stage research.
- Use medium preset for balanced production runs.
- Use hard preset when you want to focus on higher-quality, lower-noise signals.

If you want, I can also turn these presets into separate JSON files such as payload_low.json, payload_medium.json, and payload_hard.json for each timeframe.
