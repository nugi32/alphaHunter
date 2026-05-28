# AlphaHunter - Multi-Timeframe Analysis & Report Generator

This guide describes the integrated workflow for running technical analysis across multiple timeframes and generating HTML reports automatically.

## 📁 File structure

```
alphaHunter/
├── main.py                    # Main orchestrator
├── analysis.py               # Technical analysis engine
├── patterns.txt              # Batch pattern file
├── output_*.csv              # Generated analysis outputs
│
├── report/
│   ├── report_generator.py   # Flexible report generator
│   ├── run_report.py         # Auto-detect CSV files
│   ├── reports/              # HTML and image reports
│   ├── templates/
│   │   └── report.html
│   └── dummy_analysis.py
│
└── data/
    └── XAUUSD/
        ├── XAUUSD1.csv       # M1
        ├── XAUUSD5.csv       # M5
        ├── XAUUSD15.csv      # M15
        ├── XAUUSD60.csv      # H1
        ├── XAUUSD240.csv     # H4
        ├── XAUUSD1440.csv    # D1
        ├── XAUUSD10080.csv   # W1
        └── XAUUSD43200.csv   # MN1
```

## 🚀 How to use

### 1. Run all timeframes at once

```bash
python main.py
```

This will:
- Analyze all 8 timeframes (M1, M5, M15, H1, H4, D1, W1, MN1)
- Store CSV output for each timeframe (`output_M1.csv`, `output_D1.csv`, etc.)
- Generate HTML reports automatically

### 2. Run a specific timeframe

```bash
# Single timeframe
python main.py --tf D1

# Multiple timeframes
python main.py --tf D1 H4 H1

# Skip report generation and save CSV only
python main.py --tf D1 --no-report
```

### 3. Analyze with specific patterns

```bash
# Single pattern
python main.py --pattern "RSI_14>70,MACD>MACD_SIGNAL"

# With timeframe selection
python main.py --tf D1 H4 --pattern "EMA_20>EMA_50"
```

### 4. Batch analysis from a pattern file

```bash
# Use the existing patterns.txt
python main.py --patterns patterns.txt

# Or use your own custom file
python main.py --patterns my_patterns.txt
```

Pattern file format:
```
# Comment lines starting with # are ignored
EMA_20>EMA_50
MACD>MACD_SIGNAL,RSI_14>50
Close>PIVOT
# Blank lines are also ignored
```

## 📊 Outputs

### CSV files
- `output_M1.csv`, `output_D1.csv`, etc.
- Contain all calculated indicators
- Can be used for downstream analysis

### HTML reports
- Location: `report/reports/`
- Format: `{TIMEFRAME}_{PATTERN}.html`
  - Example: `D1_all.html`, `H4_RSI_gt_70.html`
- Contains:
  - Statistics (total, bullish/bearish, average move)
  - Price movement histograms
  - RSI versus price move scatter plots
  - Sample data (first 10 rows)
  - Automated insights

### Images
- `report/reports/{TF}_{PATTERN}_histogram.png`
- `report/reports/{TF}_{PATTERN}_scatter.png`

## 📝 Available patterns

See `patterns.txt` for the full pattern catalog. Examples:

### Single indicators
```
EMA_20>EMA_50          # EMA 20 above EMA 50
RSI_14>70              # RSI overbought
MACD>MACD_SIGNAL       # MACD bullish cross
ADX_14>=20             # Strong trend
MOMENTUM>0             # Positive momentum
```

### Combined patterns
```
EMA_20>EMA_50,MACD>MACD_SIGNAL
Close>BB_UPPER,ADX_14>=20
SQUEEZE_ON=true,COMPRESSION=1
```

### Changes made

#### 1. `report_generator.py`
- ✅ More flexible: supports standard CSV columns
- ✅ Supports longer pathnames
- ✅ Creates directories automatically
- ✅ Improved error handling

#### 2. `run_report.py`
- ✅ Auto-detects CSV files
- ✅ No more hardcoded filenames
- ✅ Batch processing support

#### 3. `main.py`
- ✅ Main orchestrator for all operations
- ✅ Flexible CLI arguments
- ✅ Batch pattern analysis
- ✅ Progress tracking

## 💡 Usage tips

### Fast testing
```bash
# Test one timeframe without a report
python main.py --tf D1 --no-report

# Test one pattern on one timeframe
python main.py --tf D1 --pattern "RSI_14>70"
```

### Batch analysis
```bash
# Analyze with many patterns
python main.py --patterns patterns.txt

# Analyze only a selected timeframe
python main.py --tf D1 --patterns patterns.txt
```

### Generate a report from an existing CSV
```bash
cd report
python run_report.py
```

## ⚙️ Pattern customization

Edit `patterns.txt` to add or change patterns:

```
# Add a new pattern at the end of the file
MyNewPattern=1
INDICATOR_A>VALUE,INDICATOR_B<VALUE
```

Patterns are executed when you run `python main.py --patterns patterns.txt`.

## 📌 Status

✅ **Completed:**
- `report_generator.py`: Updated and flexible
- `run_report.py`: Updated and auto-detects CSV files
- `main.py`: Created with full functionality
- `patterns.txt`: Template patterns available

**Tested:**
- ✅ D1 timeframe analysis and report generation (14s)
- ✅ CSV output creation
- ✅ HTML report generation with correct paths

**Performance notes:**
- M1 (~700K candles): ~2-3 minutes
- H1 (~9K candles): ~20s
- D1 (~700 candles): ~15s
- All timeframes: ~15-20 minutes total

---

**Next steps:**
- Run `python main.py --tf D1` for a quick test
- View generated reports in `report/reports/D1_all.html`
- Edit `patterns.txt` as needed
- Run `python main.py --patterns patterns.txt` for batch analysis
