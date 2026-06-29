# Market Condition Analysis Report

**Lookahead:** 5 candles  
**Min direction:** 65.0%  
**Max mag CV:** 0.85  

---

## #1 — `ADX_strong_trend + EMA13_above_EMA21 + breakout_down`

| Field | Value |
|---|---|
| Consistency Score | **0.5232** |
| Match Count | 81 |
| Dominant Direction | BULLISH |
| Direction % | 70.4% |
| Mag ATR Mean | 2.1473 |
| Mag ATR Std | 1.1944 |
| Mag CV | 0.5562 |
| Timing (candles) | 3.07 |
| Persistence | 3.56 |
| Frequency | 0.0688% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train     56 samples  bullish   67.9%  mag_atr=2.2194
    val       12 samples  bullish   66.7%  mag_atr=2.1759
    oos       13 samples  bullish   84.6%  mag_atr=1.8103
```

> When [ADX_strong_trend + EMA13_above_EMA21 + breakout_down] occurs, price historically reacts BULLISH 70.4% of the time with an average move of 2.15 ATR (moderate variance) and stable repetition across validation splits.

---
