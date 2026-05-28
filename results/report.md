# Market Condition Analysis Report

**Lookahead:** 1 candles  
**Min direction:** 55.0%  
**Max mag CV:** 0.85  

---

## #1 — `ADX_strong_trend + EMA50_above_EMA100 + MACD_bear_cross + vol_spike_3x`

| Field | Value |
|---|---|
| Consistency Score | **0.4965** |
| Match Count | 136 |
| Dominant Direction | BULLISH |
| Direction % | 55.1% |
| Mag ATR Mean | 1.3723 |
| Mag ATR Std | 0.6799 |
| Mag CV | 0.4954 |
| Timing (candles) | 1.0 |
| Persistence | 0.61 |
| Frequency | 0.1155% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    106 samples  bullish   52.8%  mag_atr=1.3895
    val     [insufficient]
    oos       19 samples  bullish   57.9%  mag_atr=1.309
```

> When [ADX_strong_trend + EMA50_above_EMA100 + MACD_bear_cross + vol_spike_3x] occurs, price historically reacts BULLISH 55.1% of the time with an average move of 1.37 ATR (moderate variance) and stable repetition across validation splits.

---

## #2 — `ADX_trending + close_above_EMA200 + vol_spike_3x + CCI14_oversold`

| Field | Value |
|---|---|
| Consistency Score | **0.4894** |
| Match Count | 141 |
| Dominant Direction | BULLISH |
| Direction % | 56.0% |
| Mag ATR Mean | 1.4335 |
| Mag ATR Std | 0.7919 |
| Mag CV | 0.5524 |
| Timing (candles) | 1.0 |
| Persistence | 0.64 |
| Frequency | 0.1198% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    115 samples  bullish   53.9%  mag_atr=1.4392
    val     [insufficient]
    oos       19 samples  bullish   68.4%  mag_atr=1.4663
```

> When [ADX_trending + close_above_EMA200 + vol_spike_3x + CCI14_oversold] occurs, price historically reacts BULLISH 56.0% of the time with an average move of 1.43 ATR (moderate variance) and stable repetition across validation splits.

---

## #3 — `ADX_strong_trend + EMA21_above_EMA50 + MACD_bear_cross + vol_spike_3x`

| Field | Value |
|---|---|
| Consistency Score | **0.4883** |
| Match Count | 126 |
| Dominant Direction | BULLISH |
| Direction % | 57.1% |
| Mag ATR Mean | 1.4121 |
| Mag ATR Std | 0.7391 |
| Mag CV | 0.5234 |
| Timing (candles) | 1.0 |
| Persistence | 0.63 |
| Frequency | 0.107% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     95 samples  bullish   54.7%  mag_atr=1.4109
    val     [insufficient]
    oos       20 samples  bullish   60.0%  mag_atr=1.4701
```

> When [ADX_strong_trend + EMA21_above_EMA50 + MACD_bear_cross + vol_spike_3x] occurs, price historically reacts BULLISH 57.1% of the time with an average move of 1.41 ATR (moderate variance) and stable repetition across validation splits.

---

## #4 — `ADX_strong_trend + close_above_EMA200 + MACD_bear_cross + vol_spike_3x`

| Field | Value |
|---|---|
| Consistency Score | **0.4806** |
| Match Count | 119 |
| Dominant Direction | BULLISH |
| Direction % | 56.3% |
| Mag ATR Mean | 1.3988 |
| Mag ATR Std | 0.7273 |
| Mag CV | 0.5199 |
| Timing (candles) | 1.0 |
| Persistence | 0.63 |
| Frequency | 0.1011% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     94 samples  bullish   54.3%  mag_atr=1.4281
    val     [insufficient]
    oos       16 samples  bullish   62.5%  mag_atr=1.2627
```

> When [ADX_strong_trend + close_above_EMA200 + MACD_bear_cross + vol_spike_3x] occurs, price historically reacts BULLISH 56.3% of the time with an average move of 1.40 ATR (moderate variance) and stable repetition across validation splits.

---
