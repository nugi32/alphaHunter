#!/usr/bin/env python3
"""
Quick start guide for alphaHunter main.py
"""

# ============================================================================
# QUICK START COMMANDS
# ============================================================================

# 1. RUN ALL TIMEFRAMES (M1, M5, M15, H1, H4, D1, W1, MN1)
# $ python main.py

# 2. RUN SPECIFIC TIMEFRAMES
# $ python main.py --tf D1 H4 H1

# 3. RUN WITH PATTERN
# $ python main.py --tf D1 --pattern "RSI_14>70"

# 4. BATCH ANALYSIS FROM PATTERNS FILE
# $ python main.py --patterns patterns.txt

# 5. SKIP REPORT GENERATION (ONLY CSV)
# $ python main.py --tf D1 --no-report

# 6. GENERATE REPORTS FROM EXISTING CSV
# $ cd report && python run_report.py

# ============================================================================
# AVAILABLE TIMEFRAMES
# ============================================================================
TIMEFRAMES = ["M1", "M5", "M15", "H1", "H4", "D1", "W1", "MN1"]

# ============================================================================
# EXAMPLE PATTERNS (see patterns.txt for more)
# ============================================================================
EXAMPLE_PATTERNS = [
    "RSI_14>70",                           # RSI overbought
    "MACD>MACD_SIGNAL",                    # Bullish MACD cross
    "EMA_20>EMA_50",                       # EMA 20 above 50
    "EMA_20>EMA_50,MACD>MACD_SIGNAL",      # Combined: both bullish
    "Close>BB_UPPER,ADX_14>=20",           # Breakout with strong trend
    "SQUEEZE_ON=true",                     # Bollinger/Keltner squeeze
    "COMPRESSION=1,VOL_REGIME=1",          # Compression + volume regime
    "RSI_14<30,STOCH_K<20",                # Oversold conditions
]

# ============================================================================
# OUTPUT LOCATIONS
# ============================================================================
"""
CSV Files: output_{TIMEFRAME}.csv
  - output_D1.csv
  - output_H4.csv
  - etc.

HTML Reports: report/reports/{TIMEFRAME}_{PATTERN}.html
  - report/reports/D1_all.html
  - report/reports/H4_RSI_gt_70.html
  - etc.

Report Images: report/reports/{TIMEFRAME}_{PATTERN}_*.png
  - *_histogram.png
  - *_scatter.png
"""

# ============================================================================
# PERFORMANCE (approx)
# ============================================================================
"""
M1: 2-3 minutes (700K+ candles)
M5: 1 minute
M15: 30-40 seconds
H1: 20-30 seconds
H4: 15-20 seconds
D1: 15 seconds (fastest)
W1: 15 seconds
MN1: 10 seconds

Full run (all 8 TF): ~15-20 minutes
"""

# ============================================================================
# NEXT STEPS
# ============================================================================
"""
1. Test with single timeframe:
   python main.py --tf D1

2. Check the report:
   open report/reports/D1_all.html

3. Try with a pattern:
   python main.py --tf D1 --pattern "RSI_14>70"

4. Batch analysis:
   python main.py --patterns patterns.txt

5. Edit patterns.txt to add your own patterns
"""

print(__doc__)
