PROJECT FLOW MAPPING

==================================================
CORE OBJECTIVE
==================================================

The objective of this project is simple:

Start from raw candlestick CSV.

Receive analysis payload.

Generate indicators, chart patterns, and parameter combinations from payload.

Brute-force all possible combinations.

For each combination:

Check whether, when that condition is satisfied, price historically reacts with:

1. consistent direction
2. consistent magnitude

If true:

Validate:

- frequency
- sample sufficiency
- overfitting risk

Return only statistically valid conditions.

The goal is NOT profitability.

The goal is discovering repeatable market reactions after specific market conditions.

==================================================
STEP 1 — LOAD RAW CSV
==================================================

Input:

Raw candlestick CSV only.

Dataset contains:

- timestamp
- open
- high
- low
- close
- volume

Optional:
- symbol
- timeframe

No indicators yet.

No patterns yet.

No analysis yet.

==================================================
STEP 2 — RECEIVE PAYLOAD
==================================================

Receive payload defining analysis scope.

Payload may contain:

INDICATORS

Examples:
- RSI
- EMA
- SMA
- MACD
- ATR
- Bollinger Bands
- volume metrics

PATTERNS

Examples:
- engulfing
- hammer
- doji
- breakout
- inside bar
- double top / bottom

PARAMETER RANGES

Examples:

RSI:
- 14
- thresholds 20 / 25 / 30 / 70 / 80

EMA:
- 9
- 20
- 50
- 100
- 200

Volume:
- 1.5x
- 2x
- 3x

Lookahead:
- 3 candles
- 5 candles
- 10 candles

Rules:
- max combination depth
- minimum sample size
- validation split

Payload fully controls analysis scope.

==================================================
STEP 3 — FEATURE GENERATION
==================================================

From raw candles + payload:

Generate all requested indicators.

Generate all requested chart patterns.

Attach results to each candle.

Each candle becomes enriched with:

OHLCV
+
indicators
+
patterns
+
derived values

Example:

timestamp
open
high
low
close
volume
RSI14
EMA20
EMA50
MACD
ATR
bullish_engulfing
breakout

Dataset is now analysis-ready.

==================================================
STEP 4 — BUILD SEARCH SPACE
==================================================

Generate all possible combinations.

Across:

- indicators
- thresholds
- patterns
- payload parameters

Examples:

RSI14 < 25

EMA20 > EMA50

Volume > 2x average

Bullish engulfing = true

Combinations:

A

A+B

A+B+C

A+B+C+D

Generate complete brute-force search space within payload limits.

==================================================
STEP 5 — CONDITION MATCHING
==================================================

For every combination:

Scan all candles.

Mark every candle:

TRUE if condition satisfied

FALSE otherwise

Collect all TRUE matches.

==================================================
STEP 6 — PRICE REACTION MEASUREMENT
==================================================

For every TRUE match:

Using payload lookahead window:

Measure future reaction.

Evaluate:

DIRECTION

- bullish
- bearish
- neutral

MAGNITUDE

- raw move
- %
- ATR normalized

TIMING

- candles until move starts

PERSISTENCE

- continuation duration

Store all results.

==================================================
STEP 7 — CONSISTENCY TEST
==================================================

For each combination:

Check:

A — DIRECTION CONSISTENCY

Does one direction dominate?

Example:
82% bullish

--------------------------------------------

B — MAGNITUDE CONSISTENCY

Is move size tightly clustered?

Example:
0.84 ATR average
low variance

--------------------------------------------

If BOTH pass:

Candidate = TRUE

Else reject.

==================================================
STEP 8 — FREQUENCY FILTER
==================================================

Check:

- occurrence count
- dataset %
- weekly/monthly frequency

Reject if:

- too rare
- insufficient samples

==================================================
STEP 9 — OVERFIT VALIDATION
==================================================

Split based on payload:

- training
- validation
- out-of-sample

Re-run candidate.

Compare:

- direction stability
- magnitude stability
- frequency stability

If unstable:

Reject.

If stable:

VALID

==================================================
STEP 10 — RANK RESULTS
==================================================

Rank only by:

1. directional consistency
2. magnitude consistency
3. frequency
4. sample count
5. validation stability

Never by profit.

==================================================
STEP 11 — REPORT RESULTS
==================================================

For every valid condition:

Show:

CONDITION

MATCH COUNT

DIRECTIONAL CONSISTENCY

MAGNITUDE DISTRIBUTION

TIMING

PERSISTENCE

FREQUENCY

VALIDATION RESULT

OVERFIT STATUS

FINAL CONSISTENCY SCORE

INTERPRETATION

Example:

“When RSI14 < 25 + EMA20 > EMA50 + bullish engulfing occur together, price historically reacts bullish with an average move of 0.82 ATR, low variance, and stable repetition across validation datasets.”

==================================================
FINAL RULE
==================================================

The system answers only:

“From raw candlestick data and provided payload, which combinations of generated indicators and patterns trigger statistically repeatable and consistent price reactions?”

Ignore profitability.

Ignore trade metrics.

Only detect repeatable market reaction behavior.