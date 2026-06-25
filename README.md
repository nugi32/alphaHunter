# 📈 alphaHunter

> **Python-based quantitative research engine for discovering statistically repeatable market patterns from historical price data.**

---

## ⚠️ Development Status

> **Important**
>
> The `main` branch currently contains project documentation only.
>
> Active development and source code are maintained in the `lowTF` branch.
>
> To access the latest implementation:
>
> ```bash
> git clone -b lowTF git@github.com:nugi32/alphaHunter.git
> ```
>
> or:
>
> ```bash
> git checkout lowTF
> ```
>
> Additional technical documentation can be found in the `docs/` directory.

---

## 🎯 What is alphaHunter?

alphaHunter is a Python-based quantitative research tool designed to identify statistically repeatable price-action patterns from historical market data.

The engine analyzes historical CSV datasets and evaluates combinations of:

* Technical indicators
* Market conditions
* Price action structures
* Chart patterns
* Statistical relationships

to identify setups that have demonstrated consistent historical behavior across different market environments and time periods.

The ultimate goal is to transform statistically validated findings into automated trading systems for **MetaTrader 5 (MQL5)**.

---

## ✨ Features

* 📊 Historical pattern mining from CSV price data
* 📈 Technical indicator analysis
* 🔍 Chart pattern recognition
* 📉 Statistical validation of pattern performance
* ⏳ Multi-timeframe market research
* ⚡ Large-scale pattern screening
* 🏆 Automated pattern ranking
* 🧠 Historical edge discovery
* 🤖 MQL5 strategy development workflow
* 📚 Research-first quantitative methodology

---

## 🧪 Project Philosophy

Most trading systems begin with assumptions.

alphaHunter begins with data.

Instead of asking:

> "Does this strategy look good?"

alphaHunter asks:

> **"Has this pattern demonstrated a measurable historical edge across market history?"**

The project follows a data-driven research process:

1. Extract market structure from raw price data.
2. Generate technical and statistical features.
3. Detect indicator and pattern-based conditions.
4. Evaluate future price behavior after each occurrence.
5. Rank patterns by consistency and statistical performance.
6. Convert validated findings into MQL5 trading systems.

---

## 🖥️ Hardware Requirements

Resource requirements depend heavily on:

* Dataset size
* Historical depth
* Number of generated indicators
* Number of pattern combinations
* Feature engineering complexity

### Recommended

| Component | Specification            |
| --------- | ------------------------ |
| CPU       | Modern 6+ Core Processor |
| RAM       | 32 GB+                   |
| Storage   | SSD                      |
| Python    | 3.10+                    |

### Minimum

| Component | Specification       |
| --------- | ------------------- |
| CPU       | Quad-Core Processor |
| RAM       | 16 GB               |
| Storage   | SSD Recommended     |

> ⚠️ Large datasets may become extremely slow or fail on systems with insufficient memory.

---

## 🚨 Dataset Expansion Warning

alphaHunter performs extensive preprocessing and feature engineering before analysis begins.

Generated data may include:

* Technical indicators
* Pattern metadata
* Statistical metrics
* Historical context features
* Validation payloads
* Intermediate analysis structures

Because of this, datasets can become dramatically larger than the original CSV file.

### Real Example

| Stage                      | Size    |
| -------------------------- | ------- |
| Original XAUUSD D1 CSV     | 311 KB  |
| Generated Analysis Payload | 13.2 MB |

### Growth

* Approximately **42× larger**
* More than **4,000% increase in size**

### Important

❌ Do not estimate memory requirements from CSV size alone.

A seemingly small dataset can expand significantly after payload generation and feature engineering.

> ⚠️ Systems with insufficient RAM may experience severe slowdowns, excessive disk swapping, or crashes.

---

## 📂 Data Format

Input data should be supplied as CSV files containing historical market prices.

Example:

```csv
Date,Open,High,Low,Close,Volume
2024-01-01,2065.12,2070.50,2059.80,2068.22,1000
2024-01-02,2068.22,2075.10,2064.55,2072.85,1200
```

Required columns may vary depending on the analysis module.

---

## 🔄 Research Workflow

```text
Historical CSV Data
        │
        ▼
Data Validation
        │
        ▼
Feature Engineering
        │
        ▼
Technical Indicators
        │
        ▼
Pattern Detection
        │
        ▼
Statistical Evaluation
        │
        ▼
Pattern Ranking
        │
        ▼
MQL5 Strategy Development
```

---

## 🔬 Methodology

### 1. Data Collection

Load historical market data from CSV files.

### 2. Feature Engineering

Generate derived information from OHLCV data.

Examples:

* Moving averages
* Volatility metrics
* Trend measurements
* Momentum indicators
* Custom quantitative features

### 3. Pattern Detection

Search for conditions such as:

* Indicator relationships
* Price-action structures
* Chart formations
* Multi-indicator confirmations

### 4. Statistical Analysis

Evaluate how price behaved after pattern occurrences.

Metrics may include:

* Win rate
* Average return
* Expectancy
* Frequency
* Stability
* Historical consistency

### 5. Pattern Ranking

Rank discovered patterns according to statistical performance and robustness.

---

## 🌿 Branches

### `main`

Documentation and project overview.

### `lowTF`

Active development branch containing:

* Experimental features
* Latest source code
* New research modules
* Optimization work
* Low timeframe analysis improvements

Most current development occurs here.

---

## 📚 Documentation

Additional technical documentation, research notes, and implementation details may be available inside the:

```text
docs/
```

directory on development branches.

---

## 🎯 Intended Use

alphaHunter is a quantitative research and development tool.

Its purpose is to discover historically repeatable market behaviors and evaluate trading hypotheses using statistical analysis.

Historical performance does **not** guarantee future results.

All generated strategies should be independently validated and forward-tested before live deployment.

---

## ⚠️ Disclaimer

This software is provided for research and educational purposes only.

Nothing in this repository constitutes:

* Financial advice
* Investment advice
* Trading recommendations

Trading financial markets involves substantial risk.

Users are solely responsible for any decisions made using information generated by this project.

---

## 📜 License

This project is currently proprietary.

No open-source license has been assigned at this time.

Licensing terms may be added in the future.

---

<div align="center">

**Built for quantitative research, not trading myths.**

</div>
