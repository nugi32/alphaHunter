# Market Condition Analysis Report

**Lookahead:** 5 candles  
**Min direction:** 55.0%  
**Max mag CV:** 0.85  

---

## #1 — `RSI7_oversold + close_above_EMA200 + breakout_down`

| Field | Value |
|---|---|
| Consistency Score | **0.6038** |
| Match Count | 4424 |
| Dominant Direction | BULLISH |
| Direction % | 55.0% |
| Mag ATR Mean | 2.2076 |
| Mag ATR Std | 1.4156 |
| Mag CV | 0.6412 |
| Timing (candles) | 3.5 |
| Persistence | 2.94 |
| Frequency | 0.9527% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train   2664 samples  bullish   56.0%  mag_atr=2.2512
    val      790 samples  bullish   54.0%  mag_atr=2.084
    oos      970 samples  bullish   53.2%  mag_atr=2.1886
```

> When [RSI7_oversold + close_above_EMA200 + breakout_down] occurs, price historically reacts BULLISH 55.0% of the time with an average move of 2.21 ATR (high variance) and stable repetition across validation splits.

---

## #2 — `RSI7_oversold + EMA50_above_EMA100 + close_above_EMA200 + breakout_down`

| Field | Value |
|---|---|
| Consistency Score | **0.6038** |
| Match Count | 4421 |
| Dominant Direction | BULLISH |
| Direction % | 55.1% |
| Mag ATR Mean | 2.2061 |
| Mag ATR Std | 1.4145 |
| Mag CV | 0.6412 |
| Timing (candles) | 3.5 |
| Persistence | 2.94 |
| Frequency | 0.9521% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train   2663 samples  bullish   56.0%  mag_atr=2.2508
    val      789 samples  bullish   54.0%  mag_atr=2.0816
    oos      969 samples  bullish   53.2%  mag_atr=2.1845
```

> When [RSI7_oversold + EMA50_above_EMA100 + close_above_EMA200 + breakout_down] occurs, price historically reacts BULLISH 55.1% of the time with an average move of 2.21 ATR (high variance) and stable repetition across validation splits.

---

## #3 — `RSI7_oversold + EMA50_above_EMA100 + close_above_EMA200 + vol_spike_1x5 + breakout_down`

| Field | Value |
|---|---|
| Consistency Score | **0.5697** |
| Match Count | 1949 |
| Dominant Direction | BULLISH |
| Direction % | 55.2% |
| Mag ATR Mean | 2.402 |
| Mag ATR Std | 1.4874 |
| Mag CV | 0.6192 |
| Timing (candles) | 3.47 |
| Persistence | 2.92 |
| Frequency | 0.4197% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train   1170 samples  bullish   56.2%  mag_atr=2.4341
    val      360 samples  bullish   52.2%  mag_atr=2.3261
    oos      419 samples  bullish   54.6%  mag_atr=2.3776
```

> When [RSI7_oversold + EMA50_above_EMA100 + close_above_EMA200 + vol_spike_1x5 + breakout_down] occurs, price historically reacts BULLISH 55.2% of the time with an average move of 2.40 ATR (high variance) and stable repetition across validation splits.

---

## #4 — `RSI7_oversold + close_above_EMA200 + vol_spike_1x5 + breakout_down`

| Field | Value |
|---|---|
| Consistency Score | **0.5695** |
| Match Count | 1950 |
| Dominant Direction | BULLISH |
| Direction % | 55.1% |
| Mag ATR Mean | 2.4039 |
| Mag ATR Std | 1.4894 |
| Mag CV | 0.6196 |
| Timing (candles) | 3.47 |
| Persistence | 2.92 |
| Frequency | 0.4199% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train   1170 samples  bullish   56.2%  mag_atr=2.4341
    val      360 samples  bullish   52.2%  mag_atr=2.3261
    oos      420 samples  bullish   54.5%  mag_atr=2.3865
```

> When [RSI7_oversold + close_above_EMA200 + vol_spike_1x5 + breakout_down] occurs, price historically reacts BULLISH 55.1% of the time with an average move of 2.40 ATR (high variance) and stable repetition across validation splits.

---

## #5 — `EMA21_below_EMA50 + close_above_EMA200 + vol_spike_2x + squeeze_active + CCI14_oversold`

| Field | Value |
|---|---|
| Consistency Score | **0.5694** |
| Match Count | 238 |
| Dominant Direction | BULLISH |
| Direction % | 58.8% |
| Mag ATR Mean | 2.5007 |
| Mag ATR Std | 1.4031 |
| Mag CV | 0.5611 |
| Timing (candles) | 3.71 |
| Persistence | 2.94 |
| Frequency | 0.0513% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    132 samples  bullish   58.3%  mag_atr=2.6622
    val       52 samples  bullish   69.2%  mag_atr=2.3263
    oos       54 samples  bullish   50.0%  mag_atr=2.274
```

> When [EMA21_below_EMA50 + close_above_EMA200 + vol_spike_2x + squeeze_active + CCI14_oversold] occurs, price historically reacts BULLISH 58.8% of the time with an average move of 2.50 ATR (moderate variance) and stable repetition across validation splits.

---

## #6 — `RSI7_oversold + close_above_EMA200 + MACD_bear_cross + vol_spike_1x5 + breakout_down`

| Field | Value |
|---|---|
| Consistency Score | **0.5680** |
| Match Count | 1892 |
| Dominant Direction | BULLISH |
| Direction % | 55.0% |
| Mag ATR Mean | 2.4139 |
| Mag ATR Std | 1.4973 |
| Mag CV | 0.6203 |
| Timing (candles) | 3.47 |
| Persistence | 2.92 |
| Frequency | 0.4074% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train   1137 samples  bullish   56.4%  mag_atr=2.4502
    val      352 samples  bullish   51.7%  mag_atr=2.328
    oos      403 samples  bullish   54.1%  mag_atr=2.3865
```

> When [RSI7_oversold + close_above_EMA200 + MACD_bear_cross + vol_spike_1x5 + breakout_down] occurs, price historically reacts BULLISH 55.0% of the time with an average move of 2.41 ATR (high variance) and stable repetition across validation splits.

---

## #7 — `EMA50_above_EMA100 + close_below_EMA200 + bear_engulf + breakout_down`

| Field | Value |
|---|---|
| Consistency Score | **0.5672** |
| Match Count | 239 |
| Dominant Direction | BULLISH |
| Direction % | 56.5% |
| Mag ATR Mean | 2.262 |
| Mag ATR Std | 1.2156 |
| Mag CV | 0.5374 |
| Timing (candles) | 3.74 |
| Persistence | 2.87 |
| Frequency | 0.0515% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    141 samples  bullish   56.0%  mag_atr=2.3272
    val       35 samples  bullish   77.1%  mag_atr=2.2873
    oos       63 samples  bullish   46.0%  mag_atr=2.1021
```

> When [EMA50_above_EMA100 + close_below_EMA200 + bear_engulf + breakout_down] occurs, price historically reacts BULLISH 56.5% of the time with an average move of 2.26 ATR (moderate variance) and stable repetition across validation splits.

---

## #8 — `RSI7_oversold + EMA50_above_EMA100 + bear_engulf + breakout_down + CCI14_oversold`

| Field | Value |
|---|---|
| Consistency Score | **0.5665** |
| Match Count | 355 |
| Dominant Direction | BULLISH |
| Direction % | 55.2% |
| Mag ATR Mean | 2.2589 |
| Mag ATR Std | 1.197 |
| Mag CV | 0.5299 |
| Timing (candles) | 3.65 |
| Persistence | 2.83 |
| Frequency | 0.0764% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    224 samples  bullish   55.8%  mag_atr=2.3242
    val       50 samples  bullish   64.0%  mag_atr=2.1655
    oos       81 samples  bullish   48.1%  mag_atr=2.1358
```

> When [RSI7_oversold + EMA50_above_EMA100 + bear_engulf + breakout_down + CCI14_oversold] occurs, price historically reacts BULLISH 55.2% of the time with an average move of 2.26 ATR (moderate variance) and stable repetition across validation splits.

---

## #9 — `RSI7_oversold + EMA21_below_EMA50 + close_above_EMA200 + vol_spike_1x5 + squeeze_active`

| Field | Value |
|---|---|
| Consistency Score | **0.5649** |
| Match Count | 242 |
| Dominant Direction | BULLISH |
| Direction % | 57.4% |
| Mag ATR Mean | 2.604 |
| Mag ATR Std | 1.4587 |
| Mag CV | 0.5602 |
| Timing (candles) | 3.49 |
| Persistence | 2.82 |
| Frequency | 0.0521% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    147 samples  bullish   57.1%  mag_atr=2.7965
    val       49 samples  bullish   53.1%  mag_atr=2.2457
    oos       46 samples  bullish   63.0%  mag_atr=2.3705
```

> When [RSI7_oversold + EMA21_below_EMA50 + close_above_EMA200 + vol_spike_1x5 + squeeze_active] occurs, price historically reacts BULLISH 57.4% of the time with an average move of 2.60 ATR (moderate variance) and stable repetition across validation splits.

---

## #10 — `RSI7_oversold + EMA21_below_EMA50 + close_above_EMA200 + breakout_down + squeeze_active`

| Field | Value |
|---|---|
| Consistency Score | **0.5627** |
| Match Count | 287 |
| Dominant Direction | BULLISH |
| Direction % | 57.8% |
| Mag ATR Mean | 2.2976 |
| Mag ATR Std | 1.3267 |
| Mag CV | 0.5774 |
| Timing (candles) | 3.58 |
| Persistence | 2.82 |
| Frequency | 0.0618% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    172 samples  bullish   55.8%  mag_atr=2.3526
    val       51 samples  bullish   64.7%  mag_atr=2.3193
    oos       64 samples  bullish   57.8%  mag_atr=2.1327
```

> When [RSI7_oversold + EMA21_below_EMA50 + close_above_EMA200 + breakout_down + squeeze_active] occurs, price historically reacts BULLISH 57.8% of the time with an average move of 2.30 ATR (moderate variance) and stable repetition across validation splits.

---

## #11 — `RSI7_oversold + EMA21_below_EMA50 + close_above_EMA200 + vol_spike_1x5 + breakout_down`

| Field | Value |
|---|---|
| Consistency Score | **0.5624** |
| Match Count | 454 |
| Dominant Direction | BULLISH |
| Direction % | 58.6% |
| Mag ATR Mean | 2.4692 |
| Mag ATR Std | 1.4816 |
| Mag CV | 0.6 |
| Timing (candles) | 3.48 |
| Persistence | 2.92 |
| Frequency | 0.0978% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    290 samples  bullish   61.4%  mag_atr=2.486
    val       75 samples  bullish   60.0%  mag_atr=2.4318
    oos       89 samples  bullish   48.3%  mag_atr=2.4461
```

> When [RSI7_oversold + EMA21_below_EMA50 + close_above_EMA200 + vol_spike_1x5 + breakout_down] occurs, price historically reacts BULLISH 58.6% of the time with an average move of 2.47 ATR (high variance) and stable repetition across validation splits.

---

## #12 — `RSI14_deep_oversold + ADX_trending + EMA21_below_EMA50 + EMA50_above_EMA100 + breakout_down`

| Field | Value |
|---|---|
| Consistency Score | **0.5622** |
| Match Count | 454 |
| Dominant Direction | BULLISH |
| Direction % | 60.1% |
| Mag ATR Mean | 2.5393 |
| Mag ATR Std | 1.5802 |
| Mag CV | 0.6223 |
| Timing (candles) | 3.67 |
| Persistence | 3.13 |
| Frequency | 0.0978% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    256 samples  bullish   62.9%  mag_atr=2.75
    val       82 samples  bullish   64.6%  mag_atr=2.0869
    oos      116 samples  bullish   50.9%  mag_atr=2.3943
```

> When [RSI14_deep_oversold + ADX_trending + EMA21_below_EMA50 + EMA50_above_EMA100 + breakout_down] occurs, price historically reacts BULLISH 60.1% of the time with an average move of 2.54 ATR (high variance) and stable repetition across validation splits.

---

## #13 — `RSI14_oversold + EMA50_above_EMA100 + close_above_EMA200`

| Field | Value |
|---|---|
| Consistency Score | **0.5612** |
| Match Count | 998 |
| Dominant Direction | BULLISH |
| Direction % | 56.8% |
| Mag ATR Mean | 2.3856 |
| Mag ATR Std | 1.4676 |
| Mag CV | 0.6152 |
| Timing (candles) | 3.44 |
| Persistence | 2.97 |
| Frequency | 0.2149% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    642 samples  bullish   58.3%  mag_atr=2.5055
    val      157 samples  bullish   57.3%  mag_atr=2.0951
    oos      199 samples  bullish   51.8%  mag_atr=2.2276
```

> When [RSI14_oversold + EMA50_above_EMA100 + close_above_EMA200] occurs, price historically reacts BULLISH 56.8% of the time with an average move of 2.39 ATR (high variance) and stable repetition across validation splits.

---

## #14 — `RSI14_oversold + EMA50_above_EMA100 + close_above_EMA200 + MACD_bear_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.5611** |
| Match Count | 960 |
| Dominant Direction | BULLISH |
| Direction % | 57.0% |
| Mag ATR Mean | 2.3784 |
| Mag ATR Std | 1.4634 |
| Mag CV | 0.6153 |
| Timing (candles) | 3.42 |
| Persistence | 2.99 |
| Frequency | 0.2067% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    613 samples  bullish   58.7%  mag_atr=2.4899
    val      154 samples  bullish   56.5%  mag_atr=2.1046
    oos      193 samples  bullish   51.8%  mag_atr=2.243
```

> When [RSI14_oversold + EMA50_above_EMA100 + close_above_EMA200 + MACD_bear_cross] occurs, price historically reacts BULLISH 57.0% of the time with an average move of 2.38 ATR (high variance) and stable repetition across validation splits.

---

## #15 — `RSI14_oversold + RSI7_oversold + EMA50_above_EMA100 + close_above_EMA200 + MACD_bear_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.5611** |
| Match Count | 960 |
| Dominant Direction | BULLISH |
| Direction % | 57.0% |
| Mag ATR Mean | 2.3784 |
| Mag ATR Std | 1.4634 |
| Mag CV | 0.6153 |
| Timing (candles) | 3.42 |
| Persistence | 2.99 |
| Frequency | 0.2067% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    613 samples  bullish   58.7%  mag_atr=2.4899
    val      154 samples  bullish   56.5%  mag_atr=2.1046
    oos      193 samples  bullish   51.8%  mag_atr=2.243
```

> When [RSI14_oversold + RSI7_oversold + EMA50_above_EMA100 + close_above_EMA200 + MACD_bear_cross] occurs, price historically reacts BULLISH 57.0% of the time with an average move of 2.38 ATR (high variance) and stable repetition across validation splits.

---

## #16 — `RSI14_oversold + close_above_EMA200`

| Field | Value |
|---|---|
| Consistency Score | **0.5608** |
| Match Count | 999 |
| Dominant Direction | BULLISH |
| Direction % | 56.8% |
| Mag ATR Mean | 2.3893 |
| Mag ATR Std | 1.4717 |
| Mag CV | 0.616 |
| Timing (candles) | 3.44 |
| Persistence | 2.97 |
| Frequency | 0.2151% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    642 samples  bullish   58.3%  mag_atr=2.5055
    val      157 samples  bullish   57.3%  mag_atr=2.0951
    oos      200 samples  bullish   51.5%  mag_atr=2.2472
```

> When [RSI14_oversold + close_above_EMA200] occurs, price historically reacts BULLISH 56.8% of the time with an average move of 2.39 ATR (high variance) and stable repetition across validation splits.

---

## #17 — `RSI14_oversold + RSI7_oversold + EMA50_above_EMA100 + close_above_EMA200`

| Field | Value |
|---|---|
| Consistency Score | **0.5608** |
| Match Count | 996 |
| Dominant Direction | BULLISH |
| Direction % | 56.7% |
| Mag ATR Mean | 2.3869 |
| Mag ATR Std | 1.4688 |
| Mag CV | 0.6154 |
| Timing (candles) | 3.44 |
| Persistence | 2.97 |
| Frequency | 0.2145% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    642 samples  bullish   58.3%  mag_atr=2.5055
    val      157 samples  bullish   57.3%  mag_atr=2.0951
    oos      197 samples  bullish   51.3%  mag_atr=2.2326
```

> When [RSI14_oversold + RSI7_oversold + EMA50_above_EMA100 + close_above_EMA200] occurs, price historically reacts BULLISH 56.7% of the time with an average move of 2.39 ATR (high variance) and stable repetition across validation splits.

---

## #18 — `RSI14_oversold + close_above_EMA200 + MACD_bear_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.5607** |
| Match Count | 961 |
| Dominant Direction | BULLISH |
| Direction % | 56.9% |
| Mag ATR Mean | 2.3824 |
| Mag ATR Std | 1.4676 |
| Mag CV | 0.616 |
| Timing (candles) | 3.42 |
| Persistence | 2.99 |
| Frequency | 0.2069% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    613 samples  bullish   58.7%  mag_atr=2.4899
    val      154 samples  bullish   56.5%  mag_atr=2.1046
    oos      194 samples  bullish   51.5%  mag_atr=2.2631
```

> When [RSI14_oversold + close_above_EMA200 + MACD_bear_cross] occurs, price historically reacts BULLISH 56.9% of the time with an average move of 2.38 ATR (high variance) and stable repetition across validation splits.

---

## #19 — `RSI14_oversold + RSI7_oversold + close_above_EMA200 + MACD_bear_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.5607** |
| Match Count | 961 |
| Dominant Direction | BULLISH |
| Direction % | 56.9% |
| Mag ATR Mean | 2.3824 |
| Mag ATR Std | 1.4676 |
| Mag CV | 0.616 |
| Timing (candles) | 3.42 |
| Persistence | 2.99 |
| Frequency | 0.2069% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    613 samples  bullish   58.7%  mag_atr=2.4899
    val      154 samples  bullish   56.5%  mag_atr=2.1046
    oos      194 samples  bullish   51.5%  mag_atr=2.2631
```

> When [RSI14_oversold + RSI7_oversold + close_above_EMA200 + MACD_bear_cross] occurs, price historically reacts BULLISH 56.9% of the time with an average move of 2.38 ATR (high variance) and stable repetition across validation splits.

---

## #20 — `RSI14_oversold + RSI7_oversold + close_above_EMA200`

| Field | Value |
|---|---|
| Consistency Score | **0.5604** |
| Match Count | 997 |
| Dominant Direction | BULLISH |
| Direction % | 56.7% |
| Mag ATR Mean | 2.3906 |
| Mag ATR Std | 1.4728 |
| Mag CV | 0.6161 |
| Timing (candles) | 3.44 |
| Persistence | 2.97 |
| Frequency | 0.2147% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    642 samples  bullish   58.3%  mag_atr=2.5055
    val      157 samples  bullish   57.3%  mag_atr=2.0951
    oos      198 samples  bullish   51.0%  mag_atr=2.2524
```

> When [RSI14_oversold + RSI7_oversold + close_above_EMA200] occurs, price historically reacts BULLISH 56.7% of the time with an average move of 2.39 ATR (high variance) and stable repetition across validation splits.

---

## #21 — `RSI14_oversold + EMA21_below_EMA50 + EMA50_above_EMA100 + close_above_EMA200 + MACD_bear_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.5599** |
| Match Count | 586 |
| Dominant Direction | BULLISH |
| Direction % | 57.3% |
| Mag ATR Mean | 2.3623 |
| Mag ATR Std | 1.4203 |
| Mag CV | 0.6012 |
| Timing (candles) | 3.51 |
| Persistence | 2.95 |
| Frequency | 0.1262% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    379 samples  bullish   59.4%  mag_atr=2.524
    val       93 samples  bullish   51.6%  mag_atr=2.0532
    oos      114 samples  bullish   55.3%  mag_atr=2.077
```

> When [RSI14_oversold + EMA21_below_EMA50 + EMA50_above_EMA100 + close_above_EMA200 + MACD_bear_cross] occurs, price historically reacts BULLISH 57.3% of the time with an average move of 2.36 ATR (high variance) and stable repetition across validation splits.

---

## #22 — `RSI14_oversold + EMA21_below_EMA50 + EMA50_above_EMA100 + close_above_EMA200`

| Field | Value |
|---|---|
| Consistency Score | **0.5597** |
| Match Count | 612 |
| Dominant Direction | BULLISH |
| Direction % | 57.2% |
| Mag ATR Mean | 2.3651 |
| Mag ATR Std | 1.422 |
| Mag CV | 0.6012 |
| Timing (candles) | 3.51 |
| Persistence | 2.95 |
| Frequency | 0.1318% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    396 samples  bullish   58.8%  mag_atr=2.5366
    val       96 samples  bullish   53.1%  mag_atr=2.0392
    oos      120 samples  bullish   55.0%  mag_atr=2.0599
```

> When [RSI14_oversold + EMA21_below_EMA50 + EMA50_above_EMA100 + close_above_EMA200] occurs, price historically reacts BULLISH 57.2% of the time with an average move of 2.37 ATR (high variance) and stable repetition across validation splits.

---

## #23 — `RSI7_oversold + EMA21_above_EMA50 + close_above_EMA200 + MACD_bull_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.5595** |
| Match Count | 690 |
| Dominant Direction | BULLISH |
| Direction % | 57.5% |
| Mag ATR Mean | 1.8552 |
| Mag ATR Std | 1.1359 |
| Mag CV | 0.6123 |
| Timing (candles) | 3.62 |
| Persistence | 2.94 |
| Frequency | 0.1486% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    470 samples  bullish   58.1%  mag_atr=1.844
    val       89 samples  bullish   62.9%  mag_atr=1.7769
    oos      131 samples  bullish   51.9%  mag_atr=1.9487
```

> When [RSI7_oversold + EMA21_above_EMA50 + close_above_EMA200 + MACD_bull_cross] occurs, price historically reacts BULLISH 57.5% of the time with an average move of 1.86 ATR (high variance) and stable repetition across validation splits.

---

## #24 — `RSI7_oversold + EMA21_above_EMA50 + EMA50_above_EMA100 + close_above_EMA200 + MACD_bull_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.5595** |
| Match Count | 690 |
| Dominant Direction | BULLISH |
| Direction % | 57.5% |
| Mag ATR Mean | 1.8552 |
| Mag ATR Std | 1.1359 |
| Mag CV | 0.6123 |
| Timing (candles) | 3.62 |
| Persistence | 2.94 |
| Frequency | 0.1486% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    470 samples  bullish   58.1%  mag_atr=1.844
    val       89 samples  bullish   62.9%  mag_atr=1.7769
    oos      131 samples  bullish   51.9%  mag_atr=1.9487
```

> When [RSI7_oversold + EMA21_above_EMA50 + EMA50_above_EMA100 + close_above_EMA200 + MACD_bull_cross] occurs, price historically reacts BULLISH 57.5% of the time with an average move of 1.86 ATR (high variance) and stable repetition across validation splits.

---

## #25 — `RSI7_oversold + EMA21_above_EMA50 + EMA50_above_EMA100 + MACD_bull_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.5594** |
| Match Count | 741 |
| Dominant Direction | BULLISH |
| Direction % | 57.1% |
| Mag ATR Mean | 1.8504 |
| Mag ATR Std | 1.1279 |
| Mag CV | 0.6095 |
| Timing (candles) | 3.62 |
| Persistence | 2.94 |
| Frequency | 0.1596% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    489 samples  bullish   57.9%  mag_atr=1.8351
    val      115 samples  bullish   60.9%  mag_atr=1.8131
    oos      137 samples  bullish   51.1%  mag_atr=1.9366
```

> When [RSI7_oversold + EMA21_above_EMA50 + EMA50_above_EMA100 + MACD_bull_cross] occurs, price historically reacts BULLISH 57.1% of the time with an average move of 1.85 ATR (high variance) and stable repetition across validation splits.

---

## #26 — `RSI14_deep_oversold + EMA50_above_EMA100 + breakout_down`

| Field | Value |
|---|---|
| Consistency Score | **0.5593** |
| Match Count | 739 |
| Dominant Direction | BULLISH |
| Direction % | 58.9% |
| Mag ATR Mean | 2.7378 |
| Mag ATR Std | 1.7376 |
| Mag CV | 0.6347 |
| Timing (candles) | 3.61 |
| Persistence | 3.08 |
| Frequency | 0.1591% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    422 samples  bullish   61.6%  mag_atr=2.8871
    val      129 samples  bullish   62.0%  mag_atr=2.3418
    oos      188 samples  bullish   50.5%  mag_atr=2.6743
```

> When [RSI14_deep_oversold + EMA50_above_EMA100 + breakout_down] occurs, price historically reacts BULLISH 58.9% of the time with an average move of 2.74 ATR (high variance) and stable repetition across validation splits.

---

## #27 — `RSI14_oversold + RSI14_deep_oversold + EMA50_above_EMA100 + breakout_down`

| Field | Value |
|---|---|
| Consistency Score | **0.5593** |
| Match Count | 739 |
| Dominant Direction | BULLISH |
| Direction % | 58.9% |
| Mag ATR Mean | 2.7378 |
| Mag ATR Std | 1.7376 |
| Mag CV | 0.6347 |
| Timing (candles) | 3.61 |
| Persistence | 3.08 |
| Frequency | 0.1591% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    422 samples  bullish   61.6%  mag_atr=2.8871
    val      129 samples  bullish   62.0%  mag_atr=2.3418
    oos      188 samples  bullish   50.5%  mag_atr=2.6743
```

> When [RSI14_oversold + RSI14_deep_oversold + EMA50_above_EMA100 + breakout_down] occurs, price historically reacts BULLISH 58.9% of the time with an average move of 2.74 ATR (high variance) and stable repetition across validation splits.

---

## #28 — `RSI14_deep_oversold + RSI7_oversold + EMA50_above_EMA100 + breakout_down`

| Field | Value |
|---|---|
| Consistency Score | **0.5593** |
| Match Count | 739 |
| Dominant Direction | BULLISH |
| Direction % | 58.9% |
| Mag ATR Mean | 2.7378 |
| Mag ATR Std | 1.7376 |
| Mag CV | 0.6347 |
| Timing (candles) | 3.61 |
| Persistence | 3.08 |
| Frequency | 0.1591% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    422 samples  bullish   61.6%  mag_atr=2.8871
    val      129 samples  bullish   62.0%  mag_atr=2.3418
    oos      188 samples  bullish   50.5%  mag_atr=2.6743
```

> When [RSI14_deep_oversold + RSI7_oversold + EMA50_above_EMA100 + breakout_down] occurs, price historically reacts BULLISH 58.9% of the time with an average move of 2.74 ATR (high variance) and stable repetition across validation splits.

---

## #29 — `RSI14_oversold + RSI14_deep_oversold + RSI7_oversold + EMA50_above_EMA100 + breakout_down`

| Field | Value |
|---|---|
| Consistency Score | **0.5593** |
| Match Count | 739 |
| Dominant Direction | BULLISH |
| Direction % | 58.9% |
| Mag ATR Mean | 2.7378 |
| Mag ATR Std | 1.7376 |
| Mag CV | 0.6347 |
| Timing (candles) | 3.61 |
| Persistence | 3.08 |
| Frequency | 0.1591% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    422 samples  bullish   61.6%  mag_atr=2.8871
    val      129 samples  bullish   62.0%  mag_atr=2.3418
    oos      188 samples  bullish   50.5%  mag_atr=2.6743
```

> When [RSI14_oversold + RSI14_deep_oversold + RSI7_oversold + EMA50_above_EMA100 + breakout_down] occurs, price historically reacts BULLISH 58.9% of the time with an average move of 2.74 ATR (high variance) and stable repetition across validation splits.

---

## #30 — `RSI7_oversold + EMA21_above_EMA50 + MACD_bull_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.5592** |
| Match Count | 748 |
| Dominant Direction | BULLISH |
| Direction % | 56.8% |
| Mag ATR Mean | 1.8548 |
| Mag ATR Std | 1.1257 |
| Mag CV | 0.6069 |
| Timing (candles) | 3.62 |
| Persistence | 2.93 |
| Frequency | 0.1611% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    491 samples  bullish   57.8%  mag_atr=1.8361
    val      116 samples  bullish   61.2%  mag_atr=1.8246
    oos      141 samples  bullish   49.6%  mag_atr=1.9449
```

> When [RSI7_oversold + EMA21_above_EMA50 + MACD_bull_cross] occurs, price historically reacts BULLISH 56.8% of the time with an average move of 1.85 ATR (high variance) and stable repetition across validation splits.

---

## #31 — `RSI14_deep_oversold + EMA50_above_EMA100 + breakout_down + CCI14_oversold`

| Field | Value |
|---|---|
| Consistency Score | **0.5592** |
| Match Count | 676 |
| Dominant Direction | BULLISH |
| Direction % | 58.4% |
| Mag ATR Mean | 2.7897 |
| Mag ATR Std | 1.7437 |
| Mag CV | 0.625 |
| Timing (candles) | 3.59 |
| Persistence | 3.08 |
| Frequency | 0.1456% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    396 samples  bullish   60.6%  mag_atr=2.8963
    val      115 samples  bullish   60.0%  mag_atr=2.4226
    oos      165 samples  bullish   52.1%  mag_atr=2.7896
```

> When [RSI14_deep_oversold + EMA50_above_EMA100 + breakout_down + CCI14_oversold] occurs, price historically reacts BULLISH 58.4% of the time with an average move of 2.79 ATR (high variance) and stable repetition across validation splits.

---

## #32 — `RSI14_oversold + RSI14_deep_oversold + EMA50_above_EMA100 + breakout_down + CCI14_oversold`

| Field | Value |
|---|---|
| Consistency Score | **0.5592** |
| Match Count | 676 |
| Dominant Direction | BULLISH |
| Direction % | 58.4% |
| Mag ATR Mean | 2.7897 |
| Mag ATR Std | 1.7437 |
| Mag CV | 0.625 |
| Timing (candles) | 3.59 |
| Persistence | 3.08 |
| Frequency | 0.1456% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    396 samples  bullish   60.6%  mag_atr=2.8963
    val      115 samples  bullish   60.0%  mag_atr=2.4226
    oos      165 samples  bullish   52.1%  mag_atr=2.7896
```

> When [RSI14_oversold + RSI14_deep_oversold + EMA50_above_EMA100 + breakout_down + CCI14_oversold] occurs, price historically reacts BULLISH 58.4% of the time with an average move of 2.79 ATR (high variance) and stable repetition across validation splits.

---

## #33 — `RSI14_oversold + RSI7_oversold + EMA21_below_EMA50 + EMA50_above_EMA100 + close_above_EMA200`

| Field | Value |
|---|---|
| Consistency Score | **0.5592** |
| Match Count | 610 |
| Dominant Direction | BULLISH |
| Direction % | 57.0% |
| Mag ATR Mean | 2.3672 |
| Mag ATR Std | 1.4238 |
| Mag CV | 0.6015 |
| Timing (candles) | 3.51 |
| Persistence | 2.94 |
| Frequency | 0.1314% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    396 samples  bullish   58.8%  mag_atr=2.5366
    val       96 samples  bullish   53.1%  mag_atr=2.0392
    oos      118 samples  bullish   54.2%  mag_atr=2.0654
```

> When [RSI14_oversold + RSI7_oversold + EMA21_below_EMA50 + EMA50_above_EMA100 + close_above_EMA200] occurs, price historically reacts BULLISH 57.0% of the time with an average move of 2.37 ATR (high variance) and stable repetition across validation splits.

---

## #34 — `RSI14_deep_oversold + RSI7_oversold + EMA50_above_EMA100 + breakout_down + CCI14_oversold`

| Field | Value |
|---|---|
| Consistency Score | **0.5592** |
| Match Count | 676 |
| Dominant Direction | BULLISH |
| Direction % | 58.4% |
| Mag ATR Mean | 2.7897 |
| Mag ATR Std | 1.7437 |
| Mag CV | 0.625 |
| Timing (candles) | 3.59 |
| Persistence | 3.08 |
| Frequency | 0.1456% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    396 samples  bullish   60.6%  mag_atr=2.8963
    val      115 samples  bullish   60.0%  mag_atr=2.4226
    oos      165 samples  bullish   52.1%  mag_atr=2.7896
```

> When [RSI14_deep_oversold + RSI7_oversold + EMA50_above_EMA100 + breakout_down + CCI14_oversold] occurs, price historically reacts BULLISH 58.4% of the time with an average move of 2.79 ATR (high variance) and stable repetition across validation splits.

---

## #35 — `RSI14_deep_oversold + EMA21_below_EMA50 + EMA50_above_EMA100 + close_below_EMA200 + breakout_down`

| Field | Value |
|---|---|
| Consistency Score | **0.5592** |
| Match Count | 560 |
| Dominant Direction | BULLISH |
| Direction % | 57.9% |
| Mag ATR Mean | 2.6358 |
| Mag ATR Std | 1.6065 |
| Mag CV | 0.6095 |
| Timing (candles) | 3.64 |
| Persistence | 3.07 |
| Frequency | 0.1206% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    321 samples  bullish   60.4%  mag_atr=2.7584
    val      104 samples  bullish   61.5%  mag_atr=2.3003
    oos      135 samples  bullish   48.9%  mag_atr=2.6026
```

> When [RSI14_deep_oversold + EMA21_below_EMA50 + EMA50_above_EMA100 + close_below_EMA200 + breakout_down] occurs, price historically reacts BULLISH 57.9% of the time with an average move of 2.64 ATR (high variance) and stable repetition across validation splits.

---

## #36 — `RSI14_deep_oversold + EMA50_above_EMA100 + MACD_bear_cross + breakout_down + CCI14_oversold`

| Field | Value |
|---|---|
| Consistency Score | **0.5592** |
| Match Count | 676 |
| Dominant Direction | BULLISH |
| Direction % | 58.4% |
| Mag ATR Mean | 2.7897 |
| Mag ATR Std | 1.7437 |
| Mag CV | 0.625 |
| Timing (candles) | 3.59 |
| Persistence | 3.08 |
| Frequency | 0.1456% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    396 samples  bullish   60.6%  mag_atr=2.8963
    val      115 samples  bullish   60.0%  mag_atr=2.4226
    oos      165 samples  bullish   52.1%  mag_atr=2.7896
```

> When [RSI14_deep_oversold + EMA50_above_EMA100 + MACD_bear_cross + breakout_down + CCI14_oversold] occurs, price historically reacts BULLISH 58.4% of the time with an average move of 2.79 ATR (high variance) and stable repetition across validation splits.

---

## #37 — `RSI14_oversold + EMA21_below_EMA50 + close_above_EMA200`

| Field | Value |
|---|---|
| Consistency Score | **0.5591** |
| Match Count | 613 |
| Dominant Direction | BULLISH |
| Direction % | 57.1% |
| Mag ATR Mean | 2.3713 |
| Mag ATR Std | 1.429 |
| Mag CV | 0.6026 |
| Timing (candles) | 3.51 |
| Persistence | 2.94 |
| Frequency | 0.132% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    396 samples  bullish   58.8%  mag_atr=2.5366
    val       96 samples  bullish   53.1%  mag_atr=2.0392
    oos      121 samples  bullish   54.5%  mag_atr=2.0937
```

> When [RSI14_oversold + EMA21_below_EMA50 + close_above_EMA200] occurs, price historically reacts BULLISH 57.1% of the time with an average move of 2.37 ATR (high variance) and stable repetition across validation splits.

---

## #38 — `RSI14_oversold + EMA21_below_EMA50 + close_above_EMA200 + MACD_bear_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.5591** |
| Match Count | 587 |
| Dominant Direction | BULLISH |
| Direction % | 57.2% |
| Mag ATR Mean | 2.3688 |
| Mag ATR Std | 1.4276 |
| Mag CV | 0.6027 |
| Timing (candles) | 3.5 |
| Persistence | 2.94 |
| Frequency | 0.1264% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    379 samples  bullish   59.4%  mag_atr=2.524
    val       93 samples  bullish   51.6%  mag_atr=2.0532
    oos      115 samples  bullish   54.8%  mag_atr=2.1124
```

> When [RSI14_oversold + EMA21_below_EMA50 + close_above_EMA200 + MACD_bear_cross] occurs, price historically reacts BULLISH 57.2% of the time with an average move of 2.37 ATR (high variance) and stable repetition across validation splits.

---

## #39 — `RSI14_oversold + RSI7_oversold + EMA21_below_EMA50 + close_above_EMA200 + MACD_bear_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.5591** |
| Match Count | 587 |
| Dominant Direction | BULLISH |
| Direction % | 57.2% |
| Mag ATR Mean | 2.3688 |
| Mag ATR Std | 1.4276 |
| Mag CV | 0.6027 |
| Timing (candles) | 3.5 |
| Persistence | 2.94 |
| Frequency | 0.1264% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    379 samples  bullish   59.4%  mag_atr=2.524
    val       93 samples  bullish   51.6%  mag_atr=2.0532
    oos      115 samples  bullish   54.8%  mag_atr=2.1124
```

> When [RSI14_oversold + RSI7_oversold + EMA21_below_EMA50 + close_above_EMA200 + MACD_bear_cross] occurs, price historically reacts BULLISH 57.2% of the time with an average move of 2.37 ATR (high variance) and stable repetition across validation splits.

---

## #40 — `RSI14_deep_oversold + EMA50_above_EMA100 + MACD_bear_cross + breakout_down`

| Field | Value |
|---|---|
| Consistency Score | **0.5588** |
| Match Count | 732 |
| Dominant Direction | BULLISH |
| Direction % | 58.7% |
| Mag ATR Mean | 2.7456 |
| Mag ATR Std | 1.7418 |
| Mag CV | 0.6344 |
| Timing (candles) | 3.61 |
| Persistence | 3.09 |
| Frequency | 0.1576% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    419 samples  bullish   61.6%  mag_atr=2.8946
    val      128 samples  bullish   61.7%  mag_atr=2.3308
    oos      185 samples  bullish   50.3%  mag_atr=2.6953
```

> When [RSI14_deep_oversold + EMA50_above_EMA100 + MACD_bear_cross + breakout_down] occurs, price historically reacts BULLISH 58.7% of the time with an average move of 2.75 ATR (high variance) and stable repetition across validation splits.

---

## #41 — `RSI14_oversold + RSI14_deep_oversold + EMA50_above_EMA100 + MACD_bear_cross + breakout_down`

| Field | Value |
|---|---|
| Consistency Score | **0.5588** |
| Match Count | 732 |
| Dominant Direction | BULLISH |
| Direction % | 58.7% |
| Mag ATR Mean | 2.7456 |
| Mag ATR Std | 1.7418 |
| Mag CV | 0.6344 |
| Timing (candles) | 3.61 |
| Persistence | 3.09 |
| Frequency | 0.1576% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    419 samples  bullish   61.6%  mag_atr=2.8946
    val      128 samples  bullish   61.7%  mag_atr=2.3308
    oos      185 samples  bullish   50.3%  mag_atr=2.6953
```

> When [RSI14_oversold + RSI14_deep_oversold + EMA50_above_EMA100 + MACD_bear_cross + breakout_down] occurs, price historically reacts BULLISH 58.7% of the time with an average move of 2.75 ATR (high variance) and stable repetition across validation splits.

---

## #42 — `RSI14_deep_oversold + RSI7_oversold + EMA50_above_EMA100 + MACD_bear_cross + breakout_down`

| Field | Value |
|---|---|
| Consistency Score | **0.5588** |
| Match Count | 732 |
| Dominant Direction | BULLISH |
| Direction % | 58.7% |
| Mag ATR Mean | 2.7456 |
| Mag ATR Std | 1.7418 |
| Mag CV | 0.6344 |
| Timing (candles) | 3.61 |
| Persistence | 3.09 |
| Frequency | 0.1576% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    419 samples  bullish   61.6%  mag_atr=2.8946
    val      128 samples  bullish   61.7%  mag_atr=2.3308
    oos      185 samples  bullish   50.3%  mag_atr=2.6953
```

> When [RSI14_deep_oversold + RSI7_oversold + EMA50_above_EMA100 + MACD_bear_cross + breakout_down] occurs, price historically reacts BULLISH 58.7% of the time with an average move of 2.75 ATR (high variance) and stable repetition across validation splits.

---

## #43 — `EMA21_below_EMA50 + close_above_EMA200 + MACD_bear_cross + vol_spike_1x5 + breakout_down`

| Field | Value |
|---|---|
| Consistency Score | **0.5587** |
| Match Count | 511 |
| Dominant Direction | BULLISH |
| Direction % | 58.7% |
| Mag ATR Mean | 2.503 |
| Mag ATR Std | 1.5525 |
| Mag CV | 0.6203 |
| Timing (candles) | 3.49 |
| Persistence | 2.9 |
| Frequency | 0.11% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    330 samples  bullish   61.5%  mag_atr=2.5237
    val       82 samples  bullish   59.8%  mag_atr=2.4601
    oos       99 samples  bullish   48.5%  mag_atr=2.4697
```

> When [EMA21_below_EMA50 + close_above_EMA200 + MACD_bear_cross + vol_spike_1x5 + breakout_down] occurs, price historically reacts BULLISH 58.7% of the time with an average move of 2.50 ATR (high variance) and stable repetition across validation splits.

---

## #44 — `RSI14_oversold + RSI7_oversold + EMA21_below_EMA50 + close_above_EMA200`

| Field | Value |
|---|---|
| Consistency Score | **0.5585** |
| Match Count | 611 |
| Dominant Direction | BULLISH |
| Direction % | 57.0% |
| Mag ATR Mean | 2.3734 |
| Mag ATR Std | 1.4309 |
| Mag CV | 0.6029 |
| Timing (candles) | 3.51 |
| Persistence | 2.94 |
| Frequency | 0.1316% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    396 samples  bullish   58.8%  mag_atr=2.5366
    val       96 samples  bullish   53.1%  mag_atr=2.0392
    oos      119 samples  bullish   53.8%  mag_atr=2.0997
```

> When [RSI14_oversold + RSI7_oversold + EMA21_below_EMA50 + close_above_EMA200] occurs, price historically reacts BULLISH 57.0% of the time with an average move of 2.37 ATR (high variance) and stable repetition across validation splits.

---

## #45 — `RSI14_deep_oversold + ADX_trending + EMA50_above_EMA100 + close_below_EMA200 + breakout_down`

| Field | Value |
|---|---|
| Consistency Score | **0.5583** |
| Match Count | 462 |
| Dominant Direction | BULLISH |
| Direction % | 59.7% |
| Mag ATR Mean | 2.6265 |
| Mag ATR Std | 1.6622 |
| Mag CV | 0.6329 |
| Timing (candles) | 3.68 |
| Persistence | 3.15 |
| Frequency | 0.0995% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    260 samples  bullish   61.9%  mag_atr=2.8337
    val       85 samples  bullish   64.7%  mag_atr=2.1256
    oos      117 samples  bullish   51.3%  mag_atr=2.5302
```

> When [RSI14_deep_oversold + ADX_trending + EMA50_above_EMA100 + close_below_EMA200 + breakout_down] occurs, price historically reacts BULLISH 59.7% of the time with an average move of 2.63 ATR (high variance) and stable repetition across validation splits.

---

## #46 — `RSI14_deep_oversold + EMA21_below_EMA50 + EMA50_above_EMA100 + breakout_down`

| Field | Value |
|---|---|
| Consistency Score | **0.5580** |
| Match Count | 622 |
| Dominant Direction | BULLISH |
| Direction % | 58.0% |
| Mag ATR Mean | 2.6503 |
| Mag ATR Std | 1.6453 |
| Mag CV | 0.6208 |
| Timing (candles) | 3.62 |
| Persistence | 3.06 |
| Frequency | 0.1339% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    358 samples  bullish   60.9%  mag_atr=2.7976
    val      109 samples  bullish   61.5%  mag_atr=2.2742
    oos      155 samples  bullish   49.0%  mag_atr=2.5744
```

> When [RSI14_deep_oversold + EMA21_below_EMA50 + EMA50_above_EMA100 + breakout_down] occurs, price historically reacts BULLISH 58.0% of the time with an average move of 2.65 ATR (high variance) and stable repetition across validation splits.

---

## #47 — `RSI14_oversold + RSI14_deep_oversold + EMA21_below_EMA50 + EMA50_above_EMA100 + breakout_down`

| Field | Value |
|---|---|
| Consistency Score | **0.5580** |
| Match Count | 622 |
| Dominant Direction | BULLISH |
| Direction % | 58.0% |
| Mag ATR Mean | 2.6503 |
| Mag ATR Std | 1.6453 |
| Mag CV | 0.6208 |
| Timing (candles) | 3.62 |
| Persistence | 3.06 |
| Frequency | 0.1339% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    358 samples  bullish   60.9%  mag_atr=2.7976
    val      109 samples  bullish   61.5%  mag_atr=2.2742
    oos      155 samples  bullish   49.0%  mag_atr=2.5744
```

> When [RSI14_oversold + RSI14_deep_oversold + EMA21_below_EMA50 + EMA50_above_EMA100 + breakout_down] occurs, price historically reacts BULLISH 58.0% of the time with an average move of 2.65 ATR (high variance) and stable repetition across validation splits.

---

## #48 — `RSI14_deep_oversold + RSI7_oversold + EMA21_below_EMA50 + EMA50_above_EMA100 + breakout_down`

| Field | Value |
|---|---|
| Consistency Score | **0.5580** |
| Match Count | 622 |
| Dominant Direction | BULLISH |
| Direction % | 58.0% |
| Mag ATR Mean | 2.6503 |
| Mag ATR Std | 1.6453 |
| Mag CV | 0.6208 |
| Timing (candles) | 3.62 |
| Persistence | 3.06 |
| Frequency | 0.1339% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    358 samples  bullish   60.9%  mag_atr=2.7976
    val      109 samples  bullish   61.5%  mag_atr=2.2742
    oos      155 samples  bullish   49.0%  mag_atr=2.5744
```

> When [RSI14_deep_oversold + RSI7_oversold + EMA21_below_EMA50 + EMA50_above_EMA100 + breakout_down] occurs, price historically reacts BULLISH 58.0% of the time with an average move of 2.65 ATR (high variance) and stable repetition across validation splits.

---

## #49 — `RSI7_oversold + EMA21_above_EMA50 + EMA50_above_EMA100 + MACD_bull_cross + breakout_down`

| Field | Value |
|---|---|
| Consistency Score | **0.5579** |
| Match Count | 277 |
| Dominant Direction | BULLISH |
| Direction % | 61.4% |
| Mag ATR Mean | 1.9875 |
| Mag ATR Std | 1.2832 |
| Mag CV | 0.6456 |
| Timing (candles) | 3.71 |
| Persistence | 3.01 |
| Frequency | 0.0597% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    175 samples  bullish   61.1%  mag_atr=1.959
    val       45 samples  bullish   68.9%  mag_atr=1.9225
    oos       57 samples  bullish   56.1%  mag_atr=2.1261
```

> When [RSI7_oversold + EMA21_above_EMA50 + EMA50_above_EMA100 + MACD_bull_cross + breakout_down] occurs, price historically reacts BULLISH 61.4% of the time with an average move of 1.99 ATR (high variance) and stable repetition across validation splits.

---

## #50 — `EMA21_below_EMA50 + EMA50_above_EMA100 + close_above_EMA200 + vol_spike_1x5 + breakout_down`

| Field | Value |
|---|---|
| Consistency Score | **0.5579** |
| Match Count | 521 |
| Dominant Direction | BULLISH |
| Direction % | 58.4% |
| Mag ATR Mean | 2.4957 |
| Mag ATR Std | 1.5449 |
| Mag CV | 0.619 |
| Timing (candles) | 3.48 |
| Persistence | 2.9 |
| Frequency | 0.1122% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    338 samples  bullish   61.0%  mag_atr=2.5241
    val       83 samples  bullish   59.0%  mag_atr=2.4577
    oos      100 samples  bullish   49.0%  mag_atr=2.4316
```

> When [EMA21_below_EMA50 + EMA50_above_EMA100 + close_above_EMA200 + vol_spike_1x5 + breakout_down] occurs, price historically reacts BULLISH 58.4% of the time with an average move of 2.50 ATR (high variance) and stable repetition across validation splits.

---
