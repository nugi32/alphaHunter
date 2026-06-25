# 📈 AlphaHunter

> **Candlestick and indicator brute-force analysis pipeline for discovering statistically repeatable market reactions.**

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
> Additional technical documentation and research notes can be found in the `docs/` directory on development branches.

---

## 🎯 What is AlphaHunter?

AlphaHunter is a quantitative research engine that loads historical market data, enriches each candle with technical indicators and pattern metadata, generates large search spaces of market conditions, and evaluates how price historically reacted after those conditions occurred.

The objective is to identify recurring market behaviors with measurable statistical consistency and transform those findings into automated trading systems.

Unlike traditional strategy development, AlphaHunter focuses on systematic discovery rather than manually testing trading ideas one by one.

---

## 🔬 What the Pipeline Does

### 1. Load Historical Market Data

Import raw OHLCV datasets for a selected market and timeframe.

### 2. Generate Enriched Datasets

Each candle is expanded with additional analytical features including:

* Technical indicators
* Candlestick patterns
* Volume analysis
* Market structure metrics
* Custom quantitative features

### 3. Build Search Spaces

Generate candidate condition combinations from the configured payload.

Examples:

* Indicator relationships
* Pattern combinations
* Market state filters
* Multi-condition setups

### 4. Brute-Force Condition Discovery

Scan all generated combinations across the historical dataset.

### 5. Measure Forward Reactions

Evaluate future market behavior after each condition appears using configurable lookahead windows.

Examples:

* Directional movement
* Percentage return
* Maximum favorable excursion (MFE)
* Maximum adverse excursion (MAE)

### 6. Validate Results

Apply filters designed to remove weak or unreliable findings:

* Frequency requirements
* Consistency thresholds
* Validation checks
* Overfitting controls

### 7. Rank Survivors

Score and rank surviving conditions based on historical performance metrics.

### 8. Export Research Results

Generate reports and datasets suitable for further quantitative analysis and MQL5 strategy development.

---

## ✨ Core Features

* 📊 Historical pattern mining from CSV market data
* 🕯️ Candlestick pattern analysis
* 📈 Technical indicator analysis
* 🔍 Brute-force condition discovery
* 📉 Forward reaction measurement
* 🧠 Historical edge discovery
* ⚖️ Statistical validation and ranking
* ⏳ Multi-timeframe research
* 📦 Configurable payload generation
* 🚀 Research workflow for MQL5 strategy development

---

## 🧪 Project Philosophy

Most trading systems start with assumptions.

AlphaHunter starts with data.

Instead of asking:

> "Does this strategy look profitable?"

AlphaHunter asks:

> **"Which market conditions have historically produced statistically repeatable reactions?"**

The project is designed around evidence-based strategy research rather than subjective chart interpretation.

---

## 🖥️ Hardware Requirements

Resource requirements depend heavily on:

* Dataset size
* Historical depth
* Number of indicators
* Payload complexity
* Number of generated combinations

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

AlphaHunter performs extensive preprocessing and feature engineering before analysis begins.

The generated payload may include:

* Technical indicators
* Candlestick pattern flags
* Statistical metrics
* Market structure features
* Validation payloads
* Intermediate analysis structures

Because of this, memory usage can become significantly larger than the original CSV file size.

### Real Example

| Stage                      | Size    |
| -------------------------- | ------- |
| Original XAUUSD D1 CSV     | 311 KB  |
| Generated Analysis Payload | 13.2 MB |

This represents approximately:

* **42× larger than the original dataset**
* **Over 4,000% growth in size**

Although the source file may appear small, preprocessing can dramatically increase memory consumption.

### Important Notes

* Do not estimate memory requirements from CSV size alone.
* Generated payloads can be many times larger than the source data.
* Long historical datasets combined with multiple indicators can consume substantial memory.
* Research workloads involving large datasets should ideally be performed on systems with **32 GB RAM or more**.

> ⚠️ Small CSV files can become significantly larger after payload generation and feature engineering. Systems with insufficient memory may experience severe slowdowns, excessive disk swapping, or crashes.

---

## 📂 Data Format

Input data should be provided as CSV files containing historical market prices.

Example:

```csv
Date,Open,High,Low,Close,Volume
2024-01-01,2065.12,2070.50,2059.80,2068.22,1000
2024-01-02,2068.22,2075.10,2064.55,2072.85,1200
```

Required columns may vary depending on the analysis module being used.

---

## 🔄 Research Workflow

```text
Raw OHLCV Data
        │
        ▼
Data Validation
        │
        ▼
Feature Engineering
        │
        ▼
Payload Generation
        │
        ▼
Condition Generation
        │
        ▼
Brute Force Search
        │
        ▼
Forward Reaction Analysis
        │
        ▼
Validation & Filtering
        │
        ▼
Pattern Ranking
        │
        ▼
Research Reports
        │
        ▼
MQL5 Strategy Development
```

---

## 📊 Typical Analysis Metrics

AlphaHunter may evaluate patterns using metrics such as:

* Win Rate
* Average Return
* Median Return
* Profit Factor
* Frequency of Occurrence
* MFE (Maximum Favorable Excursion)
* MAE (Maximum Adverse Excursion)
* Directional Consistency
* Historical Stability
* Validation Performance

Metrics may vary depending on the active research module.

---

## 🌿 Branch Information

### `main`

Repository landing page and project documentation.

Currently does **not** contain active source code.

### `lowTF`

Active development branch containing:

* Current implementation
* Experimental features
* New research modules
* Optimization work
* Low timeframe research tools

Most recent development occurs in this branch.

---

## 📚 Documentation

Additional technical documentation, architecture notes, and research information may be available inside:

```text
docs/
```

on development branches.

---

## 🎯 Intended Use

AlphaHunter is a quantitative research and development tool.

Its purpose is to discover historically repeatable market behaviors and evaluate trading hypotheses through statistical analysis.

Historical performance does **not** guarantee future results.

Any strategy derived from this project should be independently validated and forward-tested before live deployment.

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

### 📈 Built for quantitative research, not trading myths.

</div>
