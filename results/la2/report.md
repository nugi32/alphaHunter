# Market Condition Analysis Report

**Lookahead:** 2 candles  
**Min direction:** 60.0%  
**Max mag CV:** 0.75  

---

## #1 — `SMA21_above_EMA21 + squeeze_active + STO_K14_cross_below_D + Close_below_BB_lower_20_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6410** |
| Match Count | 1348 |
| Dominant Direction | BULLISH |
| Direction % | 62.2% |
| Mag ATR Mean | 1.5022 |
| Mag ATR Std | 0.7656 |
| Mag CV | 0.5097 |
| Timing (candles) | 1.39 |
| Persistence | 1.27 |
| Frequency | 0.674% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    878 samples  bullish   60.6%  mag_atr=1.434
    val      352 samples  bullish   70.5%  mag_atr=1.6544
    oos      118 samples  bullish   50.0%  mag_atr=1.5558
```

> When [SMA21_above_EMA21 + squeeze_active + STO_K14_cross_below_D + Close_below_BB_lower_20_2] occurs, price historically reacts BULLISH 62.2% of the time with an average move of 1.50 ATR (moderate variance) and stable repetition across validation splits.

---

## #2 — `SMA21_above_EMA21 + squeeze_active + Close_below_BB_lower_20_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6400** |
| Match Count | 1493 |
| Dominant Direction | BULLISH |
| Direction % | 61.5% |
| Mag ATR Mean | 1.5072 |
| Mag ATR Std | 0.7922 |
| Mag CV | 0.5256 |
| Timing (candles) | 1.39 |
| Persistence | 1.26 |
| Frequency | 0.7465% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    980 samples  bullish   60.4%  mag_atr=1.4523
    val      385 samples  bullish   68.6%  mag_atr=1.6317
    oos      128 samples  bullish   49.2%  mag_atr=1.5535
```

> When [SMA21_above_EMA21 + squeeze_active + Close_below_BB_lower_20_2] occurs, price historically reacts BULLISH 61.5% of the time with an average move of 1.51 ATR (moderate variance) and stable repetition across validation splits.

---

## #3 — `squeeze_active + MACD_9_21_bear_cross + Close_below_BB_lower_20_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6400** |
| Match Count | 1342 |
| Dominant Direction | BULLISH |
| Direction % | 62.0% |
| Mag ATR Mean | 1.4994 |
| Mag ATR Std | 0.7635 |
| Mag CV | 0.5092 |
| Timing (candles) | 1.4 |
| Persistence | 1.26 |
| Frequency | 0.671% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    880 samples  bullish   61.0%  mag_atr=1.4558
    val      338 samples  bullish   68.9%  mag_atr=1.6033
    oos      124 samples  bullish   50.0%  mag_atr=1.5251
```

> When [squeeze_active + MACD_9_21_bear_cross + Close_below_BB_lower_20_2] occurs, price historically reacts BULLISH 62.0% of the time with an average move of 1.50 ATR (moderate variance) and stable repetition across validation splits.

---

## #4 — `close_below_EMA21 + SMA21_above_EMA21 + squeeze_active + Close_below_BB_lower_20_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6400** |
| Match Count | 1493 |
| Dominant Direction | BULLISH |
| Direction % | 61.5% |
| Mag ATR Mean | 1.5072 |
| Mag ATR Std | 0.7922 |
| Mag CV | 0.5256 |
| Timing (candles) | 1.39 |
| Persistence | 1.26 |
| Frequency | 0.7465% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    980 samples  bullish   60.4%  mag_atr=1.4523
    val      385 samples  bullish   68.6%  mag_atr=1.6317
    oos      128 samples  bullish   49.2%  mag_atr=1.5535
```

> When [close_below_EMA21 + SMA21_above_EMA21 + squeeze_active + Close_below_BB_lower_20_2] occurs, price historically reacts BULLISH 61.5% of the time with an average move of 1.51 ATR (moderate variance) and stable repetition across validation splits.

---

## #5 — `close_below_EMA21 + squeeze_active + MACD_9_21_bear_cross + Close_below_BB_lower_20_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6400** |
| Match Count | 1342 |
| Dominant Direction | BULLISH |
| Direction % | 62.0% |
| Mag ATR Mean | 1.4994 |
| Mag ATR Std | 0.7635 |
| Mag CV | 0.5092 |
| Timing (candles) | 1.4 |
| Persistence | 1.26 |
| Frequency | 0.671% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    880 samples  bullish   61.0%  mag_atr=1.4558
    val      338 samples  bullish   68.9%  mag_atr=1.6033
    oos      124 samples  bullish   50.0%  mag_atr=1.5251
```

> When [close_below_EMA21 + squeeze_active + MACD_9_21_bear_cross + Close_below_BB_lower_20_2] occurs, price historically reacts BULLISH 62.0% of the time with an average move of 1.50 ATR (moderate variance) and stable repetition across validation splits.

---

## #6 — `SMA21_above_EMA21 + ATR34_high_vol + squeeze_active + Close_below_BB_lower_20_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6400** |
| Match Count | 1493 |
| Dominant Direction | BULLISH |
| Direction % | 61.5% |
| Mag ATR Mean | 1.5072 |
| Mag ATR Std | 0.7922 |
| Mag CV | 0.5256 |
| Timing (candles) | 1.39 |
| Persistence | 1.26 |
| Frequency | 0.7465% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    980 samples  bullish   60.4%  mag_atr=1.4523
    val      385 samples  bullish   68.6%  mag_atr=1.6317
    oos      128 samples  bullish   49.2%  mag_atr=1.5535
```

> When [SMA21_above_EMA21 + ATR34_high_vol + squeeze_active + Close_below_BB_lower_20_2] occurs, price historically reacts BULLISH 61.5% of the time with an average move of 1.51 ATR (moderate variance) and stable repetition across validation splits.

---

## #7 — `ATR34_high_vol + squeeze_active + MACD_9_21_bear_cross + Close_below_BB_lower_20_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6400** |
| Match Count | 1342 |
| Dominant Direction | BULLISH |
| Direction % | 62.0% |
| Mag ATR Mean | 1.4994 |
| Mag ATR Std | 0.7635 |
| Mag CV | 0.5092 |
| Timing (candles) | 1.4 |
| Persistence | 1.26 |
| Frequency | 0.671% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    880 samples  bullish   61.0%  mag_atr=1.4558
    val      338 samples  bullish   68.9%  mag_atr=1.6033
    oos      124 samples  bullish   50.0%  mag_atr=1.5251
```

> When [ATR34_high_vol + squeeze_active + MACD_9_21_bear_cross + Close_below_BB_lower_20_2] occurs, price historically reacts BULLISH 62.0% of the time with an average move of 1.50 ATR (moderate variance) and stable repetition across validation splits.

---

## #8 — `close_below_EMA34 + SMA21_above_EMA21 + squeeze_active + Close_below_BB_lower_20_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6396** |
| Match Count | 1489 |
| Dominant Direction | BULLISH |
| Direction % | 61.5% |
| Mag ATR Mean | 1.5071 |
| Mag ATR Std | 0.7931 |
| Mag CV | 0.5262 |
| Timing (candles) | 1.39 |
| Persistence | 1.26 |
| Frequency | 0.7445% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    979 samples  bullish   60.4%  mag_atr=1.4518
    val      385 samples  bullish   68.6%  mag_atr=1.6317
    oos      125 samples  bullish   48.8%  mag_atr=1.5571
```

> When [close_below_EMA34 + SMA21_above_EMA21 + squeeze_active + Close_below_BB_lower_20_2] occurs, price historically reacts BULLISH 61.5% of the time with an average move of 1.51 ATR (moderate variance) and stable repetition across validation splits.

---

## #9 — `close_below_EMA34 + squeeze_active + MACD_9_21_bear_cross + Close_below_BB_lower_20_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6396** |
| Match Count | 1338 |
| Dominant Direction | BULLISH |
| Direction % | 62.0% |
| Mag ATR Mean | 1.4992 |
| Mag ATR Std | 0.7645 |
| Mag CV | 0.5099 |
| Timing (candles) | 1.4 |
| Persistence | 1.26 |
| Frequency | 0.669% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    879 samples  bullish   61.0%  mag_atr=1.4552
    val      338 samples  bullish   68.9%  mag_atr=1.6033
    oos      121 samples  bullish   49.6%  mag_atr=1.5282
```

> When [close_below_EMA34 + squeeze_active + MACD_9_21_bear_cross + Close_below_BB_lower_20_2] occurs, price historically reacts BULLISH 62.0% of the time with an average move of 1.50 ATR (moderate variance) and stable repetition across validation splits.

---

## #10 — `SMA21_above_EMA21 + squeeze_active + STO_K14_cross_below_D + Close_below_BB_lower_21_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6395** |
| Match Count | 1352 |
| Dominant Direction | BULLISH |
| Direction % | 62.3% |
| Mag ATR Mean | 1.4921 |
| Mag ATR Std | 0.7711 |
| Mag CV | 0.5168 |
| Timing (candles) | 1.38 |
| Persistence | 1.27 |
| Frequency | 0.676% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    892 samples  bullish   60.9%  mag_atr=1.4297
    val      354 samples  bullish   69.5%  mag_atr=1.6294
    oos      106 samples  bullish   50.0%  mag_atr=1.5586
```

> When [SMA21_above_EMA21 + squeeze_active + STO_K14_cross_below_D + Close_below_BB_lower_21_2] occurs, price historically reacts BULLISH 62.3% of the time with an average move of 1.49 ATR (moderate variance) and stable repetition across validation splits.

---

## #11 — `EMA8_below_EMA13 + SMA21_above_EMA21 + squeeze_active + Close_below_BB_lower_20_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6389** |
| Match Count | 1485 |
| Dominant Direction | BULLISH |
| Direction % | 61.4% |
| Mag ATR Mean | 1.5072 |
| Mag ATR Std | 0.7938 |
| Mag CV | 0.5267 |
| Timing (candles) | 1.39 |
| Persistence | 1.26 |
| Frequency | 0.7425% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    975 samples  bullish   60.2%  mag_atr=1.4518
    val      384 samples  bullish   68.5%  mag_atr=1.6305
    oos      126 samples  bullish   49.2%  mag_atr=1.5597
```

> When [EMA8_below_EMA13 + SMA21_above_EMA21 + squeeze_active + Close_below_BB_lower_20_2] occurs, price historically reacts BULLISH 61.4% of the time with an average move of 1.51 ATR (moderate variance) and stable repetition across validation splits.

---

## #12 — `EMA8_below_EMA13 + squeeze_active + MACD_9_21_bear_cross + Close_below_BB_lower_20_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6389** |
| Match Count | 1334 |
| Dominant Direction | BULLISH |
| Direction % | 61.8% |
| Mag ATR Mean | 1.4992 |
| Mag ATR Std | 0.7652 |
| Mag CV | 0.5104 |
| Timing (candles) | 1.4 |
| Persistence | 1.26 |
| Frequency | 0.667% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    875 samples  bullish   60.8%  mag_atr=1.4553
    val      337 samples  bullish   68.8%  mag_atr=1.6019
    oos      122 samples  bullish   50.0%  mag_atr=1.5311
```

> When [EMA8_below_EMA13 + squeeze_active + MACD_9_21_bear_cross + Close_below_BB_lower_20_2] occurs, price historically reacts BULLISH 61.8% of the time with an average move of 1.50 ATR (moderate variance) and stable repetition across validation splits.

---

## #13 — `squeeze_active + STO_K14_cross_below_D + MACD_9_21_bear_cross + Close_below_BB_lower_20_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6388** |
| Match Count | 1236 |
| Dominant Direction | BULLISH |
| Direction % | 62.5% |
| Mag ATR Mean | 1.5051 |
| Mag ATR Std | 0.7598 |
| Mag CV | 0.5048 |
| Timing (candles) | 1.4 |
| Persistence | 1.28 |
| Frequency | 0.618% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    803 samples  bullish   61.1%  mag_atr=1.451
    val      317 samples  bullish   70.3%  mag_atr=1.6277
    oos      116 samples  bullish   50.0%  mag_atr=1.5441
```

> When [squeeze_active + STO_K14_cross_below_D + MACD_9_21_bear_cross + Close_below_BB_lower_20_2] occurs, price historically reacts BULLISH 62.5% of the time with an average move of 1.51 ATR (moderate variance) and stable repetition across validation splits.

---

## #14 — `SMA21_above_EMA21 + squeeze_active + Close_below_BB_lower_21_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6385** |
| Match Count | 1498 |
| Dominant Direction | BULLISH |
| Direction % | 61.5% |
| Mag ATR Mean | 1.4959 |
| Mag ATR Std | 0.7966 |
| Mag CV | 0.5325 |
| Timing (candles) | 1.38 |
| Persistence | 1.26 |
| Frequency | 0.749% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    996 samples  bullish   60.5%  mag_atr=1.4475
    val      386 samples  bullish   67.9%  mag_atr=1.6091
    oos      116 samples  bullish   49.1%  mag_atr=1.5354
```

> When [SMA21_above_EMA21 + squeeze_active + Close_below_BB_lower_21_2] occurs, price historically reacts BULLISH 61.5% of the time with an average move of 1.50 ATR (moderate variance) and stable repetition across validation splits.

---

## #15 — `close_below_EMA21 + SMA21_above_EMA21 + squeeze_active + Close_below_BB_lower_21_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6385** |
| Match Count | 1498 |
| Dominant Direction | BULLISH |
| Direction % | 61.5% |
| Mag ATR Mean | 1.4959 |
| Mag ATR Std | 0.7966 |
| Mag CV | 0.5325 |
| Timing (candles) | 1.38 |
| Persistence | 1.26 |
| Frequency | 0.749% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    996 samples  bullish   60.5%  mag_atr=1.4475
    val      386 samples  bullish   67.9%  mag_atr=1.6091
    oos      116 samples  bullish   49.1%  mag_atr=1.5354
```

> When [close_below_EMA21 + SMA21_above_EMA21 + squeeze_active + Close_below_BB_lower_21_2] occurs, price historically reacts BULLISH 61.5% of the time with an average move of 1.50 ATR (moderate variance) and stable repetition across validation splits.

---

## #16 — `SMA21_above_EMA21 + ATR34_high_vol + squeeze_active + Close_below_BB_lower_21_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6385** |
| Match Count | 1498 |
| Dominant Direction | BULLISH |
| Direction % | 61.5% |
| Mag ATR Mean | 1.4959 |
| Mag ATR Std | 0.7966 |
| Mag CV | 0.5325 |
| Timing (candles) | 1.38 |
| Persistence | 1.26 |
| Frequency | 0.749% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    996 samples  bullish   60.5%  mag_atr=1.4475
    val      386 samples  bullish   67.9%  mag_atr=1.6091
    oos      116 samples  bullish   49.1%  mag_atr=1.5354
```

> When [SMA21_above_EMA21 + ATR34_high_vol + squeeze_active + Close_below_BB_lower_21_2] occurs, price historically reacts BULLISH 61.5% of the time with an average move of 1.50 ATR (moderate variance) and stable repetition across validation splits.

---

## #17 — `close_below_EMA34 + SMA21_above_EMA21 + squeeze_active + Close_below_BB_lower_21_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6384** |
| Match Count | 1496 |
| Dominant Direction | BULLISH |
| Direction % | 61.6% |
| Mag ATR Mean | 1.496 |
| Mag ATR Std | 0.7971 |
| Mag CV | 0.5328 |
| Timing (candles) | 1.38 |
| Persistence | 1.26 |
| Frequency | 0.748% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    996 samples  bullish   60.5%  mag_atr=1.4475
    val      386 samples  bullish   67.9%  mag_atr=1.6091
    oos      114 samples  bullish   49.1%  mag_atr=1.5374
```

> When [close_below_EMA34 + SMA21_above_EMA21 + squeeze_active + Close_below_BB_lower_21_2] occurs, price historically reacts BULLISH 61.6% of the time with an average move of 1.50 ATR (moderate variance) and stable repetition across validation splits.

---

## #18 — `squeeze_active + MACD_9_21_bear_cross + Close_below_BB_lower_21_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6381** |
| Match Count | 1332 |
| Dominant Direction | BULLISH |
| Direction % | 62.2% |
| Mag ATR Mean | 1.4886 |
| Mag ATR Std | 0.7724 |
| Mag CV | 0.5189 |
| Timing (candles) | 1.39 |
| Persistence | 1.27 |
| Frequency | 0.666% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    884 samples  bullish   61.2%  mag_atr=1.4473
    val      337 samples  bullish   68.8%  mag_atr=1.5866
    oos      111 samples  bullish   50.5%  mag_atr=1.5206
```

> When [squeeze_active + MACD_9_21_bear_cross + Close_below_BB_lower_21_2] occurs, price historically reacts BULLISH 62.2% of the time with an average move of 1.49 ATR (moderate variance) and stable repetition across validation splits.

---

## #19 — `close_below_EMA21 + squeeze_active + MACD_9_21_bear_cross + Close_below_BB_lower_21_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6381** |
| Match Count | 1332 |
| Dominant Direction | BULLISH |
| Direction % | 62.2% |
| Mag ATR Mean | 1.4886 |
| Mag ATR Std | 0.7724 |
| Mag CV | 0.5189 |
| Timing (candles) | 1.39 |
| Persistence | 1.27 |
| Frequency | 0.666% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    884 samples  bullish   61.2%  mag_atr=1.4473
    val      337 samples  bullish   68.8%  mag_atr=1.5866
    oos      111 samples  bullish   50.5%  mag_atr=1.5206
```

> When [close_below_EMA21 + squeeze_active + MACD_9_21_bear_cross + Close_below_BB_lower_21_2] occurs, price historically reacts BULLISH 62.2% of the time with an average move of 1.49 ATR (moderate variance) and stable repetition across validation splits.

---

## #20 — `ATR34_high_vol + squeeze_active + MACD_9_21_bear_cross + Close_below_BB_lower_21_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6381** |
| Match Count | 1332 |
| Dominant Direction | BULLISH |
| Direction % | 62.2% |
| Mag ATR Mean | 1.4886 |
| Mag ATR Std | 0.7724 |
| Mag CV | 0.5189 |
| Timing (candles) | 1.39 |
| Persistence | 1.27 |
| Frequency | 0.666% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    884 samples  bullish   61.2%  mag_atr=1.4473
    val      337 samples  bullish   68.8%  mag_atr=1.5866
    oos      111 samples  bullish   50.5%  mag_atr=1.5206
```

> When [ATR34_high_vol + squeeze_active + MACD_9_21_bear_cross + Close_below_BB_lower_21_2] occurs, price historically reacts BULLISH 62.2% of the time with an average move of 1.49 ATR (moderate variance) and stable repetition across validation splits.

---

## #21 — `close_below_EMA34 + squeeze_active + MACD_9_21_bear_cross + Close_below_BB_lower_21_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6380** |
| Match Count | 1330 |
| Dominant Direction | BULLISH |
| Direction % | 62.3% |
| Mag ATR Mean | 1.4887 |
| Mag ATR Std | 0.773 |
| Mag CV | 0.5192 |
| Timing (candles) | 1.39 |
| Persistence | 1.27 |
| Frequency | 0.665% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    884 samples  bullish   61.2%  mag_atr=1.4473
    val      337 samples  bullish   68.8%  mag_atr=1.5866
    oos      109 samples  bullish   50.5%  mag_atr=1.5225
```

> When [close_below_EMA34 + squeeze_active + MACD_9_21_bear_cross + Close_below_BB_lower_21_2] occurs, price historically reacts BULLISH 62.3% of the time with an average move of 1.49 ATR (moderate variance) and stable repetition across validation splits.

---

## #22 — `EMA8_below_EMA13 + SMA21_above_EMA21 + squeeze_active + Close_below_BB_lower_21_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6379** |
| Match Count | 1495 |
| Dominant Direction | BULLISH |
| Direction % | 61.5% |
| Mag ATR Mean | 1.4957 |
| Mag ATR Std | 0.7973 |
| Mag CV | 0.5331 |
| Timing (candles) | 1.38 |
| Persistence | 1.26 |
| Frequency | 0.7475% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    993 samples  bullish   60.4%  mag_atr=1.447
    val      386 samples  bullish   67.9%  mag_atr=1.6091
    oos      116 samples  bullish   49.1%  mag_atr=1.5354
```

> When [EMA8_below_EMA13 + SMA21_above_EMA21 + squeeze_active + Close_below_BB_lower_21_2] occurs, price historically reacts BULLISH 61.5% of the time with an average move of 1.50 ATR (moderate variance) and stable repetition across validation splits.

---

## #23 — `squeeze_active + CCI14_oversold + MACD_9_21_bear_cross + Close_below_BB_lower_20_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6379** |
| Match Count | 1299 |
| Dominant Direction | BULLISH |
| Direction % | 62.0% |
| Mag ATR Mean | 1.4993 |
| Mag ATR Std | 0.7675 |
| Mag CV | 0.5119 |
| Timing (candles) | 1.4 |
| Persistence | 1.26 |
| Frequency | 0.6495% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    847 samples  bullish   60.7%  mag_atr=1.4525
    val      333 samples  bullish   69.4%  mag_atr=1.6099
    oos      119 samples  bullish   51.3%  mag_atr=1.5232
```

> When [squeeze_active + CCI14_oversold + MACD_9_21_bear_cross + Close_below_BB_lower_20_2] occurs, price historically reacts BULLISH 62.0% of the time with an average move of 1.50 ATR (moderate variance) and stable repetition across validation splits.

---

## #24 — `squeeze_active + STO_K14_cross_below_D + MACD_9_21_bear_cross + Close_below_BB_lower_21_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6377** |
| Match Count | 1223 |
| Dominant Direction | BULLISH |
| Direction % | 63.0% |
| Mag ATR Mean | 1.4974 |
| Mag ATR Std | 0.77 |
| Mag CV | 0.5142 |
| Timing (candles) | 1.39 |
| Persistence | 1.29 |
| Frequency | 0.6115% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    805 samples  bullish   61.6%  mag_atr=1.4436
    val      316 samples  bullish   70.2%  mag_atr=1.6119
    oos      102 samples  bullish   51.0%  mag_atr=1.5668
```

> When [squeeze_active + STO_K14_cross_below_D + MACD_9_21_bear_cross + Close_below_BB_lower_21_2] occurs, price historically reacts BULLISH 63.0% of the time with an average move of 1.50 ATR (moderate variance) and stable repetition across validation splits.

---

## #25 — `EMA8_below_EMA13 + squeeze_active + MACD_9_21_bear_cross + Close_below_BB_lower_21_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6375** |
| Match Count | 1329 |
| Dominant Direction | BULLISH |
| Direction % | 62.1% |
| Mag ATR Mean | 1.4884 |
| Mag ATR Std | 0.7731 |
| Mag CV | 0.5194 |
| Timing (candles) | 1.39 |
| Persistence | 1.27 |
| Frequency | 0.6645% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    881 samples  bullish   61.1%  mag_atr=1.4468
    val      337 samples  bullish   68.8%  mag_atr=1.5866
    oos      111 samples  bullish   50.5%  mag_atr=1.5206
```

> When [EMA8_below_EMA13 + squeeze_active + MACD_9_21_bear_cross + Close_below_BB_lower_21_2] occurs, price historically reacts BULLISH 62.1% of the time with an average move of 1.49 ATR (moderate variance) and stable repetition across validation splits.

---

## #26 — `SMA21_above_EMA21 + squeeze_active + CCI14_oversold + Close_below_BB_lower_20_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6373** |
| Match Count | 1438 |
| Dominant Direction | BULLISH |
| Direction % | 61.5% |
| Mag ATR Mean | 1.5065 |
| Mag ATR Std | 0.7938 |
| Mag CV | 0.5269 |
| Timing (candles) | 1.39 |
| Persistence | 1.25 |
| Frequency | 0.719% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    938 samples  bullish   60.1%  mag_atr=1.4518
    val      376 samples  bullish   68.6%  mag_atr=1.6262
    oos      124 samples  bullish   50.0%  mag_atr=1.5571
```

> When [SMA21_above_EMA21 + squeeze_active + CCI14_oversold + Close_below_BB_lower_20_2] occurs, price historically reacts BULLISH 61.5% of the time with an average move of 1.51 ATR (moderate variance) and stable repetition across validation splits.

---

## #27 — `squeeze_active + CCI14_oversold + MACD_9_21_bear_cross + Close_below_BB_lower_21_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6371** |
| Match Count | 1290 |
| Dominant Direction | BULLISH |
| Direction % | 62.5% |
| Mag ATR Mean | 1.4892 |
| Mag ATR Std | 0.7744 |
| Mag CV | 0.52 |
| Timing (candles) | 1.39 |
| Persistence | 1.27 |
| Frequency | 0.645% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    847 samples  bullish   61.3%  mag_atr=1.4446
    val      333 samples  bullish   69.4%  mag_atr=1.5917
    oos      110 samples  bullish   50.9%  mag_atr=1.5223
```

> When [squeeze_active + CCI14_oversold + MACD_9_21_bear_cross + Close_below_BB_lower_21_2] occurs, price historically reacts BULLISH 62.5% of the time with an average move of 1.49 ATR (moderate variance) and stable repetition across validation splits.

---

## #28 — `SMA21_above_EMA21 + squeeze_active + CCI14_oversold + Close_below_BB_lower_21_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6365** |
| Match Count | 1443 |
| Dominant Direction | BULLISH |
| Direction % | 61.6% |
| Mag ATR Mean | 1.4945 |
| Mag ATR Std | 0.7966 |
| Mag CV | 0.533 |
| Timing (candles) | 1.38 |
| Persistence | 1.26 |
| Frequency | 0.7215% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    949 samples  bullish   60.6%  mag_atr=1.446
    val      378 samples  bullish   68.0%  mag_atr=1.604
    oos      116 samples  bullish   49.1%  mag_atr=1.5354
```

> When [SMA21_above_EMA21 + squeeze_active + CCI14_oversold + Close_below_BB_lower_21_2] occurs, price historically reacts BULLISH 61.6% of the time with an average move of 1.49 ATR (moderate variance) and stable repetition across validation splits.

---

## #29 — `squeeze_active + MACD_9_21_bear_cross + Close_below_BB_lower_20_2 + Close_below_BB_lower_21_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6360** |
| Match Count | 1232 |
| Dominant Direction | BULLISH |
| Direction % | 62.3% |
| Mag ATR Mean | 1.502 |
| Mag ATR Std | 0.7714 |
| Mag CV | 0.5136 |
| Timing (candles) | 1.4 |
| Persistence | 1.27 |
| Frequency | 0.616% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    812 samples  bullish   61.2%  mag_atr=1.4546
    val      314 samples  bullish   69.1%  mag_atr=1.6132
    oos      106 samples  bullish   50.9%  mag_atr=1.5363
```

> When [squeeze_active + MACD_9_21_bear_cross + Close_below_BB_lower_20_2 + Close_below_BB_lower_21_2] occurs, price historically reacts BULLISH 62.3% of the time with an average move of 1.50 ATR (moderate variance) and stable repetition across validation splits.

---

## #30 — `SMA21_above_EMA21 + squeeze_active + MACD_9_21_bear_cross + Close_below_BB_lower_20_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6358** |
| Match Count | 1236 |
| Dominant Direction | BULLISH |
| Direction % | 62.5% |
| Mag ATR Mean | 1.4876 |
| Mag ATR Std | 0.7685 |
| Mag CV | 0.5166 |
| Timing (candles) | 1.4 |
| Persistence | 1.27 |
| Frequency | 0.618% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    815 samples  bullish   61.1%  mag_atr=1.4415
    val      313 samples  bullish   69.3%  mag_atr=1.6044
    oos      108 samples  bullish   52.8%  mag_atr=1.4971
```

> When [SMA21_above_EMA21 + squeeze_active + MACD_9_21_bear_cross + Close_below_BB_lower_20_2] occurs, price historically reacts BULLISH 62.5% of the time with an average move of 1.49 ATR (moderate variance) and stable repetition across validation splits.

---

## #31 — `SMA21_above_EMA21 + squeeze_active + Close_below_BB_lower_20_2 + Close_below_BB_lower_21_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6358** |
| Match Count | 1381 |
| Dominant Direction | BULLISH |
| Direction % | 61.8% |
| Mag ATR Mean | 1.509 |
| Mag ATR Std | 0.7994 |
| Mag CV | 0.5298 |
| Timing (candles) | 1.39 |
| Persistence | 1.26 |
| Frequency | 0.6905% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    913 samples  bullish   60.7%  mag_atr=1.454
    val      358 samples  bullish   68.7%  mag_atr=1.6376
    oos      110 samples  bullish   49.1%  mag_atr=1.5463
```

> When [SMA21_above_EMA21 + squeeze_active + Close_below_BB_lower_20_2 + Close_below_BB_lower_21_2] occurs, price historically reacts BULLISH 61.8% of the time with an average move of 1.51 ATR (moderate variance) and stable repetition across validation splits.

---

## #32 — `EMA13_below_EMA21 + squeeze_active + MACD_9_21_bear_cross + Close_below_BB_lower_20_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6341** |
| Match Count | 1115 |
| Dominant Direction | BULLISH |
| Direction % | 61.4% |
| Mag ATR Mean | 1.5013 |
| Mag ATR Std | 0.7372 |
| Mag CV | 0.491 |
| Timing (candles) | 1.39 |
| Persistence | 1.26 |
| Frequency | 0.5575% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    729 samples  bullish   60.5%  mag_atr=1.4502
    val      292 samples  bullish   67.8%  mag_atr=1.6262
    oos       94 samples  bullish   48.9%  mag_atr=1.5098
```

> When [EMA13_below_EMA21 + squeeze_active + MACD_9_21_bear_cross + Close_below_BB_lower_20_2] occurs, price historically reacts BULLISH 61.4% of the time with an average move of 1.50 ATR (moderate variance) and stable repetition across validation splits.

---

## #33 — `SMA21_above_EMA21 + squeeze_active + MACD_9_21_bear_cross + Close_below_BB_lower_21_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6333** |
| Match Count | 1230 |
| Dominant Direction | BULLISH |
| Direction % | 62.6% |
| Mag ATR Mean | 1.478 |
| Mag ATR Std | 0.7799 |
| Mag CV | 0.5277 |
| Timing (candles) | 1.39 |
| Persistence | 1.27 |
| Frequency | 0.615% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    823 samples  bullish   61.2%  mag_atr=1.4352
    val      312 samples  bullish   68.9%  mag_atr=1.5852
    oos       95 samples  bullish   53.7%  mag_atr=1.496
```

> When [SMA21_above_EMA21 + squeeze_active + MACD_9_21_bear_cross + Close_below_BB_lower_21_2] occurs, price historically reacts BULLISH 62.6% of the time with an average move of 1.48 ATR (moderate variance) and stable repetition across validation splits.

---

## #34 — `EMA13_below_EMA21 + SMA21_above_EMA21 + squeeze_active + Close_below_BB_lower_20_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6330** |
| Match Count | 1273 |
| Dominant Direction | BULLISH |
| Direction % | 61.1% |
| Mag ATR Mean | 1.5148 |
| Mag ATR Std | 0.7795 |
| Mag CV | 0.5146 |
| Timing (candles) | 1.38 |
| Persistence | 1.25 |
| Frequency | 0.6365% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    833 samples  bullish   60.0%  mag_atr=1.4533
    val      341 samples  bullish   67.5%  mag_atr=1.6492
    oos       99 samples  bullish   48.5%  mag_atr=1.5695
```

> When [EMA13_below_EMA21 + SMA21_above_EMA21 + squeeze_active + Close_below_BB_lower_20_2] occurs, price historically reacts BULLISH 61.1% of the time with an average move of 1.51 ATR (moderate variance) and stable repetition across validation splits.

---

## #35 — `squeeze_active + CCI21_oversold + MACD_9_21_bear_cross + Close_below_BB_lower_21_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6313** |
| Match Count | 1207 |
| Dominant Direction | BULLISH |
| Direction % | 61.8% |
| Mag ATR Mean | 1.503 |
| Mag ATR Std | 0.7833 |
| Mag CV | 0.5212 |
| Timing (candles) | 1.4 |
| Persistence | 1.26 |
| Frequency | 0.6035% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    793 samples  bullish   60.7%  mag_atr=1.4599
    val      315 samples  bullish   68.6%  mag_atr=1.5967
    oos       99 samples  bullish   49.5%  mag_atr=1.5502
```

> When [squeeze_active + CCI21_oversold + MACD_9_21_bear_cross + Close_below_BB_lower_21_2] occurs, price historically reacts BULLISH 61.8% of the time with an average move of 1.50 ATR (moderate variance) and stable repetition across validation splits.

---

## #36 — `SMA21_above_EMA21 + squeeze_active + CCI21_oversold + Close_below_BB_lower_20_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6312** |
| Match Count | 1338 |
| Dominant Direction | BULLISH |
| Direction % | 61.0% |
| Mag ATR Mean | 1.5252 |
| Mag ATR Std | 0.808 |
| Mag CV | 0.5298 |
| Timing (candles) | 1.39 |
| Persistence | 1.25 |
| Frequency | 0.669% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    871 samples  bullish   59.7%  mag_atr=1.4711
    val      354 samples  bullish   68.1%  mag_atr=1.6379
    oos      113 samples  bullish   48.7%  mag_atr=1.5891
```

> When [SMA21_above_EMA21 + squeeze_active + CCI21_oversold + Close_below_BB_lower_20_2] occurs, price historically reacts BULLISH 61.0% of the time with an average move of 1.53 ATR (moderate variance) and stable repetition across validation splits.

---

## #37 — `squeeze_active + CCI21_oversold + MACD_9_21_bear_cross + Close_below_BB_lower_20_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6308** |
| Match Count | 1185 |
| Dominant Direction | BULLISH |
| Direction % | 61.4% |
| Mag ATR Mean | 1.513 |
| Mag ATR Std | 0.7768 |
| Mag CV | 0.5134 |
| Timing (candles) | 1.41 |
| Persistence | 1.26 |
| Frequency | 0.5925% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    771 samples  bullish   60.2%  mag_atr=1.4699
    val      308 samples  bullish   68.2%  mag_atr=1.6097
    oos      106 samples  bullish   50.0%  mag_atr=1.5458
```

> When [squeeze_active + CCI21_oversold + MACD_9_21_bear_cross + Close_below_BB_lower_20_2] occurs, price historically reacts BULLISH 61.4% of the time with an average move of 1.51 ATR (moderate variance) and stable repetition across validation splits.

---

## #38 — `squeeze_active + CCI34_oversold + STO_K14_cross_below_D + Close_below_BB_lower_21_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6303** |
| Match Count | 1134 |
| Dominant Direction | BULLISH |
| Direction % | 62.3% |
| Mag ATR Mean | 1.5142 |
| Mag ATR Std | 0.7881 |
| Mag CV | 0.5205 |
| Timing (candles) | 1.37 |
| Persistence | 1.28 |
| Frequency | 0.567% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    727 samples  bullish   60.2%  mag_atr=1.4729
    val      323 samples  bullish   70.3%  mag_atr=1.607
    oos       84 samples  bullish   48.8%  mag_atr=1.5148
```

> When [squeeze_active + CCI34_oversold + STO_K14_cross_below_D + Close_below_BB_lower_21_2] occurs, price historically reacts BULLISH 62.3% of the time with an average move of 1.51 ATR (moderate variance) and stable repetition across validation splits.

---

## #39 — `EMA13_below_EMA21 + squeeze_active + CCI34_oversold + Close_below_BB_lower_20_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6302** |
| Match Count | 1195 |
| Dominant Direction | BULLISH |
| Direction % | 61.3% |
| Mag ATR Mean | 1.5177 |
| Mag ATR Std | 0.7852 |
| Mag CV | 0.5174 |
| Timing (candles) | 1.38 |
| Persistence | 1.27 |
| Frequency | 0.5975% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    769 samples  bullish   59.2%  mag_atr=1.4764
    val      337 samples  bullish   69.7%  mag_atr=1.6224
    oos       89 samples  bullish   48.3%  mag_atr=1.4777
```

> When [EMA13_below_EMA21 + squeeze_active + CCI34_oversold + Close_below_BB_lower_20_2] occurs, price historically reacts BULLISH 61.3% of the time with an average move of 1.52 ATR (moderate variance) and stable repetition across validation splits.

---

## #40 — `squeeze_active + CCI34_oversold + STO_K14_cross_below_D + Close_below_BB_lower_20_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6301** |
| Match Count | 1099 |
| Dominant Direction | BULLISH |
| Direction % | 62.1% |
| Mag ATR Mean | 1.524 |
| Mag ATR Std | 0.7819 |
| Mag CV | 0.5131 |
| Timing (candles) | 1.38 |
| Persistence | 1.28 |
| Frequency | 0.5495% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    700 samples  bullish   59.9%  mag_atr=1.4801
    val      314 samples  bullish   70.7%  mag_atr=1.626
    oos       85 samples  bullish   48.2%  mag_atr=1.5088
```

> When [squeeze_active + CCI34_oversold + STO_K14_cross_below_D + Close_below_BB_lower_20_2] occurs, price historically reacts BULLISH 62.1% of the time with an average move of 1.52 ATR (moderate variance) and stable repetition across validation splits.

---

## #41 — `EMA13_below_EMA21 + WMA21_above_EMA21 + squeeze_active + Close_below_BB_lower_21_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6300** |
| Match Count | 519 |
| Dominant Direction | BULLISH |
| Direction % | 65.5% |
| Mag ATR Mean | 1.5364 |
| Mag ATR Std | 0.7299 |
| Mag CV | 0.4751 |
| Timing (candles) | 1.4 |
| Persistence | 1.32 |
| Frequency | 0.2595% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    343 samples  bullish   63.0%  mag_atr=1.4617
    val      139 samples  bullish   74.1%  mag_atr=1.7071
    oos       37 samples  bullish   56.8%  mag_atr=1.5884
```

> When [EMA13_below_EMA21 + WMA21_above_EMA21 + squeeze_active + Close_below_BB_lower_21_2] occurs, price historically reacts BULLISH 65.5% of the time with an average move of 1.54 ATR (moderate variance) and stable repetition across validation splits.

---

## #42 — `WMA21_above_EMA21 + squeeze_active + STO_K14_cross_below_D + Close_below_BB_lower_21_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6296** |
| Match Count | 665 |
| Dominant Direction | BULLISH |
| Direction % | 66.6% |
| Mag ATR Mean | 1.5283 |
| Mag ATR Std | 0.7857 |
| Mag CV | 0.5141 |
| Timing (candles) | 1.41 |
| Persistence | 1.33 |
| Frequency | 0.3325% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    448 samples  bullish   63.8%  mag_atr=1.4673
    val      164 samples  bullish   75.6%  mag_atr=1.6706
    oos       53 samples  bullish   62.3%  mag_atr=1.6045
```

> When [WMA21_above_EMA21 + squeeze_active + STO_K14_cross_below_D + Close_below_BB_lower_21_2] occurs, price historically reacts BULLISH 66.6% of the time with an average move of 1.53 ATR (moderate variance) and stable repetition across validation splits.

---

## #43 — `WMA21_above_EMA21 + squeeze_active + STO_K14_cross_below_D + Close_below_BB_lower_20_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6295** |
| Match Count | 707 |
| Dominant Direction | BULLISH |
| Direction % | 66.2% |
| Mag ATR Mean | 1.5422 |
| Mag ATR Std | 0.7942 |
| Mag CV | 0.515 |
| Timing (candles) | 1.41 |
| Persistence | 1.32 |
| Frequency | 0.3535% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    465 samples  bullish   63.4%  mag_atr=1.482
    val      176 samples  bullish   75.6%  mag_atr=1.6667
    oos       66 samples  bullish   60.6%  mag_atr=1.6347
```

> When [WMA21_above_EMA21 + squeeze_active + STO_K14_cross_below_D + Close_below_BB_lower_20_2] occurs, price historically reacts BULLISH 66.2% of the time with an average move of 1.54 ATR (moderate variance) and stable repetition across validation splits.

---

## #44 — `EMA13_below_EMA21 + WMA21_above_EMA21 + squeeze_active + Close_below_BB_lower_20_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6294** |
| Match Count | 526 |
| Dominant Direction | BULLISH |
| Direction % | 65.6% |
| Mag ATR Mean | 1.5593 |
| Mag ATR Std | 0.7478 |
| Mag CV | 0.4796 |
| Timing (candles) | 1.41 |
| Persistence | 1.31 |
| Frequency | 0.263% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    342 samples  bullish   63.2%  mag_atr=1.4816
    val      141 samples  bullish   73.0%  mag_atr=1.7017
    oos       43 samples  bullish   60.5%  mag_atr=1.7108
```

> When [EMA13_below_EMA21 + WMA21_above_EMA21 + squeeze_active + Close_below_BB_lower_20_2] occurs, price historically reacts BULLISH 65.6% of the time with an average move of 1.56 ATR (moderate variance) and stable repetition across validation splits.

---

## #45 — `WMA21_above_EMA21 + squeeze_active + MACD_9_21_bear_cross + Close_below_BB_lower_20_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6288** |
| Match Count | 729 |
| Dominant Direction | BULLISH |
| Direction % | 65.2% |
| Mag ATR Mean | 1.52 |
| Mag ATR Std | 0.7694 |
| Mag CV | 0.5062 |
| Timing (candles) | 1.41 |
| Persistence | 1.3 |
| Frequency | 0.3645% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    482 samples  bullish   62.9%  mag_atr=1.4698
    val      183 samples  bullish   73.8%  mag_atr=1.6353
    oos       64 samples  bullish   57.8%  mag_atr=1.5687
```

> When [WMA21_above_EMA21 + squeeze_active + MACD_9_21_bear_cross + Close_below_BB_lower_20_2] occurs, price historically reacts BULLISH 65.2% of the time with an average move of 1.52 ATR (moderate variance) and stable repetition across validation splits.

---

## #46 — `WMA21_above_EMA21 + squeeze_active + MACD_9_21_bear_cross + Close_below_BB_lower_21_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6284** |
| Match Count | 692 |
| Dominant Direction | BULLISH |
| Direction % | 65.6% |
| Mag ATR Mean | 1.5081 |
| Mag ATR Std | 0.767 |
| Mag CV | 0.5086 |
| Timing (candles) | 1.41 |
| Persistence | 1.31 |
| Frequency | 0.346% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    466 samples  bullish   62.9%  mag_atr=1.455
    val      172 samples  bullish   74.4%  mag_atr=1.6376
    oos       54 samples  bullish   61.1%  mag_atr=1.5535
```

> When [WMA21_above_EMA21 + squeeze_active + MACD_9_21_bear_cross + Close_below_BB_lower_21_2] occurs, price historically reacts BULLISH 65.6% of the time with an average move of 1.51 ATR (moderate variance) and stable repetition across validation splits.

---

## #47 — `WMA21_above_EMA21 + squeeze_active + Close_below_BB_lower_20_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6281** |
| Match Count | 754 |
| Dominant Direction | BULLISH |
| Direction % | 65.2% |
| Mag ATR Mean | 1.5377 |
| Mag ATR Std | 0.7909 |
| Mag CV | 0.5143 |
| Timing (candles) | 1.41 |
| Persistence | 1.3 |
| Frequency | 0.377% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    494 samples  bullish   63.2%  mag_atr=1.4811
    val      187 samples  bullish   73.8%  mag_atr=1.6418
    oos       73 samples  bullish   57.5%  mag_atr=1.6543
```

> When [WMA21_above_EMA21 + squeeze_active + Close_below_BB_lower_20_2] occurs, price historically reacts BULLISH 65.2% of the time with an average move of 1.54 ATR (moderate variance) and stable repetition across validation splits.

---

## #48 — `close_below_EMA21 + WMA21_above_EMA21 + squeeze_active + Close_below_BB_lower_20_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6281** |
| Match Count | 754 |
| Dominant Direction | BULLISH |
| Direction % | 65.2% |
| Mag ATR Mean | 1.5377 |
| Mag ATR Std | 0.7909 |
| Mag CV | 0.5143 |
| Timing (candles) | 1.41 |
| Persistence | 1.3 |
| Frequency | 0.377% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    494 samples  bullish   63.2%  mag_atr=1.4811
    val      187 samples  bullish   73.8%  mag_atr=1.6418
    oos       73 samples  bullish   57.5%  mag_atr=1.6543
```

> When [close_below_EMA21 + WMA21_above_EMA21 + squeeze_active + Close_below_BB_lower_20_2] occurs, price historically reacts BULLISH 65.2% of the time with an average move of 1.54 ATR (moderate variance) and stable repetition across validation splits.

---

## #49 — `WMA21_above_EMA21 + ATR34_high_vol + squeeze_active + Close_below_BB_lower_20_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6281** |
| Match Count | 754 |
| Dominant Direction | BULLISH |
| Direction % | 65.2% |
| Mag ATR Mean | 1.5377 |
| Mag ATR Std | 0.7909 |
| Mag CV | 0.5143 |
| Timing (candles) | 1.41 |
| Persistence | 1.3 |
| Frequency | 0.377% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    494 samples  bullish   63.2%  mag_atr=1.4811
    val      187 samples  bullish   73.8%  mag_atr=1.6418
    oos       73 samples  bullish   57.5%  mag_atr=1.6543
```

> When [WMA21_above_EMA21 + ATR34_high_vol + squeeze_active + Close_below_BB_lower_20_2] occurs, price historically reacts BULLISH 65.2% of the time with an average move of 1.54 ATR (moderate variance) and stable repetition across validation splits.

---

## #50 — `close_below_EMA34 + WMA21_above_EMA21 + squeeze_active + Close_below_BB_lower_20_2`

| Field | Value |
|---|---|
| Consistency Score | **0.6274** |
| Match Count | 750 |
| Dominant Direction | BULLISH |
| Direction % | 65.2% |
| Mag ATR Mean | 1.5376 |
| Mag ATR Std | 0.7928 |
| Mag CV | 0.5156 |
| Timing (candles) | 1.41 |
| Persistence | 1.3 |
| Frequency | 0.375% |
| Overfit Status | STABLE |

**Split Validation:**
```
    train    493 samples  bullish   63.1%  mag_atr=1.48
    val      187 samples  bullish   73.8%  mag_atr=1.6418
    oos       70 samples  bullish   57.1%  mag_atr=1.6651
```

> When [close_below_EMA34 + WMA21_above_EMA21 + squeeze_active + Close_below_BB_lower_20_2] occurs, price historically reacts BULLISH 65.2% of the time with an average move of 1.54 ATR (moderate variance) and stable repetition across validation splits.

---
