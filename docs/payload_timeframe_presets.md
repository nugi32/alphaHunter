# Payload presets by timeframe

This guide provides JSON-ready preset settings for the current payload configuration. Each timeframe includes a low, medium, and high preset.

Here, low/medium/high means selectivity:

- Low = broader and less strict
- Medium = balanced default
- High = stricter and more selective

Use the same conditions array from payload.json for every preset. Each preset below is a complete tuning block that can be merged with that conditions list.

## M1

### Low

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

### Medium

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

### High

```json
{
  "max_depth": 5,
  "max_combinations": 1000000000,
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

## M5

### Low

```json
{
  "max_depth": 3,
  "max_combinations": 5000000,
  "min_samples": 4,
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

### Medium

```json
{
  "max_depth": 4,
  "max_combinations": 200000000,
  "min_samples": 6,
  "lookahead": 2,
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

### High

```json
{
  "max_depth": 5,
  "max_combinations": 1000000000,
  "min_samples": 9,
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

## M15

### Low

```json
{
  "max_depth": 3,
  "max_combinations": 5000000,
  "min_samples": 4,
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

### Medium

```json
{
  "max_depth": 4,
  "max_combinations": 200000000,
  "min_samples": 6,
  "lookahead": 2,
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

### High

```json
{
  "max_depth": 5,
  "max_combinations": 1000000000,
  "min_samples": 10,
  "lookahead": 3,
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

## H1

### Low

```json
{
  "max_depth": 3,
  "max_combinations": 5000000,
  "min_samples": 5,
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

### Medium

```json
{
  "max_depth": 4,
  "max_combinations": 200000000,
  "min_samples": 8,
  "lookahead": 2,
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

### High

```json
{
  "max_depth": 5,
  "max_combinations": 1000000000,
  "min_samples": 12,
  "lookahead": 3,
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

## H4

### Low

```json
{
  "max_depth": 3,
  "max_combinations": 5000000,
  "min_samples": 5,
  "lookahead": 2,
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

### Medium

```json
{
  "max_depth": 4,
  "max_combinations": 200000000,
  "min_samples": 8,
  "lookahead": 3,
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

### High

```json
{
  "max_depth": 5,
  "max_combinations": 1000000000,
  "min_samples": 12,
  "lookahead": 4,
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

## D1

### Low

```json
{
  "max_depth": 3,
  "max_combinations": 5000000,
  "min_samples": 6,
  "lookahead": 2,
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

### Medium

```json
{
  "max_depth": 4,
  "max_combinations": 200000000,
  "min_samples": 10,
  "lookahead": 3,
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

### High

```json
{
  "max_depth": 5,
  "max_combinations": 1000000000,
  "min_samples": 15,
  "lookahead": 4,
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

## W1

### Low

```json
{
  "max_depth": 3,
  "max_combinations": 5000000,
  "min_samples": 8,
  "lookahead": 3,
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

### Medium

```json
{
  "max_depth": 4,
  "max_combinations": 200000000,
  "min_samples": 12,
  "lookahead": 4,
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

### High

```json
{
  "max_depth": 5,
  "max_combinations": 1000000000,
  "min_samples": 18,
  "lookahead": 5,
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

## MN1

### Low

```json
{
  "max_depth": 3,
  "max_combinations": 5000000,
  "min_samples": 10,
  "lookahead": 4,
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

### Medium

```json
{
  "max_depth": 4,
  "max_combinations": 200000000,
  "min_samples": 15,
  "lookahead": 5,
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

### High

```json
{
  "max_depth": 5,
  "max_combinations": 1000000000,
  "min_samples": 20,
  "lookahead": 6,
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

## Quick usage

- Use low for broader scanning and faster exploration.
- Use medium as the balanced default.
- Use high when you want fewer but more selective signals.
