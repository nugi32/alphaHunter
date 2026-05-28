# Market Condition Analysis Report

**Lookahead:** 5 candles  
**Min direction:** 55.0%  
**Max mag CV:** 0.85  

---

## #1 — `close_above_EMA200 + vol_spike_3x + CCI14_oversold`

| Field | Value |
|---|---|
| Consistency Score | **0.5711** |
| Match Count | 272 |
| Dominant Direction | BULLISH |
| Direction % | 55.5% |
| Mag ATR Mean | 2.4982 |
| Mag ATR Std | 1.4044 |
| Mag CV | 0.5622 |
| Timing (candles) | 3.16 |
| Persistence | 2.87 |
| Frequency | 0.231% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    211 samples  bullish   56.4%  mag_atr=2.491
    val       21 samples  bullish   57.1%  mag_atr=2.5061
    oos       40 samples  bullish   50.0%  mag_atr=2.5321
```

> When [close_above_EMA200 + vol_spike_3x + CCI14_oversold] occurs, price historically reacts BULLISH 55.5% of the time with an average move of 2.50 ATR (moderate variance) and stable repetition across validation splits.

---

## #2 — `RSI7_oversold + close_above_EMA200 + vol_spike_3x`

| Field | Value |
|---|---|
| Consistency Score | **0.5439** |
| Match Count | 186 |
| Dominant Direction | BULLISH |
| Direction % | 55.4% |
| Mag ATR Mean | 2.6824 |
| Mag ATR Std | 1.623 |
| Mag CV | 0.6051 |
| Timing (candles) | 3.19 |
| Persistence | 2.84 |
| Frequency | 0.158% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    145 samples  bullish   55.2%  mag_atr=2.6689
    val       16 samples  bullish   50.0%  mag_atr=2.5284
    oos       25 samples  bullish   60.0%  mag_atr=2.8589
```

> When [RSI7_oversold + close_above_EMA200 + vol_spike_3x] occurs, price historically reacts BULLISH 55.4% of the time with an average move of 2.68 ATR (high variance) and stable repetition across validation splits.

---

## #3 — `RSI7_oversold + vol_spike_3x + squeeze_active`

| Field | Value |
|---|---|
| Consistency Score | **0.5340** |
| Match Count | 136 |
| Dominant Direction | BULLISH |
| Direction % | 57.4% |
| Mag ATR Mean | 2.7717 |
| Mag ATR Std | 1.4124 |
| Mag CV | 0.5096 |
| Timing (candles) | 3.1 |
| Persistence | 2.97 |
| Frequency | 0.1155% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     87 samples  bullish   59.8%  mag_atr=2.8671
    val       17 samples  bullish   64.7%  mag_atr=2.5676
    oos       32 samples  bullish   46.9%  mag_atr=2.6209
```

> When [RSI7_oversold + vol_spike_3x + squeeze_active] occurs, price historically reacts BULLISH 57.4% of the time with an average move of 2.77 ATR (moderate variance) and stable repetition across validation splits.

---

## #4 — `EMA50_below_EMA100 + bull_engulf + breakout_up`

| Field | Value |
|---|---|
| Consistency Score | **0.5231** |
| Match Count | 168 |
| Dominant Direction | BEARISH |
| Direction % | 56.0% |
| Mag ATR Mean | 2.179 |
| Mag ATR Std | 1.3898 |
| Mag CV | 0.6378 |
| Timing (candles) | 3.64 |
| Persistence | 2.83 |
| Frequency | 0.1427% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    118 samples  bearish   57.6%  mag_atr=2.2323
    val       26 samples  bearish   57.7%  mag_atr=1.7992
    oos       24 samples  bearish   45.8%  mag_atr=2.3287
```

> When [EMA50_below_EMA100 + bull_engulf + breakout_up] occurs, price historically reacts BEARISH 56.0% of the time with an average move of 2.18 ATR (high variance) and stable repetition across validation splits.

---

## #5 — `ADX_strong_trend + EMA21_above_EMA50 + breakout_down`

| Field | Value |
|---|---|
| Consistency Score | **0.5179** |
| Match Count | 119 |
| Dominant Direction | BULLISH |
| Direction % | 63.0% |
| Mag ATR Mean | 2.0213 |
| Mag ATR Std | 1.2088 |
| Mag CV | 0.598 |
| Timing (candles) | 3.23 |
| Persistence | 3.31 |
| Frequency | 0.1011% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     78 samples  bullish   61.5%  mag_atr=2.1246
    val       18 samples  bullish   61.1%  mag_atr=1.9698
    oos       23 samples  bullish   69.6%  mag_atr=1.7116
```

> When [ADX_strong_trend + EMA21_above_EMA50 + breakout_down] occurs, price historically reacts BULLISH 63.0% of the time with an average move of 2.02 ATR (moderate variance) and stable repetition across validation splits.

---

## #6 — `EMA50_above_EMA100 + shooting_star + CCI14_oversold`

| Field | Value |
|---|---|
| Consistency Score | **0.5155** |
| Match Count | 175 |
| Dominant Direction | BULLISH |
| Direction % | 57.1% |
| Mag ATR Mean | 2.1451 |
| Mag ATR Std | 1.5174 |
| Mag CV | 0.7074 |
| Timing (candles) | 3.62 |
| Persistence | 2.77 |
| Frequency | 0.1486% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    115 samples  bullish   60.9%  mag_atr=2.1387
    val       36 samples  bullish   52.8%  mag_atr=2.1199
    oos       24 samples  bullish   45.8%  mag_atr=2.2136
```

> When [EMA50_above_EMA100 + shooting_star + CCI14_oversold] occurs, price historically reacts BULLISH 57.1% of the time with an average move of 2.15 ATR (high variance) and stable repetition across validation splits.

---

## #7 — `ADX_strong_trend + close_above_EMA200 + breakout_down`

| Field | Value |
|---|---|
| Consistency Score | **0.5116** |
| Match Count | 116 |
| Dominant Direction | BULLISH |
| Direction % | 61.2% |
| Mag ATR Mean | 2.0399 |
| Mag ATR Std | 1.1998 |
| Mag CV | 0.5882 |
| Timing (candles) | 3.35 |
| Persistence | 3.26 |
| Frequency | 0.0985% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     85 samples  bullish   61.2%  mag_atr=2.1321
    val       18 samples  bullish   44.4%  mag_atr=1.8705
    oos       13 samples  bullish   84.6%  mag_atr=1.6709
```

> When [ADX_strong_trend + close_above_EMA200 + breakout_down] occurs, price historically reacts BULLISH 61.2% of the time with an average move of 2.04 ATR (moderate variance) and stable repetition across validation splits.

---

## #8 — `close_above_EMA200 + shooting_star + CCI14_oversold`

| Field | Value |
|---|---|
| Consistency Score | **0.4671** |
| Match Count | 124 |
| Dominant Direction | BULLISH |
| Direction % | 55.6% |
| Mag ATR Mean | 2.1939 |
| Mag ATR Std | 1.5672 |
| Mag CV | 0.7143 |
| Timing (candles) | 3.55 |
| Persistence | 2.85 |
| Frequency | 0.1053% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     78 samples  bullish   59.0%  mag_atr=2.2092
    val       28 samples  bullish   53.6%  mag_atr=2.2071
    oos       18 samples  bullish   44.4%  mag_atr=2.1071
```

> When [close_above_EMA200 + shooting_star + CCI14_oversold] occurs, price historically reacts BULLISH 55.6% of the time with an average move of 2.19 ATR (high variance) and stable repetition across validation splits.

---

## #9 — `RSI14_overbought + EMA50_below_EMA100 + bull_engulf`

| Field | Value |
|---|---|
| Consistency Score | **0.4663** |
| Match Count | 72 |
| Dominant Direction | BEARISH |
| Direction % | 58.3% |
| Mag ATR Mean | 2.1085 |
| Mag ATR Std | 1.2354 |
| Mag CV | 0.5859 |
| Timing (candles) | 3.58 |
| Persistence | 3.11 |
| Frequency | 0.0612% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     45 samples  bearish   57.8%  mag_atr=2.0579
    val       12 samples  bearish   58.3%  mag_atr=2.1138
    oos       15 samples  bearish   60.0%  mag_atr=2.2562
```

> When [RSI14_overbought + EMA50_below_EMA100 + bull_engulf] occurs, price historically reacts BEARISH 58.3% of the time with an average move of 2.11 ATR (moderate variance) and stable repetition across validation splits.

---

## #10 — `EMA21_above_EMA50 + bear_engulf + breakout_down`

| Field | Value |
|---|---|
| Consistency Score | **0.4617** |
| Match Count | 119 |
| Dominant Direction | BULLISH |
| Direction % | 58.8% |
| Mag ATR Mean | 2.3143 |
| Mag ATR Std | 1.7684 |
| Mag CV | 0.7641 |
| Timing (candles) | 3.66 |
| Persistence | 3.03 |
| Frequency | 0.1011% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     82 samples  bullish   54.9%  mag_atr=2.3668
    val       20 samples  bullish   55.0%  mag_atr=2.5011
    oos       17 samples  bullish   82.3%  mag_atr=1.8409
```

> When [EMA21_above_EMA50 + bear_engulf + breakout_down] occurs, price historically reacts BULLISH 58.8% of the time with an average move of 2.31 ATR (high variance) and stable repetition across validation splits.

---

## #11 — `close_below_EMA200 + bull_engulf + breakout_up`

| Field | Value |
|---|---|
| Consistency Score | **0.4589** |
| Match Count | 81 |
| Dominant Direction | BEARISH |
| Direction % | 59.3% |
| Mag ATR Mean | 2.0149 |
| Mag ATR Std | 1.325 |
| Mag CV | 0.6576 |
| Timing (candles) | 3.69 |
| Persistence | 3.02 |
| Frequency | 0.0688% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     58 samples  bearish   62.1%  mag_atr=2.0176
    val       10 samples  bearish   50.0%  mag_atr=1.6952
    oos       13 samples  bearish   53.9%  mag_atr=2.2485
```

> When [close_below_EMA200 + bull_engulf + breakout_up] occurs, price historically reacts BEARISH 59.3% of the time with an average move of 2.01 ATR (high variance) and stable repetition across validation splits.

---

## #12 — `RSI14_oversold + MACD_bull_cross + breakout_down`

| Field | Value |
|---|---|
| Consistency Score | **0.4513** |
| Match Count | 62 |
| Dominant Direction | BULLISH |
| Direction % | 56.5% |
| Mag ATR Mean | 1.9144 |
| Mag ATR Std | 0.8686 |
| Mag CV | 0.4537 |
| Timing (candles) | 3.66 |
| Persistence | 3.19 |
| Frequency | 0.0527% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     33 samples  bullish   54.5%  mag_atr=2.151
    val     [insufficient]
    oos       22 samples  bullish   54.5%  mag_atr=1.6195
```

> When [RSI14_oversold + MACD_bull_cross + breakout_down] occurs, price historically reacts BULLISH 56.5% of the time with an average move of 1.91 ATR (moderate variance) and stable repetition across validation splits.

---

## #13 — `RSI14_oversold + close_above_EMA200 + vol_spike_2x`

| Field | Value |
|---|---|
| Consistency Score | **0.4324** |
| Match Count | 86 |
| Dominant Direction | BULLISH |
| Direction % | 61.6% |
| Mag ATR Mean | 2.6804 |
| Mag ATR Std | 1.8216 |
| Mag CV | 0.6796 |
| Timing (candles) | 3.1 |
| Persistence | 3.13 |
| Frequency | 0.073% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     66 samples  bullish   59.1%  mag_atr=2.8454
    val     [insufficient]
    oos       13 samples  bullish   61.5%  mag_atr=1.7691
```

> When [RSI14_oversold + close_above_EMA200 + vol_spike_2x] occurs, price historically reacts BULLISH 61.6% of the time with an average move of 2.68 ATR (high variance) and stable repetition across validation splits.

---

## #14 — `vol_spike_3x + doji + CCI14_oversold`

| Field | Value |
|---|---|
| Consistency Score | **0.4309** |
| Match Count | 77 |
| Dominant Direction | BULLISH |
| Direction % | 58.4% |
| Mag ATR Mean | 2.5839 |
| Mag ATR Std | 1.581 |
| Mag CV | 0.6119 |
| Timing (candles) | 3.36 |
| Persistence | 2.91 |
| Frequency | 0.0654% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     56 samples  bullish   60.7%  mag_atr=2.5674
    val     [insufficient]
    oos       16 samples  bullish   56.2%  mag_atr=2.8757
```

> When [vol_spike_3x + doji + CCI14_oversold] occurs, price historically reacts BULLISH 58.4% of the time with an average move of 2.58 ATR (high variance) and stable repetition across validation splits.

---

## #15 — `EMA50_below_EMA100 + vol_spike_3x + bull_engulf`

| Field | Value |
|---|---|
| Consistency Score | **0.4292** |
| Match Count | 64 |
| Dominant Direction | BULLISH |
| Direction % | 57.8% |
| Mag ATR Mean | 2.5351 |
| Mag ATR Std | 1.4386 |
| Mag CV | 0.5675 |
| Timing (candles) | 3.33 |
| Persistence | 2.81 |
| Frequency | 0.0544% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     48 samples  bullish   56.2%  mag_atr=2.4364
    val     [insufficient]
    oos       11 samples  bullish   63.6%  mag_atr=3.2132
```

> When [EMA50_below_EMA100 + vol_spike_3x + bull_engulf] occurs, price historically reacts BULLISH 57.8% of the time with an average move of 2.54 ATR (moderate variance) and stable repetition across validation splits.

---

## #16 — `RSI14_oversold + vol_spike_2x + squeeze_active`

| Field | Value |
|---|---|
| Consistency Score | **0.4267** |
| Match Count | 69 |
| Dominant Direction | BULLISH |
| Direction % | 55.1% |
| Mag ATR Mean | 2.6821 |
| Mag ATR Std | 1.4896 |
| Mag CV | 0.5554 |
| Timing (candles) | 2.94 |
| Persistence | 2.86 |
| Frequency | 0.0586% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     43 samples  bullish   48.8%  mag_atr=2.8239
    val     [insufficient]
    oos       17 samples  bullish   70.6%  mag_atr=2.1816
```

> When [RSI14_oversold + vol_spike_2x + squeeze_active] occurs, price historically reacts BULLISH 55.1% of the time with an average move of 2.68 ATR (moderate variance) and stable repetition across validation splits.

---

## #17 — `close_above_EMA200 + vol_spike_3x + bear_engulf`

| Field | Value |
|---|---|
| Consistency Score | **0.4178** |
| Match Count | 66 |
| Dominant Direction | BULLISH |
| Direction % | 59.1% |
| Mag ATR Mean | 2.5771 |
| Mag ATR Std | 1.6426 |
| Mag CV | 0.6374 |
| Timing (candles) | 2.89 |
| Persistence | 3.06 |
| Frequency | 0.0561% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     53 samples  bullish   60.4%  mag_atr=2.4115
    val     [insufficient]
    oos       11 samples  bullish   54.5%  mag_atr=3.0086
```

> When [close_above_EMA200 + vol_spike_3x + bear_engulf] occurs, price historically reacts BULLISH 59.1% of the time with an average move of 2.58 ATR (high variance) and stable repetition across validation splits.

---

## #18 — `RSI14_oversold + shooting_star + CCI14_oversold`

| Field | Value |
|---|---|
| Consistency Score | **0.4128** |
| Match Count | 84 |
| Dominant Direction | BULLISH |
| Direction % | 57.1% |
| Mag ATR Mean | 1.8944 |
| Mag ATR Std | 1.3047 |
| Mag CV | 0.6887 |
| Timing (candles) | 3.12 |
| Persistence | 3.04 |
| Frequency | 0.0713% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     64 samples  bullish   56.2%  mag_atr=2.0609
    val     [insufficient]
    oos       12 samples  bullish   50.0%  mag_atr=1.2567
```

> When [RSI14_oversold + shooting_star + CCI14_oversold] occurs, price historically reacts BULLISH 57.1% of the time with an average move of 1.89 ATR (high variance) and stable repetition across validation splits.

---

## #19 — `RSI14_overbought + MACD_bear_cross + vol_spike_1x5`

| Field | Value |
|---|---|
| Consistency Score | **0.4099** |
| Match Count | 60 |
| Dominant Direction | BEARISH |
| Direction % | 55.0% |
| Mag ATR Mean | 2.7581 |
| Mag ATR Std | 1.6343 |
| Mag CV | 0.5925 |
| Timing (candles) | 3.95 |
| Persistence | 2.77 |
| Frequency | 0.051% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     39 samples  bearish   48.7%  mag_atr=2.6436
    val       13 samples  bearish   61.5%  mag_atr=2.4015
    oos     [insufficient]
```

> When [RSI14_overbought + MACD_bear_cross + vol_spike_1x5] occurs, price historically reacts BEARISH 55.0% of the time with an average move of 2.76 ATR (moderate variance) and stable repetition across validation splits.

---
