# Market Condition Analysis Report

**Lookahead:** 5 candles  
**Min direction:** 65.0%  
**Max mag CV:** 0.85  

---

## #1 — `RSI14_oversold + ADX_strong_trend`

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

## #2 — `RSI14_oversold + ADX_trending + ADX_strong_trend`

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

## #3 — `RSI14_oversold + ADX_strong_trend + EMA21_above_Close`

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

## #4 — `RSI14_oversold + ADX_strong_trend + close_below_EMA200`

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

## #5 — `RSI14_oversold + ADX_trending + ADX_strong_trend + EMA21_above_Close`

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

> When [RSI14_oversold + ADX_trending + ADX_strong_trend + EMA21_above_Close] occurs, price historically reacts BULLISH 68.3% of the time with an average move of 2.00 ATR (moderate variance) and stable repetition across validation splits.

---

## #6 — `RSI14_oversold + ADX_trending + ADX_strong_trend + close_below_EMA200`

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

> When [RSI14_oversold + ADX_trending + ADX_strong_trend + close_below_EMA200] occurs, price historically reacts BULLISH 68.3% of the time with an average move of 2.00 ATR (moderate variance) and stable repetition across validation splits.

---

## #7 — `RSI14_oversold + ADX_strong_trend + EMA21_above_Close + close_below_EMA200`

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

> When [RSI14_oversold + ADX_strong_trend + EMA21_above_Close + close_below_EMA200] occurs, price historically reacts BULLISH 68.3% of the time with an average move of 2.00 ATR (moderate variance) and stable repetition across validation splits.

---

## #8 — `RSI14_oversold + ADX_trending + ADX_strong_trend + EMA21_above_Close + close_below_EMA200`

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

> When [RSI14_oversold + ADX_trending + ADX_strong_trend + EMA21_above_Close + close_below_EMA200] occurs, price historically reacts BULLISH 68.3% of the time with an average move of 2.00 ATR (moderate variance) and stable repetition across validation splits.

---

## #9 — `RSI14_oversold + RSI7_oversold + ADX_strong_trend`

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

> When [RSI14_oversold + RSI7_oversold + ADX_strong_trend] occurs, price historically reacts BULLISH 67.6% of the time with an average move of 2.02 ATR (moderate variance) and stable repetition across validation splits.

---

## #10 — `RSI14_oversold + RSI7_oversold + ADX_trending + ADX_strong_trend`

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

> When [RSI14_oversold + RSI7_oversold + ADX_trending + ADX_strong_trend] occurs, price historically reacts BULLISH 67.6% of the time with an average move of 2.02 ATR (moderate variance) and stable repetition across validation splits.

---

## #11 — `RSI14_oversold + RSI7_oversold + ADX_strong_trend + EMA21_above_Close`

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

> When [RSI14_oversold + RSI7_oversold + ADX_strong_trend + EMA21_above_Close] occurs, price historically reacts BULLISH 67.6% of the time with an average move of 2.02 ATR (moderate variance) and stable repetition across validation splits.

---

## #12 — `RSI14_oversold + RSI7_oversold + ADX_strong_trend + close_below_EMA200`

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

> When [RSI14_oversold + RSI7_oversold + ADX_strong_trend + close_below_EMA200] occurs, price historically reacts BULLISH 67.6% of the time with an average move of 2.02 ATR (moderate variance) and stable repetition across validation splits.

---

## #13 — `RSI14_oversold + RSI7_oversold + ADX_trending + ADX_strong_trend + EMA21_above_Close`

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

> When [RSI14_oversold + RSI7_oversold + ADX_trending + ADX_strong_trend + EMA21_above_Close] occurs, price historically reacts BULLISH 67.6% of the time with an average move of 2.02 ATR (moderate variance) and stable repetition across validation splits.

---

## #14 — `RSI14_oversold + RSI7_oversold + ADX_trending + ADX_strong_trend + close_below_EMA200`

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

> When [RSI14_oversold + RSI7_oversold + ADX_trending + ADX_strong_trend + close_below_EMA200] occurs, price historically reacts BULLISH 67.6% of the time with an average move of 2.02 ATR (moderate variance) and stable repetition across validation splits.

---

## #15 — `RSI14_oversold + RSI7_oversold + ADX_strong_trend + EMA21_above_Close + close_below_EMA200`

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

> When [RSI14_oversold + RSI7_oversold + ADX_strong_trend + EMA21_above_Close + close_below_EMA200] occurs, price historically reacts BULLISH 67.6% of the time with an average move of 2.02 ATR (moderate variance) and stable repetition across validation splits.

---

## #16 — `RSI14_oversold + ADX_strong_trend + EMA21_below_EMA50`

| Field | Value |
|---|---|
| Consistency Score | **0.5678** |
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
    oos     [insufficient]
```

> When [RSI14_oversold + ADX_strong_trend + EMA21_below_EMA50] occurs, price historically reacts BULLISH 67.5% of the time with an average move of 2.03 ATR (moderate variance) and stable repetition across validation splits.

---

## #17 — `RSI14_oversold + ADX_trending + ADX_strong_trend + EMA21_below_EMA50`

| Field | Value |
|---|---|
| Consistency Score | **0.5678** |
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
    oos     [insufficient]
```

> When [RSI14_oversold + ADX_trending + ADX_strong_trend + EMA21_below_EMA50] occurs, price historically reacts BULLISH 67.5% of the time with an average move of 2.03 ATR (moderate variance) and stable repetition across validation splits.

---

## #18 — `RSI14_oversold + ADX_strong_trend + EMA21_below_EMA50 + EMA21_above_Close`

| Field | Value |
|---|---|
| Consistency Score | **0.5678** |
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
    oos     [insufficient]
```

> When [RSI14_oversold + ADX_strong_trend + EMA21_below_EMA50 + EMA21_above_Close] occurs, price historically reacts BULLISH 67.5% of the time with an average move of 2.03 ATR (moderate variance) and stable repetition across validation splits.

---

## #19 — `RSI14_oversold + ADX_strong_trend + EMA21_below_EMA50 + close_below_EMA200`

| Field | Value |
|---|---|
| Consistency Score | **0.5678** |
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
    oos     [insufficient]
```

> When [RSI14_oversold + ADX_strong_trend + EMA21_below_EMA50 + close_below_EMA200] occurs, price historically reacts BULLISH 67.5% of the time with an average move of 2.03 ATR (moderate variance) and stable repetition across validation splits.

---

## #20 — `RSI14_oversold + ADX_trending + ADX_strong_trend + EMA21_below_EMA50 + EMA21_above_Close`

| Field | Value |
|---|---|
| Consistency Score | **0.5678** |
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
    oos     [insufficient]
```

> When [RSI14_oversold + ADX_trending + ADX_strong_trend + EMA21_below_EMA50 + EMA21_above_Close] occurs, price historically reacts BULLISH 67.5% of the time with an average move of 2.03 ATR (moderate variance) and stable repetition across validation splits.

---

## #21 — `RSI14_oversold + ADX_trending + ADX_strong_trend + EMA21_below_EMA50 + close_below_EMA200`

| Field | Value |
|---|---|
| Consistency Score | **0.5678** |
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
    oos     [insufficient]
```

> When [RSI14_oversold + ADX_trending + ADX_strong_trend + EMA21_below_EMA50 + close_below_EMA200] occurs, price historically reacts BULLISH 67.5% of the time with an average move of 2.03 ATR (moderate variance) and stable repetition across validation splits.

---

## #22 — `RSI14_oversold + ADX_strong_trend + EMA21_below_EMA50 + EMA21_above_Close + close_below_EMA200`

| Field | Value |
|---|---|
| Consistency Score | **0.5678** |
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
    oos     [insufficient]
```

> When [RSI14_oversold + ADX_strong_trend + EMA21_below_EMA50 + EMA21_above_Close + close_below_EMA200] occurs, price historically reacts BULLISH 67.5% of the time with an average move of 2.03 ATR (moderate variance) and stable repetition across validation splits.

---

## #23 — `RSI14_oversold + ADX_strong_trend + EMA50_below_EMA100`

| Field | Value |
|---|---|
| Consistency Score | **0.5641** |
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
    oos     [insufficient]
```

> When [RSI14_oversold + ADX_strong_trend + EMA50_below_EMA100] occurs, price historically reacts BULLISH 68.0% of the time with an average move of 2.03 ATR (moderate variance) and stable repetition across validation splits.

---

## #24 — `RSI14_oversold + ADX_trending + ADX_strong_trend + EMA50_below_EMA100`

| Field | Value |
|---|---|
| Consistency Score | **0.5641** |
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
    oos     [insufficient]
```

> When [RSI14_oversold + ADX_trending + ADX_strong_trend + EMA50_below_EMA100] occurs, price historically reacts BULLISH 68.0% of the time with an average move of 2.03 ATR (moderate variance) and stable repetition across validation splits.

---

## #25 — `RSI14_oversold + ADX_strong_trend + EMA21_below_EMA50 + EMA50_below_EMA100`

| Field | Value |
|---|---|
| Consistency Score | **0.5641** |
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
    oos     [insufficient]
```

> When [RSI14_oversold + ADX_strong_trend + EMA21_below_EMA50 + EMA50_below_EMA100] occurs, price historically reacts BULLISH 68.0% of the time with an average move of 2.03 ATR (moderate variance) and stable repetition across validation splits.

---

## #26 — `RSI14_oversold + ADX_strong_trend + EMA21_above_Close + EMA50_below_EMA100`

| Field | Value |
|---|---|
| Consistency Score | **0.5641** |
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
    oos     [insufficient]
```

> When [RSI14_oversold + ADX_strong_trend + EMA21_above_Close + EMA50_below_EMA100] occurs, price historically reacts BULLISH 68.0% of the time with an average move of 2.03 ATR (moderate variance) and stable repetition across validation splits.

---

## #27 — `RSI14_oversold + ADX_strong_trend + EMA50_below_EMA100 + close_below_EMA200`

| Field | Value |
|---|---|
| Consistency Score | **0.5641** |
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
    oos     [insufficient]
```

> When [RSI14_oversold + ADX_strong_trend + EMA50_below_EMA100 + close_below_EMA200] occurs, price historically reacts BULLISH 68.0% of the time with an average move of 2.03 ATR (moderate variance) and stable repetition across validation splits.

---

## #28 — `RSI14_oversold + ADX_trending + ADX_strong_trend + EMA21_below_EMA50 + EMA50_below_EMA100`

| Field | Value |
|---|---|
| Consistency Score | **0.5641** |
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
    oos     [insufficient]
```

> When [RSI14_oversold + ADX_trending + ADX_strong_trend + EMA21_below_EMA50 + EMA50_below_EMA100] occurs, price historically reacts BULLISH 68.0% of the time with an average move of 2.03 ATR (moderate variance) and stable repetition across validation splits.

---

## #29 — `RSI14_oversold + ADX_trending + ADX_strong_trend + EMA21_above_Close + EMA50_below_EMA100`

| Field | Value |
|---|---|
| Consistency Score | **0.5641** |
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
    oos     [insufficient]
```

> When [RSI14_oversold + ADX_trending + ADX_strong_trend + EMA21_above_Close + EMA50_below_EMA100] occurs, price historically reacts BULLISH 68.0% of the time with an average move of 2.03 ATR (moderate variance) and stable repetition across validation splits.

---

## #30 — `RSI14_oversold + ADX_trending + ADX_strong_trend + EMA50_below_EMA100 + close_below_EMA200`

| Field | Value |
|---|---|
| Consistency Score | **0.5641** |
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
    oos     [insufficient]
```

> When [RSI14_oversold + ADX_trending + ADX_strong_trend + EMA50_below_EMA100 + close_below_EMA200] occurs, price historically reacts BULLISH 68.0% of the time with an average move of 2.03 ATR (moderate variance) and stable repetition across validation splits.

---

## #31 — `RSI14_oversold + ADX_strong_trend + EMA21_below_EMA50 + EMA21_above_Close + EMA50_below_EMA100`

| Field | Value |
|---|---|
| Consistency Score | **0.5641** |
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
    oos     [insufficient]
```

> When [RSI14_oversold + ADX_strong_trend + EMA21_below_EMA50 + EMA21_above_Close + EMA50_below_EMA100] occurs, price historically reacts BULLISH 68.0% of the time with an average move of 2.03 ATR (moderate variance) and stable repetition across validation splits.

---

## #32 — `RSI14_oversold + ADX_strong_trend + EMA21_below_EMA50 + EMA50_below_EMA100 + close_below_EMA200`

| Field | Value |
|---|---|
| Consistency Score | **0.5641** |
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
    oos     [insufficient]
```

> When [RSI14_oversold + ADX_strong_trend + EMA21_below_EMA50 + EMA50_below_EMA100 + close_below_EMA200] occurs, price historically reacts BULLISH 68.0% of the time with an average move of 2.03 ATR (moderate variance) and stable repetition across validation splits.

---

## #33 — `RSI14_oversold + ADX_strong_trend + EMA21_above_Close + EMA50_below_EMA100 + close_below_EMA200`

| Field | Value |
|---|---|
| Consistency Score | **0.5641** |
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
    oos     [insufficient]
```

> When [RSI14_oversold + ADX_strong_trend + EMA21_above_Close + EMA50_below_EMA100 + close_below_EMA200] occurs, price historically reacts BULLISH 68.0% of the time with an average move of 2.03 ATR (moderate variance) and stable repetition across validation splits.

---

## #34 — `EMA21_below_EMA50 + MACD_bull_cross + squeeze_active + CCI14_overbought`

| Field | Value |
|---|---|
| Consistency Score | **0.5588** |
| Match Count | 70 |
| Dominant Direction | BEARISH |
| Direction % | 67.1% |
| Mag ATR Mean | 1.8867 |
| Mag ATR Std | 1.0236 |
| Mag CV | 0.5425 |
| Timing (candles) | 3.8 |
| Persistence | 3.13 |
| Frequency | 1.203% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     41 samples  bearish   65.8%  mag_atr=1.7569
    val       16 samples  bearish   75.0%  mag_atr=2.0498
    oos     [insufficient]
```

> When [EMA21_below_EMA50 + MACD_bull_cross + squeeze_active + CCI14_overbought] occurs, price historically reacts BEARISH 67.1% of the time with an average move of 1.89 ATR (moderate variance) and stable repetition across validation splits.

---

## #35 — `EMA21_below_EMA50 + EMA21_below_Close + MACD_bull_cross + squeeze_active + CCI14_overbought`

| Field | Value |
|---|---|
| Consistency Score | **0.5588** |
| Match Count | 70 |
| Dominant Direction | BEARISH |
| Direction % | 67.1% |
| Mag ATR Mean | 1.8867 |
| Mag ATR Std | 1.0236 |
| Mag CV | 0.5425 |
| Timing (candles) | 3.8 |
| Persistence | 3.13 |
| Frequency | 1.203% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     41 samples  bearish   65.8%  mag_atr=1.7569
    val       16 samples  bearish   75.0%  mag_atr=2.0498
    oos     [insufficient]
```

> When [EMA21_below_EMA50 + EMA21_below_Close + MACD_bull_cross + squeeze_active + CCI14_overbought] occurs, price historically reacts BEARISH 67.1% of the time with an average move of 1.89 ATR (moderate variance) and stable repetition across validation splits.

---

## #36 — `EMA21_below_EMA50 + squeeze_active + CCI14_overbought`

| Field | Value |
|---|---|
| Consistency Score | **0.5587** |
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
    oos     [insufficient]
```

> When [EMA21_below_EMA50 + squeeze_active + CCI14_overbought] occurs, price historically reacts BEARISH 66.2% of the time with an average move of 1.90 ATR (moderate variance) and stable repetition across validation splits.

---

## #37 — `EMA21_below_EMA50 + EMA21_below_Close + squeeze_active + CCI14_overbought`

| Field | Value |
|---|---|
| Consistency Score | **0.5587** |
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
    oos     [insufficient]
```

> When [EMA21_below_EMA50 + EMA21_below_Close + squeeze_active + CCI14_overbought] occurs, price historically reacts BEARISH 66.2% of the time with an average move of 1.90 ATR (moderate variance) and stable repetition across validation splits.

---

## #38 — `RSI14_oversold + ADX_strong_trend + MACD_bear_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.5532** |
| Match Count | 71 |
| Dominant Direction | BULLISH |
| Direction % | 67.6% |
| Mag ATR Mean | 2.0547 |
| Mag ATR Std | 1.1908 |
| Mag CV | 0.5795 |
| Timing (candles) | 3.39 |
| Persistence | 3.39 |
| Frequency | 1.2201% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     38 samples  bullish   68.4%  mag_atr=2.335
    val       18 samples  bullish   66.7%  mag_atr=1.9149
    oos     [insufficient]
```

> When [RSI14_oversold + ADX_strong_trend + MACD_bear_cross] occurs, price historically reacts BULLISH 67.6% of the time with an average move of 2.05 ATR (moderate variance) and stable repetition across validation splits.

---

## #39 — `RSI14_oversold + ADX_trending + ADX_strong_trend + MACD_bear_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.5532** |
| Match Count | 71 |
| Dominant Direction | BULLISH |
| Direction % | 67.6% |
| Mag ATR Mean | 2.0547 |
| Mag ATR Std | 1.1908 |
| Mag CV | 0.5795 |
| Timing (candles) | 3.39 |
| Persistence | 3.39 |
| Frequency | 1.2201% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     38 samples  bullish   68.4%  mag_atr=2.335
    val       18 samples  bullish   66.7%  mag_atr=1.9149
    oos     [insufficient]
```

> When [RSI14_oversold + ADX_trending + ADX_strong_trend + MACD_bear_cross] occurs, price historically reacts BULLISH 67.6% of the time with an average move of 2.05 ATR (moderate variance) and stable repetition across validation splits.

---

## #40 — `RSI14_oversold + ADX_strong_trend + EMA21_above_Close + MACD_bear_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.5532** |
| Match Count | 71 |
| Dominant Direction | BULLISH |
| Direction % | 67.6% |
| Mag ATR Mean | 2.0547 |
| Mag ATR Std | 1.1908 |
| Mag CV | 0.5795 |
| Timing (candles) | 3.39 |
| Persistence | 3.39 |
| Frequency | 1.2201% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     38 samples  bullish   68.4%  mag_atr=2.335
    val       18 samples  bullish   66.7%  mag_atr=1.9149
    oos     [insufficient]
```

> When [RSI14_oversold + ADX_strong_trend + EMA21_above_Close + MACD_bear_cross] occurs, price historically reacts BULLISH 67.6% of the time with an average move of 2.05 ATR (moderate variance) and stable repetition across validation splits.

---

## #41 — `RSI14_oversold + ADX_strong_trend + close_below_EMA200 + MACD_bear_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.5532** |
| Match Count | 71 |
| Dominant Direction | BULLISH |
| Direction % | 67.6% |
| Mag ATR Mean | 2.0547 |
| Mag ATR Std | 1.1908 |
| Mag CV | 0.5795 |
| Timing (candles) | 3.39 |
| Persistence | 3.39 |
| Frequency | 1.2201% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     38 samples  bullish   68.4%  mag_atr=2.335
    val       18 samples  bullish   66.7%  mag_atr=1.9149
    oos     [insufficient]
```

> When [RSI14_oversold + ADX_strong_trend + close_below_EMA200 + MACD_bear_cross] occurs, price historically reacts BULLISH 67.6% of the time with an average move of 2.05 ATR (moderate variance) and stable repetition across validation splits.

---

## #42 — `RSI14_oversold + ADX_trending + ADX_strong_trend + EMA21_above_Close + MACD_bear_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.5532** |
| Match Count | 71 |
| Dominant Direction | BULLISH |
| Direction % | 67.6% |
| Mag ATR Mean | 2.0547 |
| Mag ATR Std | 1.1908 |
| Mag CV | 0.5795 |
| Timing (candles) | 3.39 |
| Persistence | 3.39 |
| Frequency | 1.2201% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     38 samples  bullish   68.4%  mag_atr=2.335
    val       18 samples  bullish   66.7%  mag_atr=1.9149
    oos     [insufficient]
```

> When [RSI14_oversold + ADX_trending + ADX_strong_trend + EMA21_above_Close + MACD_bear_cross] occurs, price historically reacts BULLISH 67.6% of the time with an average move of 2.05 ATR (moderate variance) and stable repetition across validation splits.

---

## #43 — `RSI14_oversold + ADX_trending + ADX_strong_trend + close_below_EMA200 + MACD_bear_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.5532** |
| Match Count | 71 |
| Dominant Direction | BULLISH |
| Direction % | 67.6% |
| Mag ATR Mean | 2.0547 |
| Mag ATR Std | 1.1908 |
| Mag CV | 0.5795 |
| Timing (candles) | 3.39 |
| Persistence | 3.39 |
| Frequency | 1.2201% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     38 samples  bullish   68.4%  mag_atr=2.335
    val       18 samples  bullish   66.7%  mag_atr=1.9149
    oos     [insufficient]
```

> When [RSI14_oversold + ADX_trending + ADX_strong_trend + close_below_EMA200 + MACD_bear_cross] occurs, price historically reacts BULLISH 67.6% of the time with an average move of 2.05 ATR (moderate variance) and stable repetition across validation splits.

---

## #44 — `RSI14_oversold + ADX_strong_trend + EMA21_above_Close + close_below_EMA200 + MACD_bear_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.5532** |
| Match Count | 71 |
| Dominant Direction | BULLISH |
| Direction % | 67.6% |
| Mag ATR Mean | 2.0547 |
| Mag ATR Std | 1.1908 |
| Mag CV | 0.5795 |
| Timing (candles) | 3.39 |
| Persistence | 3.39 |
| Frequency | 1.2201% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     38 samples  bullish   68.4%  mag_atr=2.335
    val       18 samples  bullish   66.7%  mag_atr=1.9149
    oos     [insufficient]
```

> When [RSI14_oversold + ADX_strong_trend + EMA21_above_Close + close_below_EMA200 + MACD_bear_cross] occurs, price historically reacts BULLISH 67.6% of the time with an average move of 2.05 ATR (moderate variance) and stable repetition across validation splits.

---

## #45 — `RSI14_oversold + RSI7_oversold + ADX_strong_trend + EMA21_below_EMA50`

| Field | Value |
|---|---|
| Consistency Score | **0.5512** |
| Match Count | 72 |
| Dominant Direction | BULLISH |
| Direction % | 66.7% |
| Mag ATR Mean | 2.0412 |
| Mag ATR Std | 1.1892 |
| Mag CV | 0.5826 |
| Timing (candles) | 3.33 |
| Persistence | 3.32 |
| Frequency | 1.2373% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     40 samples  bullish   65.0%  mag_atr=2.263
    val       18 samples  bullish   72.2%  mag_atr=1.9126
    oos     [insufficient]
```

> When [RSI14_oversold + RSI7_oversold + ADX_strong_trend + EMA21_below_EMA50] occurs, price historically reacts BULLISH 66.7% of the time with an average move of 2.04 ATR (moderate variance) and stable repetition across validation splits.

---

## #46 — `RSI14_oversold + RSI7_oversold + ADX_trending + ADX_strong_trend + EMA21_below_EMA50`

| Field | Value |
|---|---|
| Consistency Score | **0.5512** |
| Match Count | 72 |
| Dominant Direction | BULLISH |
| Direction % | 66.7% |
| Mag ATR Mean | 2.0412 |
| Mag ATR Std | 1.1892 |
| Mag CV | 0.5826 |
| Timing (candles) | 3.33 |
| Persistence | 3.32 |
| Frequency | 1.2373% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     40 samples  bullish   65.0%  mag_atr=2.263
    val       18 samples  bullish   72.2%  mag_atr=1.9126
    oos     [insufficient]
```

> When [RSI14_oversold + RSI7_oversold + ADX_trending + ADX_strong_trend + EMA21_below_EMA50] occurs, price historically reacts BULLISH 66.7% of the time with an average move of 2.04 ATR (moderate variance) and stable repetition across validation splits.

---

## #47 — `RSI14_oversold + RSI7_oversold + ADX_strong_trend + EMA21_below_EMA50 + EMA21_above_Close`

| Field | Value |
|---|---|
| Consistency Score | **0.5512** |
| Match Count | 72 |
| Dominant Direction | BULLISH |
| Direction % | 66.7% |
| Mag ATR Mean | 2.0412 |
| Mag ATR Std | 1.1892 |
| Mag CV | 0.5826 |
| Timing (candles) | 3.33 |
| Persistence | 3.32 |
| Frequency | 1.2373% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     40 samples  bullish   65.0%  mag_atr=2.263
    val       18 samples  bullish   72.2%  mag_atr=1.9126
    oos     [insufficient]
```

> When [RSI14_oversold + RSI7_oversold + ADX_strong_trend + EMA21_below_EMA50 + EMA21_above_Close] occurs, price historically reacts BULLISH 66.7% of the time with an average move of 2.04 ATR (moderate variance) and stable repetition across validation splits.

---

## #48 — `RSI14_oversold + RSI7_oversold + ADX_strong_trend + EMA21_below_EMA50 + close_below_EMA200`

| Field | Value |
|---|---|
| Consistency Score | **0.5512** |
| Match Count | 72 |
| Dominant Direction | BULLISH |
| Direction % | 66.7% |
| Mag ATR Mean | 2.0412 |
| Mag ATR Std | 1.1892 |
| Mag CV | 0.5826 |
| Timing (candles) | 3.33 |
| Persistence | 3.32 |
| Frequency | 1.2373% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     40 samples  bullish   65.0%  mag_atr=2.263
    val       18 samples  bullish   72.2%  mag_atr=1.9126
    oos     [insufficient]
```

> When [RSI14_oversold + RSI7_oversold + ADX_strong_trend + EMA21_below_EMA50 + close_below_EMA200] occurs, price historically reacts BULLISH 66.7% of the time with an average move of 2.04 ATR (moderate variance) and stable repetition across validation splits.

---

## #49 — `RSI14_oversold + RSI7_oversold + ADX_strong_trend + EMA50_below_EMA100`

| Field | Value |
|---|---|
| Consistency Score | **0.5473** |
| Match Count | 70 |
| Dominant Direction | BULLISH |
| Direction % | 67.1% |
| Mag ATR Mean | 2.048 |
| Mag ATR Std | 1.2048 |
| Mag CV | 0.5883 |
| Timing (candles) | 3.34 |
| Persistence | 3.33 |
| Frequency | 1.203% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     39 samples  bullish   66.7%  mag_atr=2.2688
    val       18 samples  bullish   72.2%  mag_atr=1.9126
    oos     [insufficient]
```

> When [RSI14_oversold + RSI7_oversold + ADX_strong_trend + EMA50_below_EMA100] occurs, price historically reacts BULLISH 67.1% of the time with an average move of 2.05 ATR (moderate variance) and stable repetition across validation splits.

---

## #50 — `RSI14_oversold + ADX_strong_trend + EMA50_below_EMA100 + MACD_bear_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.5473** |
| Match Count | 68 |
| Dominant Direction | BULLISH |
| Direction % | 67.7% |
| Mag ATR Mean | 2.0825 |
| Mag ATR Std | 1.2058 |
| Mag CV | 0.579 |
| Timing (candles) | 3.4 |
| Persistence | 3.38 |
| Frequency | 1.1686% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     37 samples  bullish   70.3%  mag_atr=2.343
    val       18 samples  bullish   66.7%  mag_atr=1.9149
    oos     [insufficient]
```

> When [RSI14_oversold + ADX_strong_trend + EMA50_below_EMA100 + MACD_bear_cross] occurs, price historically reacts BULLISH 67.7% of the time with an average move of 2.08 ATR (moderate variance) and stable repetition across validation splits.

---
