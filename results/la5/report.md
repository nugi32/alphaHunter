# Market Condition Analysis Report

**Lookahead:** 5 candles  
**Min direction:** 65.0%  
**Max mag CV:** 0.85  

---

## #1 — `ADX_trending + EMA13_below_EMA21 + EMA50_above_EMA200 + close_below_EMA200 + MACD_12_26_bull_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.7303** |
| Match Count | 127 |
| Dominant Direction | BULLISH |
| Direction % | 70.1% |
| Mag ATR Mean | 1.5932 |
| Mag ATR Std | 0.7025 |
| Mag CV | 0.4409 |
| Timing (candles) | 3.82 |
| Persistence | 3.5 |
| Frequency | 2.1825% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     71 samples  bullish   77.5%  mag_atr=1.6612
    val       29 samples  bullish   58.6%  mag_atr=1.3831
    oos       27 samples  bullish   63.0%  mag_atr=1.6401
```

> When [ADX_trending + EMA13_below_EMA21 + EMA50_above_EMA200 + close_below_EMA200 + MACD_12_26_bull_cross] occurs, price historically reacts BULLISH 70.1% of the time with an average move of 1.59 ATR (moderate variance) and stable repetition across validation splits.

---

## #2 — `ADX_trending + EMA50_above_EMA200 + close_below_EMA200 + MACD_12_26_bull_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.7292** |
| Match Count | 129 |
| Dominant Direction | BULLISH |
| Direction % | 69.8% |
| Mag ATR Mean | 1.6102 |
| Mag ATR Std | 0.7199 |
| Mag CV | 0.4471 |
| Timing (candles) | 3.82 |
| Persistence | 3.47 |
| Frequency | 2.2169% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     72 samples  bullish   77.8%  mag_atr=1.6622
    val       30 samples  bullish   56.7%  mag_atr=1.4584
    oos       27 samples  bullish   63.0%  mag_atr=1.6401
```

> When [ADX_trending + EMA50_above_EMA200 + close_below_EMA200 + MACD_12_26_bull_cross] occurs, price historically reacts BULLISH 69.8% of the time with an average move of 1.61 ATR (moderate variance) and stable repetition across validation splits.

---

## #3 — `ADX_trending + EMA21_below_EMA50 + EMA50_above_EMA200 + close_below_EMA200 + MACD_12_26_bull_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.7292** |
| Match Count | 129 |
| Dominant Direction | BULLISH |
| Direction % | 69.8% |
| Mag ATR Mean | 1.6102 |
| Mag ATR Std | 0.7199 |
| Mag CV | 0.4471 |
| Timing (candles) | 3.82 |
| Persistence | 3.47 |
| Frequency | 2.2169% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     72 samples  bullish   77.8%  mag_atr=1.6622
    val       30 samples  bullish   56.7%  mag_atr=1.4584
    oos       27 samples  bullish   63.0%  mag_atr=1.6401
```

> When [ADX_trending + EMA21_below_EMA50 + EMA50_above_EMA200 + close_below_EMA200 + MACD_12_26_bull_cross] occurs, price historically reacts BULLISH 69.8% of the time with an average move of 1.61 ATR (moderate variance) and stable repetition across validation splits.

---

## #4 — `ADX_trending + EMA13_below_EMA21 + EMA50_above_EMA200 + close_below_EMA200 + MACD_9_21_bull_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.7244** |
| Match Count | 124 |
| Dominant Direction | BULLISH |
| Direction % | 69.3% |
| Mag ATR Mean | 1.5917 |
| Mag ATR Std | 0.709 |
| Mag CV | 0.4454 |
| Timing (candles) | 3.81 |
| Persistence | 3.49 |
| Frequency | 2.131% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     71 samples  bullish   77.5%  mag_atr=1.6612
    val       27 samples  bullish   55.6%  mag_atr=1.3774
    oos       26 samples  bullish   61.5%  mag_atr=1.6245
```

> When [ADX_trending + EMA13_below_EMA21 + EMA50_above_EMA200 + close_below_EMA200 + MACD_9_21_bull_cross] occurs, price historically reacts BULLISH 69.3% of the time with an average move of 1.59 ATR (moderate variance) and stable repetition across validation splits.

---

## #5 — `ADX_trending + EMA50_above_EMA200 + close_below_EMA200 + MACD_9_21_bull_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.7233** |
| Match Count | 126 |
| Dominant Direction | BULLISH |
| Direction % | 69.0% |
| Mag ATR Mean | 1.6091 |
| Mag ATR Std | 0.7266 |
| Mag CV | 0.4516 |
| Timing (candles) | 3.81 |
| Persistence | 3.45 |
| Frequency | 2.1653% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     72 samples  bullish   77.8%  mag_atr=1.6622
    val       28 samples  bullish   53.6%  mag_atr=1.4583
    oos       26 samples  bullish   61.5%  mag_atr=1.6245
```

> When [ADX_trending + EMA50_above_EMA200 + close_below_EMA200 + MACD_9_21_bull_cross] occurs, price historically reacts BULLISH 69.0% of the time with an average move of 1.61 ATR (moderate variance) and stable repetition across validation splits.

---

## #6 — `ADX_trending + EMA21_below_EMA50 + EMA50_above_EMA200 + close_below_EMA200 + MACD_9_21_bull_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.7233** |
| Match Count | 126 |
| Dominant Direction | BULLISH |
| Direction % | 69.0% |
| Mag ATR Mean | 1.6091 |
| Mag ATR Std | 0.7266 |
| Mag CV | 0.4516 |
| Timing (candles) | 3.81 |
| Persistence | 3.45 |
| Frequency | 2.1653% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     72 samples  bullish   77.8%  mag_atr=1.6622
    val       28 samples  bullish   53.6%  mag_atr=1.4583
    oos       26 samples  bullish   61.5%  mag_atr=1.6245
```

> When [ADX_trending + EMA21_below_EMA50 + EMA50_above_EMA200 + close_below_EMA200 + MACD_9_21_bull_cross] occurs, price historically reacts BULLISH 69.0% of the time with an average move of 1.61 ATR (moderate variance) and stable repetition across validation splits.

---

## #7 — `ADX_trending + EMA50_above_EMA200 + close_below_EMA200 + MACD_12_26_bull_cross + MACD_9_21_bull_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.7233** |
| Match Count | 126 |
| Dominant Direction | BULLISH |
| Direction % | 69.0% |
| Mag ATR Mean | 1.6091 |
| Mag ATR Std | 0.7266 |
| Mag CV | 0.4516 |
| Timing (candles) | 3.81 |
| Persistence | 3.45 |
| Frequency | 2.1653% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     72 samples  bullish   77.8%  mag_atr=1.6622
    val       28 samples  bullish   53.6%  mag_atr=1.4583
    oos       26 samples  bullish   61.5%  mag_atr=1.6245
```

> When [ADX_trending + EMA50_above_EMA200 + close_below_EMA200 + MACD_12_26_bull_cross + MACD_9_21_bull_cross] occurs, price historically reacts BULLISH 69.0% of the time with an average move of 1.61 ATR (moderate variance) and stable repetition across validation splits.

---

## #8 — `STO_K_21_oversold + ADX_trending + EMA21_below_EMA50 + EMA50_above_EMA200`

| Field | Value |
|---|---|
| Consistency Score | **0.7174** |
| Match Count | 131 |
| Dominant Direction | BULLISH |
| Direction % | 67.2% |
| Mag ATR Mean | 1.7537 |
| Mag ATR Std | 0.8137 |
| Mag CV | 0.464 |
| Timing (candles) | 3.84 |
| Persistence | 3.57 |
| Frequency | 2.2512% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     83 samples  bullish   65.1%  mag_atr=1.8148
    val       20 samples  bullish   65.0%  mag_atr=1.4563
    oos       28 samples  bullish   75.0%  mag_atr=1.7849
```

> When [STO_K_21_oversold + ADX_trending + EMA21_below_EMA50 + EMA50_above_EMA200] occurs, price historically reacts BULLISH 67.2% of the time with an average move of 1.75 ATR (moderate variance) and stable repetition across validation splits.

---

## #9 — `STO_K_21_oversold + ADX_trending + EMA13_below_EMA21 + EMA21_below_EMA50 + EMA50_above_EMA200`

| Field | Value |
|---|---|
| Consistency Score | **0.7174** |
| Match Count | 131 |
| Dominant Direction | BULLISH |
| Direction % | 67.2% |
| Mag ATR Mean | 1.7537 |
| Mag ATR Std | 0.8137 |
| Mag CV | 0.464 |
| Timing (candles) | 3.84 |
| Persistence | 3.57 |
| Frequency | 2.2512% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     83 samples  bullish   65.1%  mag_atr=1.8148
    val       20 samples  bullish   65.0%  mag_atr=1.4563
    oos       28 samples  bullish   75.0%  mag_atr=1.7849
```

> When [STO_K_21_oversold + ADX_trending + EMA13_below_EMA21 + EMA21_below_EMA50 + EMA50_above_EMA200] occurs, price historically reacts BULLISH 67.2% of the time with an average move of 1.75 ATR (moderate variance) and stable repetition across validation splits.

---

## #10 — `STO_K_21_oversold + ADX_trending + EMA21_below_EMA50 + EMA21_above_Close + EMA50_above_EMA200`

| Field | Value |
|---|---|
| Consistency Score | **0.7174** |
| Match Count | 131 |
| Dominant Direction | BULLISH |
| Direction % | 67.2% |
| Mag ATR Mean | 1.7537 |
| Mag ATR Std | 0.8137 |
| Mag CV | 0.464 |
| Timing (candles) | 3.84 |
| Persistence | 3.57 |
| Frequency | 2.2512% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     83 samples  bullish   65.1%  mag_atr=1.8148
    val       20 samples  bullish   65.0%  mag_atr=1.4563
    oos       28 samples  bullish   75.0%  mag_atr=1.7849
```

> When [STO_K_21_oversold + ADX_trending + EMA21_below_EMA50 + EMA21_above_Close + EMA50_above_EMA200] occurs, price historically reacts BULLISH 67.2% of the time with an average move of 1.75 ATR (moderate variance) and stable repetition across validation splits.

---

## #11 — `STO_K_21_oversold + ADX_trending + EMA21_below_EMA50 + EMA50_above_EMA200 + close_below_EMA21`

| Field | Value |
|---|---|
| Consistency Score | **0.7174** |
| Match Count | 131 |
| Dominant Direction | BULLISH |
| Direction % | 67.2% |
| Mag ATR Mean | 1.7537 |
| Mag ATR Std | 0.8137 |
| Mag CV | 0.464 |
| Timing (candles) | 3.84 |
| Persistence | 3.57 |
| Frequency | 2.2512% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     83 samples  bullish   65.1%  mag_atr=1.8148
    val       20 samples  bullish   65.0%  mag_atr=1.4563
    oos       28 samples  bullish   75.0%  mag_atr=1.7849
```

> When [STO_K_21_oversold + ADX_trending + EMA21_below_EMA50 + EMA50_above_EMA200 + close_below_EMA21] occurs, price historically reacts BULLISH 67.2% of the time with an average move of 1.75 ATR (moderate variance) and stable repetition across validation splits.

---

## #12 — `RSI7_overbought + EMA50_above_EMA200 + close_above_BB_UPPER_20_2 + CCI21_overbought + ATR14_above_ATR21`

| Field | Value |
|---|---|
| Consistency Score | **0.7134** |
| Match Count | 118 |
| Dominant Direction | BULLISH |
| Direction % | 66.1% |
| Mag ATR Mean | 2.2714 |
| Mag ATR Std | 0.9669 |
| Mag CV | 0.4257 |
| Timing (candles) | 4.02 |
| Persistence | 3.14 |
| Frequency | 2.0278% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     64 samples  bullish   73.4%  mag_atr=2.1925
    val       26 samples  bullish   57.7%  mag_atr=2.2966
    oos       28 samples  bullish   57.1%  mag_atr=2.4284
```

> When [RSI7_overbought + EMA50_above_EMA200 + close_above_BB_UPPER_20_2 + CCI21_overbought + ATR14_above_ATR21] occurs, price historically reacts BULLISH 66.1% of the time with an average move of 2.27 ATR (moderate variance) and stable repetition across validation splits.

---

## #13 — `ADX_trending + EMA21_above_Close + EMA50_above_EMA200 + close_below_EMA200 + MACD_12_26_bull_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.7129** |
| Match Count | 114 |
| Dominant Direction | BULLISH |
| Direction % | 69.3% |
| Mag ATR Mean | 1.6578 |
| Mag ATR Std | 0.7431 |
| Mag CV | 0.4482 |
| Timing (candles) | 3.82 |
| Persistence | 3.46 |
| Frequency | 1.9591% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     62 samples  bullish   79.0%  mag_atr=1.734
    val       29 samples  bullish   55.2%  mag_atr=1.4514
    oos       23 samples  bullish   60.9%  mag_atr=1.7127
```

> When [ADX_trending + EMA21_above_Close + EMA50_above_EMA200 + close_below_EMA200 + MACD_12_26_bull_cross] occurs, price historically reacts BULLISH 69.3% of the time with an average move of 1.66 ATR (moderate variance) and stable repetition across validation splits.

---

## #14 — `ADX_trending + EMA50_above_EMA200 + close_below_EMA21 + close_below_EMA200 + MACD_12_26_bull_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.7129** |
| Match Count | 114 |
| Dominant Direction | BULLISH |
| Direction % | 69.3% |
| Mag ATR Mean | 1.6578 |
| Mag ATR Std | 0.7431 |
| Mag CV | 0.4482 |
| Timing (candles) | 3.82 |
| Persistence | 3.46 |
| Frequency | 1.9591% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     62 samples  bullish   79.0%  mag_atr=1.734
    val       29 samples  bullish   55.2%  mag_atr=1.4514
    oos       23 samples  bullish   60.9%  mag_atr=1.7127
```

> When [ADX_trending + EMA50_above_EMA200 + close_below_EMA21 + close_below_EMA200 + MACD_12_26_bull_cross] occurs, price historically reacts BULLISH 69.3% of the time with an average move of 1.66 ATR (moderate variance) and stable repetition across validation splits.

---

## #15 — `EMA21_above_EMA50 + EMA50_above_EMA200 + close_above_BB_UPPER_20_2 + CCI21_overbought + ATR14_above_ATR21`

| Field | Value |
|---|---|
| Consistency Score | **0.7105** |
| Match Count | 116 |
| Dominant Direction | BULLISH |
| Direction % | 65.5% |
| Mag ATR Mean | 2.2896 |
| Mag ATR Std | 0.9649 |
| Mag CV | 0.4214 |
| Timing (candles) | 4.02 |
| Persistence | 3.11 |
| Frequency | 1.9935% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     62 samples  bullish   72.6%  mag_atr=2.224
    val       26 samples  bullish   57.7%  mag_atr=2.2966
    oos       28 samples  bullish   57.1%  mag_atr=2.4284
```

> When [EMA21_above_EMA50 + EMA50_above_EMA200 + close_above_BB_UPPER_20_2 + CCI21_overbought + ATR14_above_ATR21] occurs, price historically reacts BULLISH 65.5% of the time with an average move of 2.29 ATR (moderate variance) and stable repetition across validation splits.

---

## #16 — `EMA50_above_EMA200 + close_above_BB_UPPER_20_2 + CCI21_overbought + ATR14_above_ATR21`

| Field | Value |
|---|---|
| Consistency Score | **0.7100** |
| Match Count | 120 |
| Dominant Direction | BULLISH |
| Direction % | 65.0% |
| Mag ATR Mean | 2.2546 |
| Mag ATR Std | 0.9691 |
| Mag CV | 0.4298 |
| Timing (candles) | 4.0 |
| Persistence | 3.1 |
| Frequency | 2.0622% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     64 samples  bullish   73.4%  mag_atr=2.1925
    val       28 samples  bullish   53.6%  mag_atr=2.2226
    oos       28 samples  bullish   57.1%  mag_atr=2.4284
```

> When [EMA50_above_EMA200 + close_above_BB_UPPER_20_2 + CCI21_overbought + ATR14_above_ATR21] occurs, price historically reacts BULLISH 65.0% of the time with an average move of 2.25 ATR (moderate variance) and stable repetition across validation splits.

---

## #17 — `EMA13_above_EMA21 + EMA50_above_EMA200 + close_above_BB_UPPER_20_2 + CCI21_overbought + ATR14_above_ATR21`

| Field | Value |
|---|---|
| Consistency Score | **0.7100** |
| Match Count | 120 |
| Dominant Direction | BULLISH |
| Direction % | 65.0% |
| Mag ATR Mean | 2.2546 |
| Mag ATR Std | 0.9691 |
| Mag CV | 0.4298 |
| Timing (candles) | 4.0 |
| Persistence | 3.1 |
| Frequency | 2.0622% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     64 samples  bullish   73.4%  mag_atr=2.1925
    val       28 samples  bullish   53.6%  mag_atr=2.2226
    oos       28 samples  bullish   57.1%  mag_atr=2.4284
```

> When [EMA13_above_EMA21 + EMA50_above_EMA200 + close_above_BB_UPPER_20_2 + CCI21_overbought + ATR14_above_ATR21] occurs, price historically reacts BULLISH 65.0% of the time with an average move of 2.25 ATR (moderate variance) and stable repetition across validation splits.

---

## #18 — `EMA21_below_Close + EMA50_above_EMA200 + close_above_BB_UPPER_20_2 + CCI21_overbought + ATR14_above_ATR21`

| Field | Value |
|---|---|
| Consistency Score | **0.7100** |
| Match Count | 120 |
| Dominant Direction | BULLISH |
| Direction % | 65.0% |
| Mag ATR Mean | 2.2546 |
| Mag ATR Std | 0.9691 |
| Mag CV | 0.4298 |
| Timing (candles) | 4.0 |
| Persistence | 3.1 |
| Frequency | 2.0622% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     64 samples  bullish   73.4%  mag_atr=2.1925
    val       28 samples  bullish   53.6%  mag_atr=2.2226
    oos       28 samples  bullish   57.1%  mag_atr=2.4284
```

> When [EMA21_below_Close + EMA50_above_EMA200 + close_above_BB_UPPER_20_2 + CCI21_overbought + ATR14_above_ATR21] occurs, price historically reacts BULLISH 65.0% of the time with an average move of 2.25 ATR (moderate variance) and stable repetition across validation splits.

---

## #19 — `EMA50_above_EMA200 + close_above_EMA21 + close_above_BB_UPPER_20_2 + CCI21_overbought + ATR14_above_ATR21`

| Field | Value |
|---|---|
| Consistency Score | **0.7100** |
| Match Count | 120 |
| Dominant Direction | BULLISH |
| Direction % | 65.0% |
| Mag ATR Mean | 2.2546 |
| Mag ATR Std | 0.9691 |
| Mag CV | 0.4298 |
| Timing (candles) | 4.0 |
| Persistence | 3.1 |
| Frequency | 2.0622% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     64 samples  bullish   73.4%  mag_atr=2.1925
    val       28 samples  bullish   53.6%  mag_atr=2.2226
    oos       28 samples  bullish   57.1%  mag_atr=2.4284
```

> When [EMA50_above_EMA200 + close_above_EMA21 + close_above_BB_UPPER_20_2 + CCI21_overbought + ATR14_above_ATR21] occurs, price historically reacts BULLISH 65.0% of the time with an average move of 2.25 ATR (moderate variance) and stable repetition across validation splits.

---

## #20 — `EMA50_above_EMA200 + close_above_EMA200 + close_above_BB_UPPER_20_2 + CCI21_overbought + ATR14_above_ATR21`

| Field | Value |
|---|---|
| Consistency Score | **0.7100** |
| Match Count | 120 |
| Dominant Direction | BULLISH |
| Direction % | 65.0% |
| Mag ATR Mean | 2.2546 |
| Mag ATR Std | 0.9691 |
| Mag CV | 0.4298 |
| Timing (candles) | 4.0 |
| Persistence | 3.1 |
| Frequency | 2.0622% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     64 samples  bullish   73.4%  mag_atr=2.1925
    val       28 samples  bullish   53.6%  mag_atr=2.2226
    oos       28 samples  bullish   57.1%  mag_atr=2.4284
```

> When [EMA50_above_EMA200 + close_above_EMA200 + close_above_BB_UPPER_20_2 + CCI21_overbought + ATR14_above_ATR21] occurs, price historically reacts BULLISH 65.0% of the time with an average move of 2.25 ATR (moderate variance) and stable repetition across validation splits.

---

## #21 — `EMA50_above_EMA200 + close_above_BB_UPPER_20_2 + MACD_12_26_hist_positive + CCI21_overbought + ATR14_above_ATR21`

| Field | Value |
|---|---|
| Consistency Score | **0.7100** |
| Match Count | 120 |
| Dominant Direction | BULLISH |
| Direction % | 65.0% |
| Mag ATR Mean | 2.2546 |
| Mag ATR Std | 0.9691 |
| Mag CV | 0.4298 |
| Timing (candles) | 4.0 |
| Persistence | 3.1 |
| Frequency | 2.0622% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     64 samples  bullish   73.4%  mag_atr=2.1925
    val       28 samples  bullish   53.6%  mag_atr=2.2226
    oos       28 samples  bullish   57.1%  mag_atr=2.4284
```

> When [EMA50_above_EMA200 + close_above_BB_UPPER_20_2 + MACD_12_26_hist_positive + CCI21_overbought + ATR14_above_ATR21] occurs, price historically reacts BULLISH 65.0% of the time with an average move of 2.25 ATR (moderate variance) and stable repetition across validation splits.

---

## #22 — `EMA50_above_EMA200 + close_above_BB_UPPER_20_2 + CCI21_overbought + ATR14_above_ATR21 + ATR7_above_ATR13`

| Field | Value |
|---|---|
| Consistency Score | **0.7026** |
| Match Count | 113 |
| Dominant Direction | BULLISH |
| Direction % | 65.5% |
| Mag ATR Mean | 2.2262 |
| Mag ATR Std | 0.9529 |
| Mag CV | 0.428 |
| Timing (candles) | 3.99 |
| Persistence | 3.14 |
| Frequency | 1.9419% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     60 samples  bullish   71.7%  mag_atr=2.1963
    val       27 samples  bullish   55.6%  mag_atr=2.2454
    oos       26 samples  bullish   61.5%  mag_atr=2.275
```

> When [EMA50_above_EMA200 + close_above_BB_UPPER_20_2 + CCI21_overbought + ATR14_above_ATR21 + ATR7_above_ATR13] occurs, price historically reacts BULLISH 65.5% of the time with an average move of 2.23 ATR (moderate variance) and stable repetition across validation splits.

---

## #23 — `ADX_trending + EMA13_below_EMA21 + EMA50_above_EMA200 + close_below_EMA200 + MACD_8_21_bull_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.7011** |
| Match Count | 107 |
| Dominant Direction | BULLISH |
| Direction % | 71.0% |
| Mag ATR Mean | 1.5528 |
| Mag ATR Std | 0.7187 |
| Mag CV | 0.4628 |
| Timing (candles) | 3.77 |
| Persistence | 3.5 |
| Frequency | 1.8388% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     60 samples  bullish   83.3%  mag_atr=1.6057
    val       25 samples  bullish   52.0%  mag_atr=1.3544
    oos       22 samples  bullish   59.1%  mag_atr=1.6342
```

> When [ADX_trending + EMA13_below_EMA21 + EMA50_above_EMA200 + close_below_EMA200 + MACD_8_21_bull_cross] occurs, price historically reacts BULLISH 71.0% of the time with an average move of 1.55 ATR (moderate variance) and stable repetition across validation splits.

---

## #24 — `STO_K_14_oversold + ADX_trending + EMA21_below_EMA50 + EMA50_above_EMA200`

| Field | Value |
|---|---|
| Consistency Score | **0.6897** |
| Match Count | 105 |
| Dominant Direction | BULLISH |
| Direction % | 68.6% |
| Mag ATR Mean | 1.7269 |
| Mag ATR Std | 0.7898 |
| Mag CV | 0.4574 |
| Timing (candles) | 3.84 |
| Persistence | 3.54 |
| Frequency | 1.8044% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     62 samples  bullish   66.1%  mag_atr=1.8222
    val       19 samples  bullish   68.4%  mag_atr=1.4876
    oos       24 samples  bullish   75.0%  mag_atr=1.6699
```

> When [STO_K_14_oversold + ADX_trending + EMA21_below_EMA50 + EMA50_above_EMA200] occurs, price historically reacts BULLISH 68.6% of the time with an average move of 1.73 ATR (moderate variance) and stable repetition across validation splits.

---

## #25 — `STO_K_14_oversold + ADX_trending + EMA13_below_EMA21 + EMA21_below_EMA50 + EMA50_above_EMA200`

| Field | Value |
|---|---|
| Consistency Score | **0.6897** |
| Match Count | 105 |
| Dominant Direction | BULLISH |
| Direction % | 68.6% |
| Mag ATR Mean | 1.7269 |
| Mag ATR Std | 0.7898 |
| Mag CV | 0.4574 |
| Timing (candles) | 3.84 |
| Persistence | 3.54 |
| Frequency | 1.8044% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     62 samples  bullish   66.1%  mag_atr=1.8222
    val       19 samples  bullish   68.4%  mag_atr=1.4876
    oos       24 samples  bullish   75.0%  mag_atr=1.6699
```

> When [STO_K_14_oversold + ADX_trending + EMA13_below_EMA21 + EMA21_below_EMA50 + EMA50_above_EMA200] occurs, price historically reacts BULLISH 68.6% of the time with an average move of 1.73 ATR (moderate variance) and stable repetition across validation splits.

---

## #26 — `STO_K_14_oversold + ADX_trending + EMA21_below_EMA50 + EMA21_above_Close + EMA50_above_EMA200`

| Field | Value |
|---|---|
| Consistency Score | **0.6897** |
| Match Count | 105 |
| Dominant Direction | BULLISH |
| Direction % | 68.6% |
| Mag ATR Mean | 1.7269 |
| Mag ATR Std | 0.7898 |
| Mag CV | 0.4574 |
| Timing (candles) | 3.84 |
| Persistence | 3.54 |
| Frequency | 1.8044% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     62 samples  bullish   66.1%  mag_atr=1.8222
    val       19 samples  bullish   68.4%  mag_atr=1.4876
    oos       24 samples  bullish   75.0%  mag_atr=1.6699
```

> When [STO_K_14_oversold + ADX_trending + EMA21_below_EMA50 + EMA21_above_Close + EMA50_above_EMA200] occurs, price historically reacts BULLISH 68.6% of the time with an average move of 1.73 ATR (moderate variance) and stable repetition across validation splits.

---

## #27 — `STO_K_14_oversold + ADX_trending + EMA21_below_EMA50 + EMA50_above_EMA200 + close_below_EMA21`

| Field | Value |
|---|---|
| Consistency Score | **0.6897** |
| Match Count | 105 |
| Dominant Direction | BULLISH |
| Direction % | 68.6% |
| Mag ATR Mean | 1.7269 |
| Mag ATR Std | 0.7898 |
| Mag CV | 0.4574 |
| Timing (candles) | 3.84 |
| Persistence | 3.54 |
| Frequency | 1.8044% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     62 samples  bullish   66.1%  mag_atr=1.8222
    val       19 samples  bullish   68.4%  mag_atr=1.4876
    oos       24 samples  bullish   75.0%  mag_atr=1.6699
```

> When [STO_K_14_oversold + ADX_trending + EMA21_below_EMA50 + EMA50_above_EMA200 + close_below_EMA21] occurs, price historically reacts BULLISH 68.6% of the time with an average move of 1.73 ATR (moderate variance) and stable repetition across validation splits.

---

## #28 — `STO_K_14_oversold + STO_K_21_oversold + ADX_trending + EMA21_below_EMA50 + EMA50_above_EMA200`

| Field | Value |
|---|---|
| Consistency Score | **0.6863** |
| Match Count | 104 |
| Dominant Direction | BULLISH |
| Direction % | 68.3% |
| Mag ATR Mean | 1.7289 |
| Mag ATR Std | 0.7933 |
| Mag CV | 0.4588 |
| Timing (candles) | 3.83 |
| Persistence | 3.56 |
| Frequency | 1.7872% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     61 samples  bullish   65.6%  mag_atr=1.8272
    val       19 samples  bullish   68.4%  mag_atr=1.4876
    oos       24 samples  bullish   75.0%  mag_atr=1.6699
```

> When [STO_K_14_oversold + STO_K_21_oversold + ADX_trending + EMA21_below_EMA50 + EMA50_above_EMA200] occurs, price historically reacts BULLISH 68.3% of the time with an average move of 1.73 ATR (moderate variance) and stable repetition across validation splits.

---

## #29 — `RSI7_overbought + MACD_12_26_bear_cross + CCI14_overbought + ATR14_above_ATR21 + ATR7_above_ATR13`

| Field | Value |
|---|---|
| Consistency Score | **0.6812** |
| Match Count | 107 |
| Dominant Direction | BULLISH |
| Direction % | 65.4% |
| Mag ATR Mean | 2.3285 |
| Mag ATR Std | 1.0797 |
| Mag CV | 0.4637 |
| Timing (candles) | 3.93 |
| Persistence | 3.13 |
| Frequency | 1.8388% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     59 samples  bullish   64.4%  mag_atr=2.3492
    val       28 samples  bullish   60.7%  mag_atr=2.2643
    oos       20 samples  bullish   75.0%  mag_atr=2.3573
```

> When [RSI7_overbought + MACD_12_26_bear_cross + CCI14_overbought + ATR14_above_ATR21 + ATR7_above_ATR13] occurs, price historically reacts BULLISH 65.4% of the time with an average move of 2.33 ATR (moderate variance) and stable repetition across validation splits.

---

## #30 — `STO_D_21_overbought + MACD_12_26_bear_cross + CCI14_overbought + ATR14_above_ATR21 + ATR7_above_ATR13`

| Field | Value |
|---|---|
| Consistency Score | **0.6808** |
| Match Count | 106 |
| Dominant Direction | BULLISH |
| Direction % | 65.1% |
| Mag ATR Mean | 2.4059 |
| Mag ATR Std | 1.0886 |
| Mag CV | 0.4525 |
| Timing (candles) | 4.0 |
| Persistence | 3.16 |
| Frequency | 1.8216% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     60 samples  bullish   60.0%  mag_atr=2.4054
    val       28 samples  bullish   67.9%  mag_atr=2.3809
    oos       18 samples  bullish   77.8%  mag_atr=2.4465
```

> When [STO_D_21_overbought + MACD_12_26_bear_cross + CCI14_overbought + ATR14_above_ATR21 + ATR7_above_ATR13] occurs, price historically reacts BULLISH 65.1% of the time with an average move of 2.41 ATR (moderate variance) and stable repetition across validation splits.

---

## #31 — `STO_D_21_overbought + EMA50_above_EMA200 + close_above_BB_UPPER_20_2 + CCI21_overbought + ATR14_above_ATR21`

| Field | Value |
|---|---|
| Consistency Score | **0.6771** |
| Match Count | 101 |
| Dominant Direction | BULLISH |
| Direction % | 65.3% |
| Mag ATR Mean | 2.3195 |
| Mag ATR Std | 0.998 |
| Mag CV | 0.4303 |
| Timing (candles) | 4.08 |
| Persistence | 3.14 |
| Frequency | 1.7357% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     56 samples  bullish   71.4%  mag_atr=2.2519
    val       23 samples  bullish   60.9%  mag_atr=2.3343
    oos       22 samples  bullish   54.5%  mag_atr=2.476
```

> When [STO_D_21_overbought + EMA50_above_EMA200 + close_above_BB_UPPER_20_2 + CCI21_overbought + ATR14_above_ATR21] occurs, price historically reacts BULLISH 65.3% of the time with an average move of 2.32 ATR (moderate variance) and stable repetition across validation splits.

---

## #32 — `ADX_trending + EMA21_above_Close + EMA50_above_EMA100 + MACD_12_26_bull_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.6766** |
| Match Count | 125 |
| Dominant Direction | BULLISH |
| Direction % | 65.6% |
| Mag ATR Mean | 1.7176 |
| Mag ATR Std | 0.7795 |
| Mag CV | 0.4538 |
| Timing (candles) | 3.93 |
| Persistence | 3.23 |
| Frequency | 2.1481% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     96 samples  bullish   58.3%  mag_atr=1.689
    val     [insufficient]
    oos       27 samples  bullish   88.9%  mag_atr=1.8385
```

> When [ADX_trending + EMA21_above_Close + EMA50_above_EMA100 + MACD_12_26_bull_cross] occurs, price historically reacts BULLISH 65.6% of the time with an average move of 1.72 ATR (moderate variance) and stable repetition across validation splits.

---

## #33 — `ADX_trending + EMA50_above_EMA100 + close_below_EMA21 + MACD_12_26_bull_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.6766** |
| Match Count | 125 |
| Dominant Direction | BULLISH |
| Direction % | 65.6% |
| Mag ATR Mean | 1.7176 |
| Mag ATR Std | 0.7795 |
| Mag CV | 0.4538 |
| Timing (candles) | 3.93 |
| Persistence | 3.23 |
| Frequency | 2.1481% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     96 samples  bullish   58.3%  mag_atr=1.689
    val     [insufficient]
    oos       27 samples  bullish   88.9%  mag_atr=1.8385
```

> When [ADX_trending + EMA50_above_EMA100 + close_below_EMA21 + MACD_12_26_bull_cross] occurs, price historically reacts BULLISH 65.6% of the time with an average move of 1.72 ATR (moderate variance) and stable repetition across validation splits.

---

## #34 — `ADX_trending + EMA13_below_EMA21 + EMA21_above_Close + EMA50_above_EMA100 + MACD_12_26_bull_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.6766** |
| Match Count | 125 |
| Dominant Direction | BULLISH |
| Direction % | 65.6% |
| Mag ATR Mean | 1.7176 |
| Mag ATR Std | 0.7795 |
| Mag CV | 0.4538 |
| Timing (candles) | 3.93 |
| Persistence | 3.23 |
| Frequency | 2.1481% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     96 samples  bullish   58.3%  mag_atr=1.689
    val     [insufficient]
    oos       27 samples  bullish   88.9%  mag_atr=1.8385
```

> When [ADX_trending + EMA13_below_EMA21 + EMA21_above_Close + EMA50_above_EMA100 + MACD_12_26_bull_cross] occurs, price historically reacts BULLISH 65.6% of the time with an average move of 1.72 ATR (moderate variance) and stable repetition across validation splits.

---

## #35 — `ADX_trending + EMA13_below_EMA21 + EMA50_above_EMA100 + close_below_EMA21 + MACD_12_26_bull_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.6766** |
| Match Count | 125 |
| Dominant Direction | BULLISH |
| Direction % | 65.6% |
| Mag ATR Mean | 1.7176 |
| Mag ATR Std | 0.7795 |
| Mag CV | 0.4538 |
| Timing (candles) | 3.93 |
| Persistence | 3.23 |
| Frequency | 2.1481% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     96 samples  bullish   58.3%  mag_atr=1.689
    val     [insufficient]
    oos       27 samples  bullish   88.9%  mag_atr=1.8385
```

> When [ADX_trending + EMA13_below_EMA21 + EMA50_above_EMA100 + close_below_EMA21 + MACD_12_26_bull_cross] occurs, price historically reacts BULLISH 65.6% of the time with an average move of 1.72 ATR (moderate variance) and stable repetition across validation splits.

---

## #36 — `ADX_trending + EMA21_above_Close + EMA50_above_EMA100 + close_below_EMA21 + MACD_12_26_bull_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.6766** |
| Match Count | 125 |
| Dominant Direction | BULLISH |
| Direction % | 65.6% |
| Mag ATR Mean | 1.7176 |
| Mag ATR Std | 0.7795 |
| Mag CV | 0.4538 |
| Timing (candles) | 3.93 |
| Persistence | 3.23 |
| Frequency | 2.1481% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     96 samples  bullish   58.3%  mag_atr=1.689
    val     [insufficient]
    oos       27 samples  bullish   88.9%  mag_atr=1.8385
```

> When [ADX_trending + EMA21_above_Close + EMA50_above_EMA100 + close_below_EMA21 + MACD_12_26_bull_cross] occurs, price historically reacts BULLISH 65.6% of the time with an average move of 1.72 ATR (moderate variance) and stable repetition across validation splits.

---

## #37 — `ADX_trending + EMA21_below_EMA50 + EMA21_above_Close + EMA50_above_EMA100 + MACD_12_26_bull_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.6743** |
| Match Count | 124 |
| Dominant Direction | BULLISH |
| Direction % | 65.3% |
| Mag ATR Mean | 1.7132 |
| Mag ATR Std | 0.781 |
| Mag CV | 0.4559 |
| Timing (candles) | 3.92 |
| Persistence | 3.24 |
| Frequency | 2.131% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     96 samples  bullish   58.3%  mag_atr=1.689
    val     [insufficient]
    oos       26 samples  bullish   88.5%  mag_atr=1.822
```

> When [ADX_trending + EMA21_below_EMA50 + EMA21_above_Close + EMA50_above_EMA100 + MACD_12_26_bull_cross] occurs, price historically reacts BULLISH 65.3% of the time with an average move of 1.71 ATR (moderate variance) and stable repetition across validation splits.

---

## #38 — `ADX_trending + EMA21_below_EMA50 + EMA50_above_EMA100 + close_below_EMA21 + MACD_12_26_bull_cross`

| Field | Value |
|---|---|
| Consistency Score | **0.6743** |
| Match Count | 124 |
| Dominant Direction | BULLISH |
| Direction % | 65.3% |
| Mag ATR Mean | 1.7132 |
| Mag ATR Std | 0.781 |
| Mag CV | 0.4559 |
| Timing (candles) | 3.92 |
| Persistence | 3.24 |
| Frequency | 2.131% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     96 samples  bullish   58.3%  mag_atr=1.689
    val     [insufficient]
    oos       26 samples  bullish   88.5%  mag_atr=1.822
```

> When [ADX_trending + EMA21_below_EMA50 + EMA50_above_EMA100 + close_below_EMA21 + MACD_12_26_bull_cross] occurs, price historically reacts BULLISH 65.3% of the time with an average move of 1.71 ATR (moderate variance) and stable repetition across validation splits.

---

## #39 — `RSI7_overbought + MACD_9_21_bear_cross + CCI14_overbought + ATR14_above_ATR21 + ATR7_above_ATR13`

| Field | Value |
|---|---|
| Consistency Score | **0.6740** |
| Match Count | 101 |
| Dominant Direction | BULLISH |
| Direction % | 66.3% |
| Mag ATR Mean | 2.3028 |
| Mag ATR Std | 1.0512 |
| Mag CV | 0.4565 |
| Timing (candles) | 3.9 |
| Persistence | 3.19 |
| Frequency | 1.7357% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     57 samples  bullish   63.2%  mag_atr=2.3539
    val       25 samples  bullish   64.0%  mag_atr=2.1911
    oos       19 samples  bullish   79.0%  mag_atr=2.2963
```

> When [RSI7_overbought + MACD_9_21_bear_cross + CCI14_overbought + ATR14_above_ATR21 + ATR7_above_ATR13] occurs, price historically reacts BULLISH 66.3% of the time with an average move of 2.30 ATR (moderate variance) and stable repetition across validation splits.

---

## #40 — `STO_D_21_overbought + MACD_9_21_bear_cross + CCI14_overbought + ATR14_above_ATR21 + ATR7_above_ATR13`

| Field | Value |
|---|---|
| Consistency Score | **0.6735** |
| Match Count | 100 |
| Dominant Direction | BULLISH |
| Direction % | 66.0% |
| Mag ATR Mean | 2.3846 |
| Mag ATR Std | 1.0624 |
| Mag CV | 0.4455 |
| Timing (candles) | 3.97 |
| Persistence | 3.22 |
| Frequency | 1.7185% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     58 samples  bullish   58.6%  mag_atr=2.412
    val       25 samples  bullish   72.0%  mag_atr=2.3217
    oos       17 samples  bullish   82.3%  mag_atr=2.3835
```

> When [STO_D_21_overbought + MACD_9_21_bear_cross + CCI14_overbought + ATR14_above_ATR21 + ATR7_above_ATR13] occurs, price historically reacts BULLISH 66.0% of the time with an average move of 2.38 ATR (moderate variance) and stable repetition across validation splits.

---

## #41 — `EMA50_above_EMA100 + close_above_BB_UPPER_20_2 + MACD_12_26_bear_cross + ATR7_above_ATR13`

| Field | Value |
|---|---|
| Consistency Score | **0.6667** |
| Match Count | 103 |
| Dominant Direction | BULLISH |
| Direction % | 65.0% |
| Mag ATR Mean | 2.3137 |
| Mag ATR Std | 1.1195 |
| Mag CV | 0.4839 |
| Timing (candles) | 4.12 |
| Persistence | 3.17 |
| Frequency | 1.7701% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     59 samples  bullish   66.1%  mag_atr=2.2444
    val       28 samples  bullish   60.7%  mag_atr=2.5403
    oos       16 samples  bullish   68.8%  mag_atr=2.1723
```

> When [EMA50_above_EMA100 + close_above_BB_UPPER_20_2 + MACD_12_26_bear_cross + ATR7_above_ATR13] occurs, price historically reacts BULLISH 65.0% of the time with an average move of 2.31 ATR (moderate variance) and stable repetition across validation splits.

---

## #42 — `EMA13_above_EMA21 + EMA50_above_EMA100 + close_above_BB_UPPER_20_2 + MACD_12_26_bear_cross + ATR7_above_ATR13`

| Field | Value |
|---|---|
| Consistency Score | **0.6667** |
| Match Count | 103 |
| Dominant Direction | BULLISH |
| Direction % | 65.0% |
| Mag ATR Mean | 2.3137 |
| Mag ATR Std | 1.1195 |
| Mag CV | 0.4839 |
| Timing (candles) | 4.12 |
| Persistence | 3.17 |
| Frequency | 1.7701% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     59 samples  bullish   66.1%  mag_atr=2.2444
    val       28 samples  bullish   60.7%  mag_atr=2.5403
    oos       16 samples  bullish   68.8%  mag_atr=2.1723
```

> When [EMA13_above_EMA21 + EMA50_above_EMA100 + close_above_BB_UPPER_20_2 + MACD_12_26_bear_cross + ATR7_above_ATR13] occurs, price historically reacts BULLISH 65.0% of the time with an average move of 2.31 ATR (moderate variance) and stable repetition across validation splits.

---

## #43 — `EMA21_above_EMA50 + EMA50_above_EMA100 + close_above_BB_UPPER_20_2 + MACD_12_26_bear_cross + ATR7_above_ATR13`

| Field | Value |
|---|---|
| Consistency Score | **0.6667** |
| Match Count | 103 |
| Dominant Direction | BULLISH |
| Direction % | 65.0% |
| Mag ATR Mean | 2.3137 |
| Mag ATR Std | 1.1195 |
| Mag CV | 0.4839 |
| Timing (candles) | 4.12 |
| Persistence | 3.17 |
| Frequency | 1.7701% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     59 samples  bullish   66.1%  mag_atr=2.2444
    val       28 samples  bullish   60.7%  mag_atr=2.5403
    oos       16 samples  bullish   68.8%  mag_atr=2.1723
```

> When [EMA21_above_EMA50 + EMA50_above_EMA100 + close_above_BB_UPPER_20_2 + MACD_12_26_bear_cross + ATR7_above_ATR13] occurs, price historically reacts BULLISH 65.0% of the time with an average move of 2.31 ATR (moderate variance) and stable repetition across validation splits.

---

## #44 — `EMA21_below_Close + EMA50_above_EMA100 + close_above_BB_UPPER_20_2 + MACD_12_26_bear_cross + ATR7_above_ATR13`

| Field | Value |
|---|---|
| Consistency Score | **0.6667** |
| Match Count | 103 |
| Dominant Direction | BULLISH |
| Direction % | 65.0% |
| Mag ATR Mean | 2.3137 |
| Mag ATR Std | 1.1195 |
| Mag CV | 0.4839 |
| Timing (candles) | 4.12 |
| Persistence | 3.17 |
| Frequency | 1.7701% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     59 samples  bullish   66.1%  mag_atr=2.2444
    val       28 samples  bullish   60.7%  mag_atr=2.5403
    oos       16 samples  bullish   68.8%  mag_atr=2.1723
```

> When [EMA21_below_Close + EMA50_above_EMA100 + close_above_BB_UPPER_20_2 + MACD_12_26_bear_cross + ATR7_above_ATR13] occurs, price historically reacts BULLISH 65.0% of the time with an average move of 2.31 ATR (moderate variance) and stable repetition across validation splits.

---

## #45 — `EMA50_above_EMA100 + close_above_EMA21 + close_above_BB_UPPER_20_2 + MACD_12_26_bear_cross + ATR7_above_ATR13`

| Field | Value |
|---|---|
| Consistency Score | **0.6667** |
| Match Count | 103 |
| Dominant Direction | BULLISH |
| Direction % | 65.0% |
| Mag ATR Mean | 2.3137 |
| Mag ATR Std | 1.1195 |
| Mag CV | 0.4839 |
| Timing (candles) | 4.12 |
| Persistence | 3.17 |
| Frequency | 1.7701% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     59 samples  bullish   66.1%  mag_atr=2.2444
    val       28 samples  bullish   60.7%  mag_atr=2.5403
    oos       16 samples  bullish   68.8%  mag_atr=2.1723
```

> When [EMA50_above_EMA100 + close_above_EMA21 + close_above_BB_UPPER_20_2 + MACD_12_26_bear_cross + ATR7_above_ATR13] occurs, price historically reacts BULLISH 65.0% of the time with an average move of 2.31 ATR (moderate variance) and stable repetition across validation splits.

---

## #46 — `EMA50_above_EMA100 + close_above_EMA200 + close_above_BB_UPPER_20_2 + MACD_12_26_bear_cross + ATR7_above_ATR13`

| Field | Value |
|---|---|
| Consistency Score | **0.6667** |
| Match Count | 103 |
| Dominant Direction | BULLISH |
| Direction % | 65.0% |
| Mag ATR Mean | 2.3137 |
| Mag ATR Std | 1.1195 |
| Mag CV | 0.4839 |
| Timing (candles) | 4.12 |
| Persistence | 3.17 |
| Frequency | 1.7701% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     59 samples  bullish   66.1%  mag_atr=2.2444
    val       28 samples  bullish   60.7%  mag_atr=2.5403
    oos       16 samples  bullish   68.8%  mag_atr=2.1723
```

> When [EMA50_above_EMA100 + close_above_EMA200 + close_above_BB_UPPER_20_2 + MACD_12_26_bear_cross + ATR7_above_ATR13] occurs, price historically reacts BULLISH 65.0% of the time with an average move of 2.31 ATR (moderate variance) and stable repetition across validation splits.

---

## #47 — `STO_K_21_oversold + ADX_trending + EMA21_below_EMA50 + EMA50_above_EMA200 + close_below_EMA200`

| Field | Value |
|---|---|
| Consistency Score | **0.6640** |
| Match Count | 95 |
| Dominant Direction | BULLISH |
| Direction % | 66.3% |
| Mag ATR Mean | 1.7997 |
| Mag ATR Std | 0.8048 |
| Mag CV | 0.4472 |
| Timing (candles) | 3.86 |
| Persistence | 3.51 |
| Frequency | 1.6326% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     51 samples  bullish   64.7%  mag_atr=1.9708
    val       20 samples  bullish   65.0%  mag_atr=1.4563
    oos       24 samples  bullish   70.8%  mag_atr=1.7222
```

> When [STO_K_21_oversold + ADX_trending + EMA21_below_EMA50 + EMA50_above_EMA200 + close_below_EMA200] occurs, price historically reacts BULLISH 66.3% of the time with an average move of 1.80 ATR (moderate variance) and stable repetition across validation splits.

---

## #48 — `EMA50_above_EMA200 + close_above_BB_UPPER_20_2 + close_above_BB_UPPER_50_2 + CCI21_overbought + ATR14_above_ATR21`

| Field | Value |
|---|---|
| Consistency Score | **0.6637** |
| Match Count | 93 |
| Dominant Direction | BULLISH |
| Direction % | 65.6% |
| Mag ATR Mean | 2.2655 |
| Mag ATR Std | 0.9558 |
| Mag CV | 0.4219 |
| Timing (candles) | 3.98 |
| Persistence | 3.18 |
| Frequency | 1.5982% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     56 samples  bullish   71.4%  mag_atr=2.2756
    val       21 samples  bullish   57.1%  mag_atr=2.3515
    oos       16 samples  bullish   56.2%  mag_atr=2.1172
```

> When [EMA50_above_EMA200 + close_above_BB_UPPER_20_2 + close_above_BB_UPPER_50_2 + CCI21_overbought + ATR14_above_ATR21] occurs, price historically reacts BULLISH 65.6% of the time with an average move of 2.27 ATR (moderate variance) and stable repetition across validation splits.

---

## #49 — `RSI7_overbought + EMA50_above_EMA100 + close_above_BB_UPPER_20_2 + MACD_12_26_bear_cross + ATR7_above_ATR13`

| Field | Value |
|---|---|
| Consistency Score | **0.6635** |
| Match Count | 100 |
| Dominant Direction | BULLISH |
| Direction % | 66.0% |
| Mag ATR Mean | 2.3292 |
| Mag ATR Std | 1.1314 |
| Mag CV | 0.4857 |
| Timing (candles) | 4.13 |
| Persistence | 3.19 |
| Frequency | 1.7185% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     57 samples  bullish   66.7%  mag_atr=2.2529
    val       27 samples  bullish   63.0%  mag_atr=2.583
    oos       16 samples  bullish   68.8%  mag_atr=2.1723
```

> When [RSI7_overbought + EMA50_above_EMA100 + close_above_BB_UPPER_20_2 + MACD_12_26_bear_cross + ATR7_above_ATR13] occurs, price historically reacts BULLISH 66.0% of the time with an average move of 2.33 ATR (moderate variance) and stable repetition across validation splits.

---

## #50 — `STO_D_21_overbought + EMA13_above_EMA21 + EMA21_below_EMA50 + close_below_EMA200`

| Field | Value |
|---|---|
| Consistency Score | **0.6634** |
| Match Count | 105 |
| Dominant Direction | BEARISH |
| Direction % | 67.6% |
| Mag ATR Mean | 1.736 |
| Mag ATR Std | 0.7223 |
| Mag CV | 0.4161 |
| Timing (candles) | 3.71 |
| Persistence | 3.28 |
| Frequency | 1.8044% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     66 samples  bearish   75.8%  mag_atr=1.8264
    val     [insufficient]
    oos       25 samples  bearish   60.0%  mag_atr=1.5505
```

> When [STO_D_21_overbought + EMA13_above_EMA21 + EMA21_below_EMA50 + close_below_EMA200] occurs, price historically reacts BEARISH 67.6% of the time with an average move of 1.74 ATR (moderate variance) and stable repetition across validation splits.

---
