# Market Condition Analysis Report

**Lookahead:** 5 candles  
**Min direction:** 65.0%  
**Max mag CV:** 0.85  

---

## #1 — `close_above_BB_UPPER_20_2 + MACD_9_21_bear_cross + ATR7_above_ATR13`

| Field | Value |
|---|---|
| Consistency Score | **0.6586** |
| Match Count | 97 |
| Dominant Direction | BULLISH |
| Direction % | 66.0% |
| Mag ATR Mean | 2.2553 |
| Mag ATR Std | 1.0836 |
| Mag CV | 0.4805 |
| Timing (candles) | 4.05 |
| Persistence | 3.23 |
| Frequency | 1.667% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     57 samples  bullish   66.7%  mag_atr=2.2384
    val       24 samples  bullish   62.5%  mag_atr=2.4335
    oos       16 samples  bullish   68.8%  mag_atr=2.0482
```

> When [close_above_BB_UPPER_20_2 + MACD_9_21_bear_cross + ATR7_above_ATR13] occurs, price historically reacts BULLISH 66.0% of the time with an average move of 2.26 ATR (moderate variance) and stable repetition across validation splits.

---

## #2 — `STO_K_14_oversold + ADX_strong_trend + EMA21_above_Close`

| Field | Value |
|---|---|
| Consistency Score | **0.6451** |
| Match Count | 106 |
| Dominant Direction | BULLISH |
| Direction % | 65.1% |
| Mag ATR Mean | 1.9482 |
| Mag ATR Std | 1.1598 |
| Mag CV | 0.5953 |
| Timing (candles) | 3.62 |
| Persistence | 3.34 |
| Frequency | 1.8216% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     51 samples  bullish   66.7%  mag_atr=2.3333
    val       23 samples  bullish   69.6%  mag_atr=1.843
    oos       32 samples  bullish   59.4%  mag_atr=1.4101
```

> When [STO_K_14_oversold + ADX_strong_trend + EMA21_above_Close] occurs, price historically reacts BULLISH 65.1% of the time with an average move of 1.95 ATR (moderate variance) and stable repetition across validation splits.

---

## #3 — `STO_K_14_oversold + ADX_strong_trend + close_below_EMA21`

| Field | Value |
|---|---|
| Consistency Score | **0.6451** |
| Match Count | 106 |
| Dominant Direction | BULLISH |
| Direction % | 65.1% |
| Mag ATR Mean | 1.9482 |
| Mag ATR Std | 1.1598 |
| Mag CV | 0.5953 |
| Timing (candles) | 3.62 |
| Persistence | 3.34 |
| Frequency | 1.8216% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     51 samples  bullish   66.7%  mag_atr=2.3333
    val       23 samples  bullish   69.6%  mag_atr=1.843
    oos       32 samples  bullish   59.4%  mag_atr=1.4101
```

> When [STO_K_14_oversold + ADX_strong_trend + close_below_EMA21] occurs, price historically reacts BULLISH 65.1% of the time with an average move of 1.95 ATR (moderate variance) and stable repetition across validation splits.

---

## #4 — `STO_K_21_oversold + EMA50_above_EMA200 + MACD_12_26_bull_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.6380** |
| Match Count | 67 |
| Dominant Direction | BULLISH |
| Direction % | 73.1% |
| Mag ATR Mean | 1.8973 |
| Mag ATR Std | 0.7936 |
| Mag CV | 0.4183 |
| Timing (candles) | 3.93 |
| Persistence | 3.87 |
| Frequency | 1.1514% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     36 samples  bullish   80.6%  mag_atr=2.0694
    val       14 samples  bullish   71.4%  mag_atr=1.5633
    oos       17 samples  bullish   58.8%  mag_atr=1.8079
```

> When [STO_K_21_oversold + EMA50_above_EMA200 + MACD_12_26_bull_cross] occurs, price historically reacts BULLISH 73.1% of the time with an average move of 1.90 ATR (moderate variance) and stable repetition across validation splits.

---

## #5 — `close_above_BB_UPPER_20_2 + MACD_9_21_bear_cross + ATR14_above_ATR21`

| Field | Value |
|---|---|
| Consistency Score | **0.6332** |
| Match Count | 83 |
| Dominant Direction | BULLISH |
| Direction % | 65.1% |
| Mag ATR Mean | 2.2795 |
| Mag ATR Std | 1.0373 |
| Mag CV | 0.4551 |
| Timing (candles) | 4.02 |
| Persistence | 3.12 |
| Frequency | 1.4264% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     47 samples  bullish   68.1%  mag_atr=2.2869
    val       18 samples  bullish   61.1%  mag_atr=2.1699
    oos       18 samples  bullish   61.1%  mag_atr=2.3698
```

> When [close_above_BB_UPPER_20_2 + MACD_9_21_bear_cross + ATR14_above_ATR21] occurs, price historically reacts BULLISH 65.1% of the time with an average move of 2.28 ATR (moderate variance) and stable repetition across validation splits.

---

## #6 — `STO_K_14_oversold + ADX_strong_trend + EMA13_below_EMA21`

| Field | Value |
|---|---|
| Consistency Score | **0.6329** |
| Match Count | 94 |
| Dominant Direction | BULLISH |
| Direction % | 69.2% |
| Mag ATR Mean | 1.9988 |
| Mag ATR Std | 1.2053 |
| Mag CV | 0.603 |
| Timing (candles) | 3.61 |
| Persistence | 3.47 |
| Frequency | 1.6154% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     45 samples  bullish   73.3%  mag_atr=2.4491
    val       22 samples  bullish   68.2%  mag_atr=1.8157
    oos       27 samples  bullish   63.0%  mag_atr=1.3974
```

> When [STO_K_14_oversold + ADX_strong_trend + EMA13_below_EMA21] occurs, price historically reacts BULLISH 69.2% of the time with an average move of 2.00 ATR (high variance) and stable repetition across validation splits.

---

## #7 — `STO_K_14_oversold + STO_K_21_oversold + ADX_strong_trend`

| Field | Value |
|---|---|
| Consistency Score | **0.6305** |
| Match Count | 98 |
| Dominant Direction | BULLISH |
| Direction % | 66.3% |
| Mag ATR Mean | 1.967 |
| Mag ATR Std | 1.1919 |
| Mag CV | 0.6059 |
| Timing (candles) | 3.61 |
| Persistence | 3.37 |
| Frequency | 1.6841% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     48 samples  bullish   68.8%  mag_atr=2.3818
    val       22 samples  bullish   68.2%  mag_atr=1.8157
    oos       28 samples  bullish   60.7%  mag_atr=1.3749
```

> When [STO_K_14_oversold + STO_K_21_oversold + ADX_strong_trend] occurs, price historically reacts BULLISH 66.3% of the time with an average move of 1.97 ATR (high variance) and stable repetition across validation splits.

---

## #8 — `STO_K_14_oversold + ADX_strong_trend + EMA21_below_EMA50`

| Field | Value |
|---|---|
| Consistency Score | **0.6294** |
| Match Count | 91 |
| Dominant Direction | BULLISH |
| Direction % | 69.2% |
| Mag ATR Mean | 2.0344 |
| Mag ATR Std | 1.2076 |
| Mag CV | 0.5936 |
| Timing (candles) | 3.64 |
| Persistence | 3.47 |
| Frequency | 1.5638% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     45 samples  bullish   73.3%  mag_atr=2.4491
    val       22 samples  bullish   68.2%  mag_atr=1.8157
    oos       24 samples  bullish   62.5%  mag_atr=1.4572
```

> When [STO_K_14_oversold + ADX_strong_trend + EMA21_below_EMA50] occurs, price historically reacts BULLISH 69.2% of the time with an average move of 2.03 ATR (moderate variance) and stable repetition across validation splits.

---

## #9 — `STO_K_21_oversold + EMA50_above_EMA200 + MACD_9_21_bull_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.6236** |
| Match Count | 60 |
| Dominant Direction | BULLISH |
| Direction % | 73.3% |
| Mag ATR Mean | 1.8957 |
| Mag ATR Std | 0.7994 |
| Mag CV | 0.4217 |
| Timing (candles) | 3.88 |
| Persistence | 3.93 |
| Frequency | 1.0311% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     35 samples  bullish   80.0%  mag_atr=2.0633
    val       10 samples  bullish   70.0%  mag_atr=1.6309
    oos       15 samples  bullish   60.0%  mag_atr=1.681
```

> When [STO_K_21_oversold + EMA50_above_EMA200 + MACD_9_21_bull_cross] occurs, price historically reacts BULLISH 73.3% of the time with an average move of 1.90 ATR (moderate variance) and stable repetition across validation splits.

---

## #10 — `close_above_BB_UPPER_20_2 + MACD_8_21_bear_cross + ATR7_above_ATR13`

| Field | Value |
|---|---|
| Consistency Score | **0.6196** |
| Match Count | 73 |
| Dominant Direction | BULLISH |
| Direction % | 68.5% |
| Mag ATR Mean | 2.2419 |
| Mag ATR Std | 1.067 |
| Mag CV | 0.4759 |
| Timing (candles) | 4.14 |
| Persistence | 3.22 |
| Frequency | 1.2545% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     46 samples  bullish   67.4%  mag_atr=2.2793
    val       14 samples  bullish   57.1%  mag_atr=2.2078
    oos       13 samples  bullish   84.6%  mag_atr=2.1462
```

> When [close_above_BB_UPPER_20_2 + MACD_8_21_bear_cross + ATR7_above_ATR13] occurs, price historically reacts BULLISH 68.5% of the time with an average move of 2.24 ATR (moderate variance) and stable repetition across validation splits.

---

## #11 — `RSI13_oversold + ADX_strong_trend`

| Field | Value |
|---|---|
| Consistency Score | **0.6078** |
| Match Count | 82 |
| Dominant Direction | BULLISH |
| Direction % | 67.1% |
| Mag ATR Mean | 1.9735 |
| Mag ATR Std | 1.1382 |
| Mag CV | 0.5767 |
| Timing (candles) | 3.39 |
| Persistence | 3.44 |
| Frequency | 1.4092% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     44 samples  bullish   68.2%  mag_atr=2.2142
    val       21 samples  bullish   66.7%  mag_atr=1.8596
    oos       17 samples  bullish   64.7%  mag_atr=1.4912
```

> When [RSI13_oversold + ADX_strong_trend] occurs, price historically reacts BULLISH 67.1% of the time with an average move of 1.97 ATR (moderate variance) and stable repetition across validation splits.

---

## #12 — `RSI13_oversold + ADX_trending + ADX_strong_trend`

| Field | Value |
|---|---|
| Consistency Score | **0.6078** |
| Match Count | 82 |
| Dominant Direction | BULLISH |
| Direction % | 67.1% |
| Mag ATR Mean | 1.9735 |
| Mag ATR Std | 1.1382 |
| Mag CV | 0.5767 |
| Timing (candles) | 3.39 |
| Persistence | 3.44 |
| Frequency | 1.4092% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     44 samples  bullish   68.2%  mag_atr=2.2142
    val       21 samples  bullish   66.7%  mag_atr=1.8596
    oos       17 samples  bullish   64.7%  mag_atr=1.4912
```

> When [RSI13_oversold + ADX_trending + ADX_strong_trend] occurs, price historically reacts BULLISH 67.1% of the time with an average move of 1.97 ATR (moderate variance) and stable repetition across validation splits.

---

## #13 — `RSI13_oversold + ADX_strong_trend + EMA13_below_EMA21`

| Field | Value |
|---|---|
| Consistency Score | **0.6078** |
| Match Count | 82 |
| Dominant Direction | BULLISH |
| Direction % | 67.1% |
| Mag ATR Mean | 1.9735 |
| Mag ATR Std | 1.1382 |
| Mag CV | 0.5767 |
| Timing (candles) | 3.39 |
| Persistence | 3.44 |
| Frequency | 1.4092% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     44 samples  bullish   68.2%  mag_atr=2.2142
    val       21 samples  bullish   66.7%  mag_atr=1.8596
    oos       17 samples  bullish   64.7%  mag_atr=1.4912
```

> When [RSI13_oversold + ADX_strong_trend + EMA13_below_EMA21] occurs, price historically reacts BULLISH 67.1% of the time with an average move of 1.97 ATR (moderate variance) and stable repetition across validation splits.

---

## #14 — `RSI13_oversold + ADX_strong_trend + EMA21_above_Close`

| Field | Value |
|---|---|
| Consistency Score | **0.6078** |
| Match Count | 82 |
| Dominant Direction | BULLISH |
| Direction % | 67.1% |
| Mag ATR Mean | 1.9735 |
| Mag ATR Std | 1.1382 |
| Mag CV | 0.5767 |
| Timing (candles) | 3.39 |
| Persistence | 3.44 |
| Frequency | 1.4092% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     44 samples  bullish   68.2%  mag_atr=2.2142
    val       21 samples  bullish   66.7%  mag_atr=1.8596
    oos       17 samples  bullish   64.7%  mag_atr=1.4912
```

> When [RSI13_oversold + ADX_strong_trend + EMA21_above_Close] occurs, price historically reacts BULLISH 67.1% of the time with an average move of 1.97 ATR (moderate variance) and stable repetition across validation splits.

---

## #15 — `RSI13_oversold + ADX_strong_trend + close_below_EMA21`

| Field | Value |
|---|---|
| Consistency Score | **0.6078** |
| Match Count | 82 |
| Dominant Direction | BULLISH |
| Direction % | 67.1% |
| Mag ATR Mean | 1.9735 |
| Mag ATR Std | 1.1382 |
| Mag CV | 0.5767 |
| Timing (candles) | 3.39 |
| Persistence | 3.44 |
| Frequency | 1.4092% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     44 samples  bullish   68.2%  mag_atr=2.2142
    val       21 samples  bullish   66.7%  mag_atr=1.8596
    oos       17 samples  bullish   64.7%  mag_atr=1.4912
```

> When [RSI13_oversold + ADX_strong_trend + close_below_EMA21] occurs, price historically reacts BULLISH 67.1% of the time with an average move of 1.97 ATR (moderate variance) and stable repetition across validation splits.

---

## #16 — `RSI14_oversold + ADX_strong_trend`

| Field | Value |
|---|---|
| Consistency Score | **0.6072** |
| Match Count | 79 |
| Dominant Direction | BULLISH |
| Direction % | 68.3% |
| Mag ATR Mean | 2.0048 |
| Mag ATR Std | 1.1478 |
| Mag CV | 0.5725 |
| Timing (candles) | 3.39 |
| Persistence | 3.44 |
| Frequency | 1.3576% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     43 samples  bullish   67.4%  mag_atr=2.2353
    val       20 samples  bullish   70.0%  mag_atr=1.9004
    oos       16 samples  bullish   68.8%  mag_atr=1.5158
```

> When [RSI14_oversold + ADX_strong_trend] occurs, price historically reacts BULLISH 68.3% of the time with an average move of 2.00 ATR (moderate variance) and stable repetition across validation splits.

---

## #17 — `RSI13_oversold + RSI14_oversold + ADX_strong_trend`

| Field | Value |
|---|---|
| Consistency Score | **0.6072** |
| Match Count | 79 |
| Dominant Direction | BULLISH |
| Direction % | 68.3% |
| Mag ATR Mean | 2.0048 |
| Mag ATR Std | 1.1478 |
| Mag CV | 0.5725 |
| Timing (candles) | 3.39 |
| Persistence | 3.44 |
| Frequency | 1.3576% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     43 samples  bullish   67.4%  mag_atr=2.2353
    val       20 samples  bullish   70.0%  mag_atr=1.9004
    oos       16 samples  bullish   68.8%  mag_atr=1.5158
```

> When [RSI13_oversold + RSI14_oversold + ADX_strong_trend] occurs, price historically reacts BULLISH 68.3% of the time with an average move of 2.00 ATR (moderate variance) and stable repetition across validation splits.

---

## #18 — `RSI14_oversold + ADX_trending + ADX_strong_trend`

| Field | Value |
|---|---|
| Consistency Score | **0.6072** |
| Match Count | 79 |
| Dominant Direction | BULLISH |
| Direction % | 68.3% |
| Mag ATR Mean | 2.0048 |
| Mag ATR Std | 1.1478 |
| Mag CV | 0.5725 |
| Timing (candles) | 3.39 |
| Persistence | 3.44 |
| Frequency | 1.3576% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     43 samples  bullish   67.4%  mag_atr=2.2353
    val       20 samples  bullish   70.0%  mag_atr=1.9004
    oos       16 samples  bullish   68.8%  mag_atr=1.5158
```

> When [RSI14_oversold + ADX_trending + ADX_strong_trend] occurs, price historically reacts BULLISH 68.3% of the time with an average move of 2.00 ATR (moderate variance) and stable repetition across validation splits.

---

## #19 — `RSI14_oversold + ADX_strong_trend + EMA13_below_EMA21`

| Field | Value |
|---|---|
| Consistency Score | **0.6072** |
| Match Count | 79 |
| Dominant Direction | BULLISH |
| Direction % | 68.3% |
| Mag ATR Mean | 2.0048 |
| Mag ATR Std | 1.1478 |
| Mag CV | 0.5725 |
| Timing (candles) | 3.39 |
| Persistence | 3.44 |
| Frequency | 1.3576% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     43 samples  bullish   67.4%  mag_atr=2.2353
    val       20 samples  bullish   70.0%  mag_atr=1.9004
    oos       16 samples  bullish   68.8%  mag_atr=1.5158
```

> When [RSI14_oversold + ADX_strong_trend + EMA13_below_EMA21] occurs, price historically reacts BULLISH 68.3% of the time with an average move of 2.00 ATR (moderate variance) and stable repetition across validation splits.

---

## #20 — `RSI14_oversold + ADX_strong_trend + EMA21_above_Close`

| Field | Value |
|---|---|
| Consistency Score | **0.6072** |
| Match Count | 79 |
| Dominant Direction | BULLISH |
| Direction % | 68.3% |
| Mag ATR Mean | 2.0048 |
| Mag ATR Std | 1.1478 |
| Mag CV | 0.5725 |
| Timing (candles) | 3.39 |
| Persistence | 3.44 |
| Frequency | 1.3576% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     43 samples  bullish   67.4%  mag_atr=2.2353
    val       20 samples  bullish   70.0%  mag_atr=1.9004
    oos       16 samples  bullish   68.8%  mag_atr=1.5158
```

> When [RSI14_oversold + ADX_strong_trend + EMA21_above_Close] occurs, price historically reacts BULLISH 68.3% of the time with an average move of 2.00 ATR (moderate variance) and stable repetition across validation splits.

---

## #21 — `RSI14_oversold + ADX_strong_trend + close_below_EMA21`

| Field | Value |
|---|---|
| Consistency Score | **0.6072** |
| Match Count | 79 |
| Dominant Direction | BULLISH |
| Direction % | 68.3% |
| Mag ATR Mean | 2.0048 |
| Mag ATR Std | 1.1478 |
| Mag CV | 0.5725 |
| Timing (candles) | 3.39 |
| Persistence | 3.44 |
| Frequency | 1.3576% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     43 samples  bullish   67.4%  mag_atr=2.2353
    val       20 samples  bullish   70.0%  mag_atr=1.9004
    oos       16 samples  bullish   68.8%  mag_atr=1.5158
```

> When [RSI14_oversold + ADX_strong_trend + close_below_EMA21] occurs, price historically reacts BULLISH 68.3% of the time with an average move of 2.00 ATR (moderate variance) and stable repetition across validation splits.

---

## #22 — `RSI14_oversold + ADX_strong_trend + close_below_EMA200`

| Field | Value |
|---|---|
| Consistency Score | **0.6072** |
| Match Count | 79 |
| Dominant Direction | BULLISH |
| Direction % | 68.3% |
| Mag ATR Mean | 2.0048 |
| Mag ATR Std | 1.1478 |
| Mag CV | 0.5725 |
| Timing (candles) | 3.39 |
| Persistence | 3.44 |
| Frequency | 1.3576% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     43 samples  bullish   67.4%  mag_atr=2.2353
    val       20 samples  bullish   70.0%  mag_atr=1.9004
    oos       16 samples  bullish   68.8%  mag_atr=1.5158
```

> When [RSI14_oversold + ADX_strong_trend + close_below_EMA200] occurs, price historically reacts BULLISH 68.3% of the time with an average move of 2.00 ATR (moderate variance) and stable repetition across validation splits.

---

## #23 — `RSI14_overbought + MACD_8_21_bear_cross + CCI14_overbought`

| Field | Value |
|---|---|
| Consistency Score | **0.6069** |
| Match Count | 74 |
| Dominant Direction | BULLISH |
| Direction % | 67.6% |
| Mag ATR Mean | 2.4644 |
| Mag ATR Std | 1.2858 |
| Mag CV | 0.5217 |
| Timing (candles) | 4.04 |
| Persistence | 3.3 |
| Frequency | 1.2717% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     48 samples  bullish   62.5%  mag_atr=2.3659
    val       13 samples  bullish   53.9%  mag_atr=2.836
    oos       13 samples  bullish   100.0%  mag_atr=2.4563
```

> When [RSI14_overbought + MACD_8_21_bear_cross + CCI14_overbought] occurs, price historically reacts BULLISH 67.6% of the time with an average move of 2.46 ATR (moderate variance) and stable repetition across validation splits.

---

## #24 — `RSI13_oversold + ADX_strong_trend + close_below_EMA200`

| Field | Value |
|---|---|
| Consistency Score | **0.6043** |
| Match Count | 81 |
| Dominant Direction | BULLISH |
| Direction % | 66.7% |
| Mag ATR Mean | 1.9817 |
| Mag ATR Std | 1.1428 |
| Mag CV | 0.5767 |
| Timing (candles) | 3.37 |
| Persistence | 3.42 |
| Frequency | 1.392% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     43 samples  bullish   67.4%  mag_atr=2.2353
    val       21 samples  bullish   66.7%  mag_atr=1.8596
    oos       17 samples  bullish   64.7%  mag_atr=1.4912
```

> When [RSI13_oversold + ADX_strong_trend + close_below_EMA200] occurs, price historically reacts BULLISH 66.7% of the time with an average move of 1.98 ATR (moderate variance) and stable repetition across validation splits.

---

## #25 — `close_above_BB_UPPER_20_2 + MACD_8_21_bear_cross + ATR14_above_ATR21`

| Field | Value |
|---|---|
| Consistency Score | **0.6032** |
| Match Count | 61 |
| Dominant Direction | BULLISH |
| Direction % | 68.8% |
| Mag ATR Mean | 2.2365 |
| Mag ATR Std | 1.0031 |
| Mag CV | 0.4485 |
| Timing (candles) | 4.05 |
| Persistence | 3.23 |
| Frequency | 1.0483% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     37 samples  bullish   67.6%  mag_atr=2.3267
    val       10 samples  bullish   60.0%  mag_atr=1.9872
    oos       14 samples  bullish   78.6%  mag_atr=2.1764
```

> When [close_above_BB_UPPER_20_2 + MACD_8_21_bear_cross + ATR14_above_ATR21] occurs, price historically reacts BULLISH 68.8% of the time with an average move of 2.24 ATR (moderate variance) and stable repetition across validation splits.

---

## #26 — `STO_K_14_oversold + ADX_strong_trend + close_below_EMA200`

| Field | Value |
|---|---|
| Consistency Score | **0.6026** |
| Match Count | 87 |
| Dominant Direction | BULLISH |
| Direction % | 65.5% |
| Mag ATR Mean | 1.9999 |
| Mag ATR Std | 1.2331 |
| Mag CV | 0.6166 |
| Timing (candles) | 3.62 |
| Persistence | 3.3 |
| Frequency | 1.4951% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     38 samples  bullish   65.8%  mag_atr=2.5347
    val       22 samples  bullish   68.2%  mag_atr=1.8157
    oos       27 samples  bullish   63.0%  mag_atr=1.3974
```

> When [STO_K_14_oversold + ADX_strong_trend + close_below_EMA200] occurs, price historically reacts BULLISH 65.5% of the time with an average move of 2.00 ATR (high variance) and stable repetition across validation splits.

---

## #27 — `RSI13_oversold + ADX_strong_trend + EMA21_below_EMA50`

| Field | Value |
|---|---|
| Consistency Score | **0.6016** |
| Match Count | 80 |
| Dominant Direction | BULLISH |
| Direction % | 66.2% |
| Mag ATR Mean | 1.9949 |
| Mag ATR Std | 1.1441 |
| Mag CV | 0.5735 |
| Timing (candles) | 3.39 |
| Persistence | 3.4 |
| Frequency | 1.3748% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     44 samples  bullish   68.2%  mag_atr=2.2142
    val       21 samples  bullish   66.7%  mag_atr=1.8596
    oos       15 samples  bullish   60.0%  mag_atr=1.5411
```

> When [RSI13_oversold + ADX_strong_trend + EMA21_below_EMA50] occurs, price historically reacts BULLISH 66.2% of the time with an average move of 1.99 ATR (moderate variance) and stable repetition across validation splits.

---

## #28 — `RSI14_oversold + ADX_strong_trend + EMA21_below_EMA50`

| Field | Value |
|---|---|
| Consistency Score | **0.6012** |
| Match Count | 77 |
| Dominant Direction | BULLISH |
| Direction % | 67.5% |
| Mag ATR Mean | 2.0279 |
| Mag ATR Std | 1.1535 |
| Mag CV | 0.5688 |
| Timing (candles) | 3.39 |
| Persistence | 3.4 |
| Frequency | 1.3233% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     43 samples  bullish   67.4%  mag_atr=2.2353
    val       20 samples  bullish   70.0%  mag_atr=1.9004
    oos       14 samples  bullish   64.3%  mag_atr=1.5728
```

> When [RSI14_oversold + ADX_strong_trend + EMA21_below_EMA50] occurs, price historically reacts BULLISH 67.5% of the time with an average move of 2.03 ATR (moderate variance) and stable repetition across validation splits.

---

## #29 — `STO_K_14_oversold + EMA50_above_EMA200 + MACD_12_26_bull_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.6001** |
| Match Count | 51 |
| Dominant Direction | BULLISH |
| Direction % | 70.6% |
| Mag ATR Mean | 1.7234 |
| Mag ATR Std | 0.6957 |
| Mag CV | 0.4037 |
| Timing (candles) | 3.94 |
| Persistence | 3.75 |
| Frequency | 0.8764% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     23 samples  bullish   78.3%  mag_atr=1.9814
    val       15 samples  bullish   66.7%  mag_atr=1.3893
    oos       13 samples  bullish   61.5%  mag_atr=1.6525
```

> When [STO_K_14_oversold + EMA50_above_EMA200 + MACD_12_26_bull_cross] occurs, price historically reacts BULLISH 70.6% of the time with an average move of 1.72 ATR (moderate variance) and stable repetition across validation splits.

---

## #30 — `RSI7_oversold + STO_K_21_oversold + ADX_strong_trend`

| Field | Value |
|---|---|
| Consistency Score | **0.5974** |
| Match Count | 74 |
| Dominant Direction | BULLISH |
| Direction % | 68.9% |
| Mag ATR Mean | 2.0334 |
| Mag ATR Std | 1.177 |
| Mag CV | 0.5788 |
| Timing (candles) | 3.5 |
| Persistence | 3.34 |
| Frequency | 1.2717% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     35 samples  bullish   77.1%  mag_atr=2.5152
    val       18 samples  bullish   66.7%  mag_atr=1.855
    oos       21 samples  bullish   57.1%  mag_atr=1.3833
```

> When [RSI7_oversold + STO_K_21_oversold + ADX_strong_trend] occurs, price historically reacts BULLISH 68.9% of the time with an average move of 2.03 ATR (moderate variance) and stable repetition across validation splits.

---

## #31 — `RSI14_oversold + ADX_strong_trend + EMA50_below_EMA100`

| Field | Value |
|---|---|
| Consistency Score | **0.5974** |
| Match Count | 75 |
| Dominant Direction | BULLISH |
| Direction % | 68.0% |
| Mag ATR Mean | 2.0338 |
| Mag ATR Std | 1.1676 |
| Mag CV | 0.5741 |
| Timing (candles) | 3.4 |
| Persistence | 3.41 |
| Frequency | 1.2889% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     42 samples  bullish   69.0%  mag_atr=2.24
    val       20 samples  bullish   70.0%  mag_atr=1.9004
    oos       13 samples  bullish   61.5%  mag_atr=1.5731
```

> When [RSI14_oversold + ADX_strong_trend + EMA50_below_EMA100] occurs, price historically reacts BULLISH 68.0% of the time with an average move of 2.03 ATR (moderate variance) and stable repetition across validation splits.

---

## #32 — `RSI13_oversold + ADX_strong_trend + EMA50_below_EMA100`

| Field | Value |
|---|---|
| Consistency Score | **0.5957** |
| Match Count | 76 |
| Dominant Direction | BULLISH |
| Direction % | 67.1% |
| Mag ATR Mean | 2.0208 |
| Mag ATR Std | 1.1653 |
| Mag CV | 0.5767 |
| Timing (candles) | 3.37 |
| Persistence | 3.39 |
| Frequency | 1.3061% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     42 samples  bullish   69.0%  mag_atr=2.24
    val       21 samples  bullish   66.7%  mag_atr=1.8596
    oos       13 samples  bullish   61.5%  mag_atr=1.5731
```

> When [RSI13_oversold + ADX_strong_trend + EMA50_below_EMA100] occurs, price historically reacts BULLISH 67.1% of the time with an average move of 2.02 ATR (moderate variance) and stable repetition across validation splits.

---

## #33 — `RSI14_oversold + STO_K_21_oversold + ADX_strong_trend`

| Field | Value |
|---|---|
| Consistency Score | **0.5956** |
| Match Count | 65 |
| Dominant Direction | BULLISH |
| Direction % | 72.3% |
| Mag ATR Mean | 2.1465 |
| Mag ATR Std | 1.2023 |
| Mag CV | 0.5601 |
| Timing (candles) | 3.45 |
| Persistence | 3.48 |
| Frequency | 1.117% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     30 samples  bullish   76.7%  mag_atr=2.6529
    val       19 samples  bullish   68.4%  mag_atr=1.8781
    oos       16 samples  bullish   68.8%  mag_atr=1.5158
```

> When [RSI14_oversold + STO_K_21_oversold + ADX_strong_trend] occurs, price historically reacts BULLISH 72.3% of the time with an average move of 2.15 ATR (moderate variance) and stable repetition across validation splits.

---

## #34 — `RSI13_oversold + STO_K_21_oversold + ADX_strong_trend`

| Field | Value |
|---|---|
| Consistency Score | **0.5930** |
| Match Count | 66 |
| Dominant Direction | BULLISH |
| Direction % | 71.2% |
| Mag ATR Mean | 2.1306 |
| Mag ATR Std | 1.2 |
| Mag CV | 0.5632 |
| Timing (candles) | 3.45 |
| Persistence | 3.47 |
| Frequency | 1.1342% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     30 samples  bullish   76.7%  mag_atr=2.6529
    val       19 samples  bullish   68.4%  mag_atr=1.8781
    oos       17 samples  bullish   64.7%  mag_atr=1.4912
```

> When [RSI13_oversold + STO_K_21_oversold + ADX_strong_trend] occurs, price historically reacts BULLISH 71.2% of the time with an average move of 2.13 ATR (moderate variance) and stable repetition across validation splits.

---

## #35 — `EMA21_below_EMA50 + CCI14_overbought + squeeze_active`

| Field | Value |
|---|---|
| Consistency Score | **0.5921** |
| Match Count | 71 |
| Dominant Direction | BEARISH |
| Direction % | 66.2% |
| Mag ATR Mean | 1.8965 |
| Mag ATR Std | 1.0196 |
| Mag CV | 0.5376 |
| Timing (candles) | 3.79 |
| Persistence | 3.08 |
| Frequency | 1.2201% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     42 samples  bearish   64.3%  mag_atr=1.7766
    val       16 samples  bearish   75.0%  mag_atr=2.0498
    oos       13 samples  bearish   61.5%  mag_atr=2.0952
```

> When [EMA21_below_EMA50 + CCI14_overbought + squeeze_active] occurs, price historically reacts BEARISH 66.2% of the time with an average move of 1.90 ATR (moderate variance) and stable repetition across validation splits.

---

## #36 — `RSI7_oversold + RSI13_oversold + ADX_strong_trend`

| Field | Value |
|---|---|
| Consistency Score | **0.5911** |
| Match Count | 77 |
| Dominant Direction | BULLISH |
| Direction % | 66.2% |
| Mag ATR Mean | 1.9825 |
| Mag ATR Std | 1.1717 |
| Mag CV | 0.591 |
| Timing (candles) | 3.34 |
| Persistence | 3.36 |
| Frequency | 1.3233% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     41 samples  bullish   65.8%  mag_atr=2.2397
    val       19 samples  bullish   68.4%  mag_atr=1.8669
    oos       17 samples  bullish   64.7%  mag_atr=1.4912
```

> When [RSI7_oversold + RSI13_oversold + ADX_strong_trend] occurs, price historically reacts BULLISH 66.2% of the time with an average move of 1.98 ATR (moderate variance) and stable repetition across validation splits.

---

## #37 — `RSI7_oversold + RSI14_oversold + ADX_strong_trend`

| Field | Value |
|---|---|
| Consistency Score | **0.5907** |
| Match Count | 74 |
| Dominant Direction | BULLISH |
| Direction % | 67.6% |
| Mag ATR Mean | 2.0162 |
| Mag ATR Std | 1.1826 |
| Mag CV | 0.5865 |
| Timing (candles) | 3.34 |
| Persistence | 3.36 |
| Frequency | 1.2717% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     40 samples  bullish   65.0%  mag_atr=2.263
    val       18 samples  bullish   72.2%  mag_atr=1.9126
    oos       16 samples  bullish   68.8%  mag_atr=1.5158
```

> When [RSI7_oversold + RSI14_oversold + ADX_strong_trend] occurs, price historically reacts BULLISH 67.6% of the time with an average move of 2.02 ATR (moderate variance) and stable repetition across validation splits.

---

## #38 — `STO_K_14_oversold + ADX_strong_trend + EMA50_below_EMA100`

| Field | Value |
|---|---|
| Consistency Score | **0.5891** |
| Match Count | 71 |
| Dominant Direction | BULLISH |
| Direction % | 70.4% |
| Mag ATR Mean | 2.1465 |
| Mag ATR Std | 1.3063 |
| Mag CV | 0.6086 |
| Timing (candles) | 3.61 |
| Persistence | 3.49 |
| Frequency | 1.2201% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     34 samples  bullish   73.5%  mag_atr=2.6519
    val       22 samples  bullish   68.2%  mag_atr=1.8157
    oos       15 samples  bullish   66.7%  mag_atr=1.4859
```

> When [STO_K_14_oversold + ADX_strong_trend + EMA50_below_EMA100] occurs, price historically reacts BULLISH 70.4% of the time with an average move of 2.15 ATR (high variance) and stable repetition across validation splits.

---

## #39 — `RSI14_oversold + STO_K_14_oversold + ADX_strong_trend`

| Field | Value |
|---|---|
| Consistency Score | **0.5888** |
| Match Count | 59 |
| Dominant Direction | BULLISH |
| Direction % | 74.6% |
| Mag ATR Mean | 2.1654 |
| Mag ATR Std | 1.2341 |
| Mag CV | 0.5699 |
| Timing (candles) | 3.51 |
| Persistence | 3.51 |
| Frequency | 1.0139% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     27 samples  bullish   77.8%  mag_atr=2.7282
    val       16 samples  bullish   75.0%  mag_atr=1.8654
    oos       16 samples  bullish   68.8%  mag_atr=1.5158
```

> When [RSI14_oversold + STO_K_14_oversold + ADX_strong_trend] occurs, price historically reacts BULLISH 74.6% of the time with an average move of 2.17 ATR (moderate variance) and stable repetition across validation splits.

---

## #40 — `RSI13_oversold + STO_K_14_oversold + ADX_strong_trend`

| Field | Value |
|---|---|
| Consistency Score | **0.5856** |
| Match Count | 60 |
| Dominant Direction | BULLISH |
| Direction % | 73.3% |
| Mag ATR Mean | 2.1476 |
| Mag ATR Std | 1.2314 |
| Mag CV | 0.5734 |
| Timing (candles) | 3.52 |
| Persistence | 3.5 |
| Frequency | 1.0311% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     27 samples  bullish   77.8%  mag_atr=2.7282
    val       16 samples  bullish   75.0%  mag_atr=1.8654
    oos       17 samples  bullish   64.7%  mag_atr=1.4912
```

> When [RSI13_oversold + STO_K_14_oversold + ADX_strong_trend] occurs, price historically reacts BULLISH 73.3% of the time with an average move of 2.15 ATR (moderate variance) and stable repetition across validation splits.

---

## #41 — `RSI7_oversold + STO_K_14_oversold + ADX_strong_trend`

| Field | Value |
|---|---|
| Consistency Score | **0.5845** |
| Match Count | 67 |
| Dominant Direction | BULLISH |
| Direction % | 70.2% |
| Mag ATR Mean | 2.0491 |
| Mag ATR Std | 1.2104 |
| Mag CV | 0.5907 |
| Timing (candles) | 3.52 |
| Persistence | 3.39 |
| Frequency | 1.1514% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     31 samples  bullish   77.4%  mag_atr=2.5961
    val       15 samples  bullish   73.3%  mag_atr=1.851
    oos       21 samples  bullish   57.1%  mag_atr=1.3833
```

> When [RSI7_oversold + STO_K_14_oversold + ADX_strong_trend] occurs, price historically reacts BULLISH 70.2% of the time with an average move of 2.05 ATR (moderate variance) and stable repetition across validation splits.

---

## #42 — `RSI7_overbought + ATR7_above_ATR13 + doji`

| Field | Value |
|---|---|
| Consistency Score | **0.5829** |
| Match Count | 60 |
| Dominant Direction | BULLISH |
| Direction % | 65.0% |
| Mag ATR Mean | 2.3164 |
| Mag ATR Std | 1.0835 |
| Mag CV | 0.4678 |
| Timing (candles) | 4.08 |
| Persistence | 3.1 |
| Frequency | 1.0311% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     34 samples  bullish   64.7%  mag_atr=2.2573
    val       15 samples  bullish   66.7%  mag_atr=2.5502
    oos       11 samples  bullish   63.6%  mag_atr=2.1748
```

> When [RSI7_overbought + ATR7_above_ATR13 + doji] occurs, price historically reacts BULLISH 65.0% of the time with an average move of 2.32 ATR (moderate variance) and stable repetition across validation splits.

---

## #43 — `RSI7_oversold + EMA21_below_EMA50 + close_above_EMA200`

| Field | Value |
|---|---|
| Consistency Score | **0.5772** |
| Match Count | 59 |
| Dominant Direction | BULLISH |
| Direction % | 69.5% |
| Mag ATR Mean | 1.7124 |
| Mag ATR Std | 0.934 |
| Mag CV | 0.5454 |
| Timing (candles) | 3.97 |
| Persistence | 3.66 |
| Frequency | 1.0139% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     36 samples  bullish   72.2%  mag_atr=1.6953
    val       12 samples  bullish   75.0%  mag_atr=1.7326
    oos       11 samples  bullish   54.5%  mag_atr=1.7462
```

> When [RSI7_oversold + EMA21_below_EMA50 + close_above_EMA200] occurs, price historically reacts BULLISH 69.5% of the time with an average move of 1.71 ATR (moderate variance) and stable repetition across validation splits.

---

## #44 — `STO_K_14_oversold + EMA50_above_EMA200 + MACD_9_21_bull_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.5748** |
| Match Count | 42 |
| Dominant Direction | BULLISH |
| Direction % | 69.0% |
| Mag ATR Mean | 1.6854 |
| Mag ATR Std | 0.6913 |
| Mag CV | 0.4102 |
| Timing (candles) | 3.83 |
| Persistence | 3.79 |
| Frequency | 0.7218% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     22 samples  bullish   77.3%  mag_atr=1.9678
    val       10 samples  bullish   60.0%  mag_atr=1.3849
    oos       10 samples  bullish   60.0%  mag_atr=1.3647
```

> When [STO_K_14_oversold + EMA50_above_EMA200 + MACD_9_21_bull_cross] occurs, price historically reacts BULLISH 69.0% of the time with an average move of 1.69 ATR (moderate variance) and stable repetition across validation splits.

---

## #45 — `RSI14_oversold + ADX_strong_trend + EMA50_below_EMA200`

| Field | Value |
|---|---|
| Consistency Score | **0.5708** |
| Match Count | 68 |
| Dominant Direction | BULLISH |
| Direction % | 66.2% |
| Mag ATR Mean | 2.0309 |
| Mag ATR Std | 1.2139 |
| Mag CV | 0.5977 |
| Timing (candles) | 3.38 |
| Persistence | 3.35 |
| Frequency | 1.1686% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     37 samples  bullish   67.6%  mag_atr=2.2481
    val       18 samples  bullish   66.7%  mag_atr=1.9149
    oos       13 samples  bullish   61.5%  mag_atr=1.5731
```

> When [RSI14_oversold + ADX_strong_trend + EMA50_below_EMA200] occurs, price historically reacts BULLISH 66.2% of the time with an average move of 2.03 ATR (moderate variance) and stable repetition across validation splits.

---

## #46 — `RSI13_oversold + ADX_strong_trend + EMA50_below_EMA200`

| Field | Value |
|---|---|
| Consistency Score | **0.5688** |
| Match Count | 69 |
| Dominant Direction | BULLISH |
| Direction % | 65.2% |
| Mag ATR Mean | 2.0166 |
| Mag ATR Std | 1.2109 |
| Mag CV | 0.6005 |
| Timing (candles) | 3.35 |
| Persistence | 3.33 |
| Frequency | 1.1858% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     37 samples  bullish   67.6%  mag_atr=2.2481
    val       19 samples  bullish   63.2%  mag_atr=1.8691
    oos       13 samples  bullish   61.5%  mag_atr=1.5731
```

> When [RSI13_oversold + ADX_strong_trend + EMA50_below_EMA200] occurs, price historically reacts BULLISH 65.2% of the time with an average move of 2.02 ATR (high variance) and stable repetition across validation splits.

---

## #47 — `close_above_BB_UPPER_20_2 + MACD_8_21_bear_cross + CCI21_overbought`

| Field | Value |
|---|---|
| Consistency Score | **0.5656** |
| Match Count | 60 |
| Dominant Direction | BULLISH |
| Direction % | 65.0% |
| Mag ATR Mean | 2.2608 |
| Mag ATR Std | 1.2138 |
| Mag CV | 0.5369 |
| Timing (candles) | 4.1 |
| Persistence | 3.25 |
| Frequency | 1.0311% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     32 samples  bullish   65.6%  mag_atr=2.1998
    val       14 samples  bullish   64.3%  mag_atr=2.7623
    oos       14 samples  bullish   64.3%  mag_atr=1.8986
```

> When [close_above_BB_UPPER_20_2 + MACD_8_21_bear_cross + CCI21_overbought] occurs, price historically reacts BULLISH 65.0% of the time with an average move of 2.26 ATR (moderate variance) and stable repetition across validation splits.

---

## #48 — `STO_K_14_oversold + ADX_strong_trend + EMA50_below_EMA200`

| Field | Value |
|---|---|
| Consistency Score | **0.5603** |
| Match Count | 67 |
| Dominant Direction | BULLISH |
| Direction % | 65.7% |
| Mag ATR Mean | 2.1424 |
| Mag ATR Std | 1.338 |
| Mag CV | 0.6245 |
| Timing (candles) | 3.72 |
| Persistence | 3.22 |
| Frequency | 1.1514% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     33 samples  bullish   63.6%  mag_atr=2.6036
    val       19 samples  bullish   68.4%  mag_atr=1.8596
    oos       15 samples  bullish   66.7%  mag_atr=1.4859
```

> When [STO_K_14_oversold + ADX_strong_trend + EMA50_below_EMA200] occurs, price historically reacts BULLISH 65.7% of the time with an average move of 2.14 ATR (high variance) and stable repetition across validation splits.

---

## #49 — `RSI7_oversold + EMA50_above_EMA200 + MACD_12_26_bull_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.5583** |
| Match Count | 40 |
| Dominant Direction | BULLISH |
| Direction % | 72.5% |
| Mag ATR Mean | 1.8086 |
| Mag ATR Std | 0.6773 |
| Mag CV | 0.3745 |
| Timing (candles) | 4.17 |
| Persistence | 3.73 |
| Frequency | 0.6874% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     21 samples  bullish   71.4%  mag_atr=2.0784
    val       10 samples  bullish   70.0%  mag_atr=1.4664
    oos     [insufficient]
```

> When [RSI7_oversold + EMA50_above_EMA200 + MACD_12_26_bull_cross] occurs, price historically reacts BULLISH 72.5% of the time with an average move of 1.81 ATR (low variance) and stable repetition across validation splits.

---

## #50 — `STO_K_14_oversold + ADX_strong_trend + MACD_12_26_bull_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.5578** |
| Match Count | 56 |
| Dominant Direction | BULLISH |
| Direction % | 69.6% |
| Mag ATR Mean | 2.0648 |
| Mag ATR Std | 1.2395 |
| Mag CV | 0.6003 |
| Timing (candles) | 3.59 |
| Persistence | 3.59 |
| Frequency | 0.9624% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     19 samples  bullish   68.4%  mag_atr=2.8328
    val       22 samples  bullish   68.2%  mag_atr=1.8157
    oos       15 samples  bullish   73.3%  mag_atr=1.4572
```

> When [STO_K_14_oversold + ADX_strong_trend + MACD_12_26_bull_cross] occurs, price historically reacts BULLISH 69.6% of the time with an average move of 2.06 ATR (high variance) and stable repetition across validation splits.

---
