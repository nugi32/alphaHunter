# Payload Parameters — Complete Reference

Every parameter in `payload.json` is adjustable.
This document explains what each one does, how it affects the pipeline,
and shows the exact calculation behind it.

---

## Table of Contents

1. [max_depth](#max_depth)
2. [min_samples](#min_samples)
3. [lookahead](#lookahead)
4. [validation_split](#validation_split)
5. [min_direction_pct](#min_direction_pct)
6. [max_mag_cv](#max_mag_cv)
7. [min_freq_pct](#min_freq_pct)
8. [max_freq_pct](#max_freq_pct)
9. [dir_grace](#dir_grace)
10. [Parameter Interaction Map](#parameter-interaction-map)
11. [Recommended Starting Points by Timeframe](#recommended-starting-points-by-timeframe)

---

## max_depth

**Used in:** Step 4 — Build Search Space

**What it does:**
Controls how many conditions are allowed to be combined together
in a single candidate. Depth 1 means single conditions only.
Depth 3 means combinations of up to 3 conditions simultaneously.

**Formula — total combinations at each depth:**

```
Given N atomic conditions:

Depth 1 : C(N,1) = N
Depth 2 : C(N,2) = N! / (2! × (N-2)!)
Depth 3 : C(N,3) = N! / (3! × (N-3)!)
Depth 4 : C(N,4) = N! / (4! × (N-4)!)

Total   = sum of all depths
```

**Example with N=28 conditions:**

```
Depth 1 : C(28,1) =    28
Depth 2 : C(28,2) =   378
Depth 3 : C(28,3) = 3,276
Depth 4 : C(28,4) = 20,475
─────────────────────────
Total at depth 4  : 24,157 combinations
Total at depth 3  :  3,682 combinations
```

**Effect on runtime:**
Depth 4 adds ~20k more combinations to scan.
On 117k candles this is significant. Rule of thumb:

```
depth 2 → fast      (seconds)
depth 3 → moderate  (seconds to minutes)
depth 4 → slow      (minutes)
depth 5 → very slow (tens of minutes)
```

**Effect on results:**
Higher depth finds more specific conditions (3 or 4 things must align at once).
More specific = fewer matches = harder to reach min_samples.
More specific = higher risk of overfitting.

**Recommended values:**

```
First run    : max_depth = 3   (balanced)
Exploration  : max_depth = 4   (more granular, watch sample counts)
Quick test   : max_depth = 2   (fast, broad patterns only)
```

---

## min_samples

**Used in:** Step 5 — Condition Matching (post-filter)

**What it does:**
Minimum number of times a condition combo must have fired
across the entire dataset to be considered for analysis.
Combos below this count are discarded immediately after scanning.

**Formula:**

```
match_count = number of candles where ALL conditions in combo = TRUE
if match_count < min_samples → discard
```

**Example:**

```
Dataset       : 117,000 candles
Condition     : RSI14_oversold + vol_spike_3x + squeeze_active
Matches found : 136 candles

min_samples = 50  → 136 ≥ 50  → KEEP
min_samples = 200 → 136 < 200 → DISCARD
```

**Why it matters:**
With too few samples, a 70% direction rate could easily be
random chance. With 10 samples, 7 bullish out of 10 is noise.
With 100 samples, 70 bullish out of 100 is statistically meaningful.

**Statistical reasoning:**
At 55% direction (just above noise), the minimum samples
needed for ~95% confidence that it is real and not random:

```
Approximate minimum n for detecting 55% vs 50% at 95% confidence:

  n ≈ (Z / (p - 0.5))²  × p × (1-p)
  n ≈ (1.96 / 0.05)²    × 0.55 × 0.45
  n ≈ 1537              (strict)

Practical shortcut:
  At 60% direction → min ~100 samples gives reasonable confidence
  At 65% direction → min ~50  samples is acceptable
  At 70% direction → min ~30  samples is acceptable
```

**Recommended values:**

```
Strict   : min_samples = 100
Balanced : min_samples = 50
Loose    : min_samples = 30  (accept more noise)
```

Higher min_samples will reduce the number of candidates
that survive Step 5, but all survivors are more statistically
grounded.

---

## lookahead

**Used in:** Step 6 — Price Reaction Measurement

**What it does:**
Defines how many candles forward the system looks after a
condition fires. The direction and magnitude are measured
over this window.

**How direction is calculated:**

```
Entry candle position  : i
Lookahead window       : candles i+1 through i+N

entry_close  = Close[i]
final_close  = Close[i + lookahead]

net_move     = final_close - entry_close
net_atr      = net_move / ATR[i]

if net_atr >  +0.2  → BULLISH
if net_atr <  -0.2  → BEARISH
else                 → NEUTRAL
```

**Example — lookahead = 5 on H1 data:**

```
Candle i    Close = 1.08500   ATR = 0.00200

Future candles:
  i+1  Close = 1.08520
  i+2  Close = 1.08480
  i+3  Close = 1.08610
  i+4  Close = 1.08590
  i+5  Close = 1.08720   ← this is what we measure

net_move = 1.08720 - 1.08500 = +0.00220
net_atr  = 0.00220 / 0.00200 = +1.10

+1.10 > +0.2 → direction = BULLISH
magnitude   = 1.10 ATR
```

**What changes at each lookahead value:**

```
lookahead = 1
  Measures: next candle close vs entry close
  Catches : immediate 1-bar reactions
  Risk    : very noisy, single candle can be random

lookahead = 3
  Measures: 3 candles forward
  Catches : fast momentum responses
  Risk    : moderate noise

lookahead = 5
  Measures: 5 candles forward  (default)
  Catches : short-term directional moves
  Risk    : balanced

lookahead = 10
  Measures: 10 candles forward
  Catches : sustained trends after the condition
  Risk    : many unrelated events can corrupt the signal

lookahead = 20
  Measures: 20 candles forward
  Catches : medium-term trend continuation
  Risk    : high noise, direction % tends to collapse toward 50%
```

**On H1 candles, lookahead = N means:**

```
lookahead =  1 →  1 hour forward
lookahead =  5 →  5 hours forward
lookahead = 10 → 10 hours forward
lookahead = 24 →  1 day forward
```

**A condition is most trustworthy if it appears across
multiple lookahead values.** Run the sweep and compare:

```python
lookaheads = [1, 3, 5, 10]
```

If a condition survives at la=3 AND la=5 AND la=10, the
reaction persists across time — not just a spike.

---

## validation_split

**Used in:** Step 9 — Overfit Validation

**What it does:**
Controls how the dataset is split into train, validation,
and out-of-sample (OOS) segments for overfitting detection.
The split is always positional — chronological order is preserved.

**Formula:**

```
total_candles = N

train_end = int(N × (1 - 2 × validation_split))
val_end   = int(N × (1 - validation_split))

Train      : candles[0           : train_end]
Validation : candles[train_end   : val_end  ]
OOS        : candles[val_end     : N        ]
```

**Example — 117,000 candles, validation_split = 0.20:**

```
train_end  = int(117000 × (1 - 0.40)) = int(117000 × 0.60) = 70,200
val_end    = int(117000 × (1 - 0.20)) = int(117000 × 0.80) = 93,600

Train      : candles 0       → 70,199    (70,200 candles = 60%)
Validation : candles 70,200  → 93,599    (23,400 candles = 20%)
OOS        : candles 93,600  → 116,999   (23,400 candles = 20%)
```

**Example — same dataset, validation_split = 0.15:**

```
train_end  = int(117000 × 0.70) = 81,900
val_end    = int(117000 × 0.85) = 99,450

Train      : 81,900 candles  (70%)
Validation : 17,550 candles  (15%)
OOS        : 17,550 candles  (15%)
```

**What happens during validation:**
For each candidate condition, the system re-runs reaction
measurement separately on each split and checks:

```
1. Does dominant direction stay the same in all splits?
   Train=bullish, Val=bullish, OOS=bullish → PASS
   Train=bullish, Val=bullish, OOS=bearish → FAIL (direction flipped)

2. Does direction % stay above the grace floor?
   min_direction_pct=55%, dir_grace=0.80
   grace_floor = 55% × 0.80 = 44%

   Train=63%, Val=58%, OOS=61% → all ≥ 44% → PASS
   Train=63%, Val=58%, OOS=41% → OOS < 44% → FAIL (degraded)
```

**Tradeoff:**

```
validation_split = 0.10
  Train : 80%  Val : 10%  OOS : 10%
  More training data → conditions easier to satisfy in train
  Less validation data → less reliable OOS check
  Risk  : weaker overfitting protection

validation_split = 0.20  (default)
  Train : 60%  Val : 20%  OOS : 20%
  Balanced

validation_split = 0.30
  Train : 40%  Val : 30%  OOS : 30%
  Stronger overfitting protection
  Risk  : less training data → min_samples harder to reach in train
```

**Recommended values:**

```
Large dataset (>50k candles)  : 0.20 — 0.25
Medium dataset (10k–50k)      : 0.15 — 0.20
Small dataset  (<10k candles) : 0.10 — 0.15
```

---

## min_direction_pct

**Used in:** Step 7 — Consistency Test (direction check)

**What it does:**
Minimum percentage of reactions that must go in the dominant
direction for a condition to be considered directionally consistent.

**Formula:**

```
bull_pct    = (bullish reactions / total reactions) × 100
bear_pct    = (bearish reactions / total reactions) × 100
dominant    = max(bull_pct, bear_pct)

if dominant < min_direction_pct → REJECT
```

**Example:**

```
Condition fires 200 times.
Results:
  Bullish  : 118 times
  Bearish  :  62 times
  Neutral  :  20 times

bull_pct = 118/200 × 100 = 59.0%
bear_pct =  62/200 × 100 = 31.0%
dominant = 59.0%

min_direction_pct = 55.0  → 59.0 ≥ 55.0 → PASS
min_direction_pct = 62.0  → 59.0 < 62.0  → REJECT
```

**What different thresholds mean:**

```
55% — slightly above coin flip (50%). Low bar. More results,
      but some may be marginal. Good for exploration.

60% — moderate confidence. Price goes the expected way
      60 out of 100 times.

65% — high confidence. Strong directional tendency.
      Fewer results but more reliable.

70%+ — very strict. On noisy timeframes (M1, M5, H1) this
       may produce zero results because market noise is high.
```

**What 50% means:** pure random. The condition has zero
directional edge. Any value close to 50% should be ignored.

**Recommended starting values by timeframe:**

```
M1, M5   : 58–62%   (very noisy, strict threshold needed)
M15, H1  : 55–60%   (moderate noise)
H4, D1   : 53–58%   (cleaner, lower threshold acceptable)
W1       : 52–55%   (weekly candles are cleaner still)
```

---

## max_mag_cv

**Used in:** Step 7 — Consistency Test (magnitude check)

**What it does:**
Maximum allowed Coefficient of Variation (CV) for the ATR-
normalised magnitude of reactions. CV measures how scattered
the move sizes are relative to their average.

**Formula:**

```
CV = standard_deviation / mean

mag_atr values for each reaction:
  [1.2, 0.9, 1.4, 1.1, 2.8, 1.0, 1.3, 0.8, 1.2, 1.1]

mean = 1.28
std  = 0.54

CV = 0.54 / 1.28 = 0.422

max_mag_cv = 0.85  → 0.422 ≤ 0.85 → PASS  (tight cluster)
max_mag_cv = 0.40  → 0.422 > 0.40 → REJECT (too scattered)
```

**What CV values mean:**

```
CV = 0.0   — all moves are exactly the same size (impossible in practice)
CV = 0.2   — very tight cluster, nearly uniform move size
CV = 0.4   — tight, moves are within roughly 40% of each other
CV = 0.6   — moderate scatter
CV = 0.8   — high scatter, move size varies widely
CV = 1.0   — std equals mean, very high variance
CV > 1.0   — extreme variance, single outlier events dominate
```

**Visual example:**

```
Low CV (0.35) — consistent magnitude:
  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
      (moves cluster tightly around average)

High CV (0.90) — inconsistent magnitude:
  ▓▓        ▓▓▓▓▓▓▓   ▓               ▓▓▓▓▓▓▓▓▓▓▓▓▓▓
      (moves scattered widely, some tiny, some huge)
```

**Why magnitude consistency matters:**
A condition that always moves bullish is interesting.
A condition that always moves bullish by roughly the same amount
is more meaningful — it suggests a repeatable mechanical reaction,
not just a directional bias with random magnitude.

**Recommended values:**

```
Strict   : max_mag_cv = 0.50  (tight clustering required)
Balanced : max_mag_cv = 0.70  (default for most timeframes)
Loose    : max_mag_cv = 0.90  (accepts high variance)
```

---

## min_freq_pct

**Used in:** Step 8 — Frequency Filter (lower bound)

**What it does:**
Minimum percentage of total candles on which a condition must
fire. Conditions that are too rare are rejected — not enough
real-world occurrence to be practically useful.

**Formula:**

```
freq_pct = (match_count / total_candles) × 100

if freq_pct < min_freq_pct → REJECT (too rare)
```

**Example:**

```
Total candles : 117,000
Condition matches : 47

freq_pct = (47 / 117,000) × 100 = 0.040%

min_freq_pct = 0.05  → 0.040 < 0.05 → REJECT (too rare)
min_freq_pct = 0.03  → 0.040 ≥ 0.03 → PASS
```

**Converting freq_pct to approximate real-world frequency
on H1 data (117k candles ≈ 13.4 years):**

```
freq_pct = 0.05%  →  ~58   occurrences total  →  ~4  per year
freq_pct = 0.10%  →  ~117  occurrences total  →  ~9  per year
freq_pct = 0.50%  →  ~585  occurrences total  →  ~44 per year
freq_pct = 1.00%  →  ~1170 occurrences total  →  ~87 per year
```

**Recommended values:**

```
Strict (rare patterns OK)   : min_freq_pct = 0.02
Balanced                    : min_freq_pct = 0.05
Practical (need regularity) : min_freq_pct = 0.10
```

---

## max_freq_pct

**Used in:** Step 8 — Frequency Filter (upper bound)

**What it does:**
Maximum percentage of total candles on which a condition may
fire. Conditions that fire too often are not selective — they
are describing ambient market state, not a specific setup.

**Formula:**

```
freq_pct = (match_count / total_candles) × 100

if freq_pct > max_freq_pct → REJECT (too common)
```

**Example:**

```
Total candles : 117,000
Condition     : EMA21_above_EMA50  (fires ~55% of the time)
Matches       : 64,350

freq_pct = (64,350 / 117,000) × 100 = 55.0%

max_freq_pct = 5.0  → 55.0 > 5.0 → REJECT (not selective)
```

**Why this matters:**
If a condition fires 55% of the time, measuring direction
after it fires is nearly identical to measuring random candles.
There is no signal — the condition is always on.

**The selectivity principle:**

```
freq = 50%  → fires every other candle. Useless.
freq = 20%  → fires 1 in 5 candles. Still too common.
freq = 5%   → fires 1 in 20 candles. Borderline.
freq = 1%   → fires 1 in 100 candles. Selective.
freq = 0.1% → fires 1 in 1000 candles. Very selective.
```

**Recommended values:**

```
Default : max_freq_pct = 5.0
Strict  : max_freq_pct = 2.0   (only selective conditions)
Loose   : max_freq_pct = 10.0  (allow moderately common conditions)
```

Note: `max_freq_pct` and `min_samples` must be compatible.
On 117k candles, `max_freq_pct = 1.0%` means max 1,170 matches.
`min_samples = 50` means min 50 matches.
Both constraints apply simultaneously.

---

## dir_grace

**Used in:** Step 9 — Overfit Validation

**What it does:**
A tolerance multiplier applied to `min_direction_pct` during
split validation. Allows natural variance between time periods
without rejecting every condition that dips slightly below the
training threshold in one split.

**Formula:**

```
grace_floor = min_direction_pct × dir_grace

A split passes if:
  1. dominant direction is the same as overall dominant direction
  2. split direction % ≥ grace_floor
```

**Example:**

```
min_direction_pct = 55.0
dir_grace         = 0.80

grace_floor = 55.0 × 0.80 = 44.0%

Condition results by split:
  Train      : bullish 61.2%  → 61.2 ≥ 44.0 → PASS
  Validation : bullish 57.8%  → 57.8 ≥ 44.0 → PASS
  OOS        : bullish 52.1%  → 52.1 ≥ 44.0 → PASS
  → OVERALL: STABLE

If OOS dropped to 41.0%:
  41.0 < 44.0 → FAIL → UNSTABLE → REJECTED
```

**What dir_grace controls:**

```
dir_grace = 1.00
  No grace at all. Every split must meet the full threshold.
  Very strict. Will reject most conditions on volatile instruments.

dir_grace = 0.80  (default)
  Splits can drop 20% below the threshold.
  Balanced: allows for regime variance without ignoring collapse.

dir_grace = 0.70
  Splits can drop 30% below the threshold.
  Lenient. Accepts conditions that degrade significantly in OOS.

dir_grace = 0.60
  Very lenient. Only catches complete direction flips.
```

**Combined example showing how dir_grace + min_direction_pct
interact:**

```
Scenario A:  min_direction_pct=55,  dir_grace=0.80
  grace_floor = 44.0%
  OOS at 46% → PASS

Scenario B:  min_direction_pct=60,  dir_grace=0.80
  grace_floor = 48.0%
  OOS at 46% → FAIL

Scenario C:  min_direction_pct=55,  dir_grace=0.90
  grace_floor = 49.5%
  OOS at 46% → FAIL

Scenario D:  min_direction_pct=55,  dir_grace=0.70
  grace_floor = 38.5%
  OOS at 46% → PASS
```

Setting both `min_direction_pct` and `dir_grace` high at the
same time will produce very few survivors. Setting both low
will produce many survivors but with weak overfitting protection.

---

## Parameter Interaction Map

```
┌─────────────────┐     affects     ┌──────────────────────┐
│   max_depth     │────────────────►│  search space size   │
└─────────────────┘                 │  (Step 4)            │
                                    └──────────────────────┘

┌─────────────────┐     affects     ┌──────────────────────┐
│   min_samples   │────────────────►│  candidates after    │
└─────────────────┘                 │  Step 5              │
                                    └──────────────────────┘

┌─────────────────┐     affects     ┌──────────────────────┐
│   lookahead     │────────────────►│  direction %         │
└─────────────────┘                 │  mag ATR values      │
                                    │  (Step 6)            │
                                    └──────────────────────┘

┌─────────────────┐     affects     ┌──────────────────────┐
│min_direction_pct│────────────────►│  direction filter    │
│max_mag_cv       │                 │  (Step 7)            │
└─────────────────┘                 └──────────────────────┘

┌─────────────────┐     affects     ┌──────────────────────┐
│  min_freq_pct   │────────────────►│  frequency filter    │
│  max_freq_pct   │                 │  (Step 8)            │
└─────────────────┘                 └──────────────────────┘

┌─────────────────┐     affects     ┌──────────────────────┐
│validation_split │────────────────►│  split sizes         │
│dir_grace        │                 │  overfitting check   │
└─────────────────┘                 │  (Step 9)            │
                                    └──────────────────────┘
```

---

## Recommended Starting Points by Timeframe

```
┌──────────┬───────────┬─────────────┬──────────┬─────────────────┬────────────┬──────────────┬──────────────┬───────────┐
│Timeframe │ max_depth │ min_samples │ lookahead│ min_direction   │ max_mag_cv │ min_freq_pct │ max_freq_pct │ dir_grace │
├──────────┼───────────┼─────────────┼──────────┼─────────────────┼────────────┼──────────────┼──────────────┼───────────┤
│ M1       │     3     │     200     │   5–10   │      60.0       │    0.70    │     0.01     │     2.0      │   0.80    │
│ M5       │     3     │     150     │   5–10   │      58.0       │    0.75    │     0.02     │     3.0      │   0.80    │
│ M15      │     3     │     100     │    5     │      57.0       │    0.80    │     0.03     │     4.0      │   0.80    │
│ H1       │     3     │      50     │   3–5    │      55.0       │    0.85    │     0.05     │     5.0      │   0.80    │
│ H4       │     3     │      50     │   3–5    │      54.0       │    0.85    │     0.10     │     8.0      │   0.75    │
│ D1       │     3     │      30     │    3     │      53.0       │    0.90    │     0.20     │    10.0      │   0.75    │
│ W1       │     2     │      20     │    2     │      52.0       │    0.95    │     0.50     │    15.0      │   0.70    │
└──────────┴───────────┴─────────────┴──────────┴─────────────────┴────────────┴──────────────┴──────────────┴───────────┘
```

Lower timeframes need stricter direction thresholds and smaller
lookaheads because noise is higher and patterns resolve faster.
Higher timeframes can use looser thresholds because each candle
carries more structural information.