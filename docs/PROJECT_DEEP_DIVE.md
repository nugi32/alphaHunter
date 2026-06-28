# AlphaHunter Deep Dive

This document is a technical walkthrough of the AlphaHunter project as implemented in the current repository. It is written for a new developer who needs to understand not just what the code does, but how the pieces fit together from raw market data to a final ranked report.

---

## 1. Project Overview

### What problem this project solves

AlphaHunter is a research engine for discovering market conditions that have historically produced repeatable forward reactions.

Instead of starting with a pre-written strategy and testing it, the project takes historical OHLCV data and asks a broader question:

> Which combinations of technical indicators, candlestick patterns, and market-state conditions have historically produced strong and repeatable reactions in future price action?

The project therefore performs a brute-force search over many candidate conditions and evaluates the resulting pattern behavior statistically.

### Why brute-force analysis is used

The core idea is that many market patterns are not obvious from a single manual analysis. A brute-force engine is useful because it:

- explores many condition combinations automatically,
- finds relationships that humans might miss,
- produces a ranked list of historically repeatable setups,
- avoids confirmation bias from hand-picked ideas.

The search is not intended to prove profitability by itself. It is intended to surface conditions that deserve further study.

### High-level architecture

```text
Raw OHLCV CSV
    │
    ▼
Loader / Timeframe Reader
    │
    ▼
Feature Engineering
  - indicators
  - patterns
  - derived values
    │
    ▼
Payload-driven Condition Definitions
    │
    ▼
Combination Generator
    │
    ▼
Brute-force Matcher
    │
    ▼
Reaction Measurement
  - direction
  - magnitude
  - timing
  - persistence
    │
    ▼
Filter / Validation
  - consistency
  - frequency
  - overfit checks
    │
    ▼
Ranking + Report Generation
```

### Important design principle

The system is built around a simple pipeline:

1. Load candles.
2. Enrich each candle with features.
3. Build a search space of condition combinations.
4. Scan the history for every condition combination.
5. Measure what happened after each occurrence.
6. Filter and validate the survivors.
7. Rank them and export a report.

---

## 2. Folder Structure

### Root-level files

- [main.py](../main.py): CLI entry point for preparing data and running the full pipeline.
- [loader.py](../loader.py): Loads historical market data for each timeframe.
- [prepare_utils.py](../prepare_utils.py): Orchestrates all feature generation steps.
- [payload.json](../payload.json): Main configuration file defining the available conditions and analysis limits.
- [README.md](../README.md): Project overview and high-level documentation.

### Analysis package

- [analysis/search_space.py](../analysis/search_space.py): Builds the candidate combination list.
- [analysis/condition_engine.py](../analysis/condition_engine.py): Evaluates condition combinations over the dataframe.
- [analysis/reaction_engine.py](../analysis/reaction_engine.py): Measures forward reactions after each match.
- [analysis/consistency.py](../analysis/consistency.py): Filters by direction, magnitude stability, and frequency.
- [analysis/validator.py](../analysis/validator.py): Performs train/validation/OOS stability checks.
- [analysis/ranker.py](../analysis/ranker.py): Scores and sorts surviving candidates.
- [analysis/reporter.py](../analysis/reporter.py): Writes the markdown and CSV reports.

### Indicators package

The [indicators](../indicators) package contains feature generators. Each module appends columns to the dataframe.

Examples:

- [indicators/trend_ma.py](../indicators/trend_ma.py): SMA/EMA/WMA columns.
- [indicators/rsi.py](../indicators/rsi.py): RSI values for multiple periods.
- [indicators/atr.py](../indicators/atr.py): ATR values for multiple periods.
- [indicators/macd.py](../indicators/macd.py): MACD, signal line, histogram.
- [indicators/bollinger.py](../indicators/bollinger.py): Bollinger Bands.
- [indicators/adx.py](../indicators/adx.py): ADX and directional movement lines.
- [indicators/cci.py](../indicators/cci.py): Commodity Channel Index.
- [indicators/advanced.py](../indicators/advanced.py): Additional price-structure indicators.

### Patterns package

The [patterns](../patterns) package adds pattern-based features and regime signals.

Examples:

- [patterns/candle_patterns.py](../patterns/candle_patterns.py): Hammer, doji, engulfing, harami, etc.
- [patterns/market_structure.py](../patterns/market_structure.py): Higher high / lower low / breakout flags.
- [patterns/compression.py](../patterns/compression.py): Range and compression signal columns.
- [patterns/volatility_regime.py](../patterns/volatility_regime.py): Volatility regime classification.

### Data folder

- [data](../data): Contains CSV market data files for different timeframes and symbols.

### Results folder

- [results](../results): Stores the generated reports and summary CSVs.

### Tests

- [tests](../tests): Unit tests for payload configuration and reaction measurement.

---

## 3. Execution Flow

### Step-by-step pipeline

The flow is:

```text
Program Start
↓
Load Configuration
↓
Load Market Data
↓
Generate Indicators
↓
Generate Combinations
↓
Run Brute Force Analysis
↓
Calculate Statistics
↓
Validation
↓
Ranking
↓
Report Generation
```

### 1. Program Start

Input:
- CLI arguments from [main.py](../main.py)

Outputs:
- either a prepared CSV payload or a full analysis run

Complexity:
- low, mostly argument parsing and file handling

Memory usage:
- minimal

### 2. Load Configuration

Input:
- [payload.json](../payload.json)

Outputs:
- a Python dictionary containing:
  - condition definitions,
  - search depth limits,
  - minimum sample thresholds,
  - lookahead length,
  - validation settings.

Complexity:
- trivial

Memory usage:
- small

### 3. Load Market Data

Input:
- timeframe label such as M1, H1, D1

Outputs:
- a DataFrame with OHLCV columns and a timestamp column

Implementation:
- [loader.py](../loader.py)

Complexity:
- linear in CSV size

Memory usage:
- proportional to the loaded candles

### 4. Generate Indicators

Input:
- raw OHLCV DataFrame

Outputs:
- a richer DataFrame with many additional feature columns

Implementation:
- [prepare_utils.py](../prepare_utils.py)
- each indicator module in [indicators](../indicators)

Complexity:
- roughly $O(n \times p)$ for many rolling/EMA computations, where $n$ is candles and $p$ is the number of indicator periods

Memory usage:
- grows as new columns are added

### 5. Generate Combinations

Input:
- the payload condition list and max depth

Outputs:
- a list of condition tuples, such as:
  - single-condition combos,
  - two-condition combos,
  - three-condition combos,
  - and so on up to max depth

Implementation:
- [analysis/search_space.py](../analysis/search_space.py)

Complexity:
- combinatorial

Memory usage:
- grows with the number of generated combinations

### 6. Run Brute Force Analysis

Input:
- the enriched DataFrame and the generated condition combinations

Outputs:
- a list of candidate matches that satisfy the minimum sample requirement

Implementation:
- [analysis/condition_engine.py](../analysis/condition_engine.py)

Complexity:
- roughly $O(C \times n)$ where $C$ is the number of combinations and $n$ is the number of rows

Memory usage:
- moderate, because each accepted match stores an index list

### 7. Calculate Statistics

Input:
- the DataFrame plus the selected matches

Outputs:
- directional and magnitude statistics for each candidate

Implementation:
- [analysis/reaction_engine.py](../analysis/reaction_engine.py)

Complexity:
- roughly $O(M \times L \times n)$ in the worst case, where $M$ is number of matches and $L$ is lookahead length

Memory usage:
- can be high if every per-entry reaction is stored

### 8. Validation

Input:
- statistically described candidates

Outputs:
- only those that pass stability checks

Implementation:
- [analysis/validator.py](../analysis/validator.py)

Complexity:
- linear in the number of surviving candidates, but each validation re-runs measurement logic on splits

Memory usage:
- moderate

### 9. Ranking

Input:
- validated candidates

Outputs:
- a sorted list ranked by a composite consistency score

Implementation:
- [analysis/ranker.py](../analysis/ranker.py)

Complexity:
- sorting is $O(K \log K)$ for $K$ validated candidates

### 10. Report Generation

Input:
- ranked candidates

Outputs:
- markdown summary and CSV results

Implementation:
- [analysis/reporter.py](../analysis/reporter.py)

---

## 4. Data Pipeline

### Raw dataframe structure

The loader produces a DataFrame with the following core columns:

- `UTC`: timestamp
- `Open`
- `High`
- `Low`
- `Close`
- `Volume`

This is the base candle table.

### Indicator columns

The indicator modules add many columns such as:

- `RSI_7`, `RSI_13`, `RSI_14`, `RSI_21`
- `EMA_5`, `EMA_13`, `EMA_21`, `EMA_50`, `EMA_100`, `EMA_200`
- `SMA_5`, `SMA_20`, etc.
- `ATR_7`, `ATR_13`, `ATR_14`, `ATR_21`
- `ADX_14`
- `MACD_12_26`, `MACD_SIGNAL_9`, `MACD_HIST_12_26_9`
- `BB_UPPER_20_2`, `BB_LOWER_20_2`
- `CCI_9`, `CCI_14`, `CCI_21`

### Signal columns

The payload uses these as condition inputs. A signal column is simply a DataFrame column that can be tested with a comparison operator. Examples include:

- `ADX_14`
- `RSI_14`
- `EMA_50`
- `MACD_12_26`
- `Close`
- `ATR_14`

### Pattern columns

Pattern modules add binary or categorical features such as:

- `DOJI`
- `HAMMER`
- `SHOOTING_STAR`
- `BULL_ENGULF`
- `BEAR_ENGULF`
- `BREAKOUT_UP`
- `BREAKOUT_DOWN`
- `COMPRESSION`
- `VOL_REGIME`

### Temporary columns

The system may create temporary arrays and intermediate Series while computing indicators. These are often not persisted beyond the function call, but they can appear in memory at the same time as the larger DataFrame.

### Derived columns

Some columns are derived from other columns in a way that is useful for conditions or later analysis. This includes:

- ratio-based comparisons,
- rolling thresholds,
- regime labels,
- cross-based signals.

### Important implementation detail

Most indicator modules mutate the existing DataFrame in place or return a new DataFrame with added columns. The workflow assumes that after preparation, the DataFrame contains enough signals for the search engine to test against.

---

## 5. Combination Engine

### How combinations are generated

The search space is built from the condition definitions in [payload.json](../payload.json). Every condition has a name and a definition that says how to evaluate it.

Examples of condition definitions include:

- `RSI14_oversold`: `RSI_14 < 30`
- `EMA21_above_EMA50`: `EMA_21 > EMA_50`
- `MACD_12_26_bear_cross`: `MACD_12_26 < MACD_SIGNAL_9`
- `bull_engulf`: `BULL_ENGULF == 1`

The combination engine then creates tuples of condition names up to a configured maximum depth.

### Why the search space can grow quickly

The search space is not just a simple list of conditions. It grows as the number of possible condition combinations increases.

If there are $n$ available conditions and the engine allows combinations of size up to $d$, then the number of possible combinations is:

$$
\sum_{k=1}^{d} \binom{n}{k}
$$

where:

- $n$ = number of conditions,
- $k$ = combination size,
- $d$ = maximum depth.

### Mathematical explanation

#### Combination notation

The number of ways to choose $k$ items from $n$ items is:

$$
\binom{n}{k} = \frac{n!}{k!(n-k)!}
$$

This is called $n$ choose $k$.

#### Cartesian products

If you were to combine every condition from one set with every condition from another set, that would be a Cartesian product. For example, if one set has 10 conditions and another set has 10 conditions, the cross-product is $10 \times 10 = 100$ pairs.

The project does not use full Cartesian products in the same way; it uses combinations of condition names, but the same combinatorial explosion idea still applies.

#### Combination explosion

The number of combinations grows very rapidly when $n$ is large or when $d$ increases.

Example:

- if there are 30 available conditions,
- and the engine allows depth 4,

then the total number of combinations is:

$$
\binom{30}{1} + \binom{30}{2} + \binom{30}{3} + \binom{30}{4}
$$

which is:

$$
30 + 435 + 4060 + 27405 = 31930
$$

So even with only 30 conditions, depth 4 produces over 31,000 unique combinations.

### Why this matters

A larger search space means:

- more computation,
- more memory usage,
- slower scanning,
- more chances to surface weak or overfitted patterns.

That is why the payload includes limits such as `max_depth`, `min_samples`, and `max_combinations`.

---

## 6. Brute Force Engine Internals

### Iteration strategy

The engine iterates over every generated combination in order and evaluates it against the enriched DataFrame.

For each combination:

1. the engine constructs a boolean mask,
2. the mask is applied to the DataFrame,
3. the number of matches is counted,
4. the combination is retained only if it passes the minimum sample threshold.

### Filtering strategy

A combination is not immediately accepted just because it exists. It must pass multiple filters:

- minimum match count,
- directional consistency,
- magnitude stability,
- frequency range,
- stability across splits.

### Scoring strategy

The engine is not trying to maximize raw profit. Instead, it builds a statistical score from several metrics:

- directional consistency,
- magnitude consistency,
- frequency,
- sample size,
- stability across splits.

### Pruning strategy

There is a practical pruning mechanism at the matching stage:

- if a combination is already false for all rows, the engine stops evaluating the remaining conditions in that combo.

This reduces unnecessary work.

### Early exits

The matching pipeline uses early exits in two important places:

- when the boolean mask becomes all False,
- when a match count is below the threshold.

### Optimization techniques

The implementation uses several practical optimizations:

- vectorized boolean operations rather than row-by-row Python loops where possible,
- NumPy arrays for forward reaction calculations,
- short-circuiting when a combination cannot possibly match further rows,
- batching of indicator and pattern column creation.

### Chunk processing and batching

The loader supports chunked CSV reading when limits are used. This helps when working with large datasets that would otherwise be too large to fit comfortably in memory.

The feature-generation stage also uses batch assignment to append columns in larger blocks rather than repeatedly appending single columns.

---

## 7. Memory Management

### Why RAM usage grows

Memory usage grows because the project does not work with a single candle at a time. It creates:

- a full DataFrame of candles,
- many indicator and pattern columns,
- temporary arrays for rolling operations,
- boolean masks,
- index arrays for matched positions,
- large NumPy arrays used in reaction measurement.

### Which objects are largest

The largest memory consumers are usually:

1. the enriched DataFrame,
2. NumPy arrays created during reaction measurement,
3. the index lists attached to each surviving match,
4. temporary arrays created by rolling window calculations.

### DataFrame memory cost

A pandas DataFrame stores data in columns, and each numeric column consumes memory. Roughly speaking, a NumPy float64 column costs 8 bytes per element. So a column with $n$ rows uses approximately:

$$
8 \times n \text{ bytes}
$$

If a DataFrame has 100,000 rows and 100 numeric columns, the raw numeric payload is roughly:

$$
100{,}000 \times 100 \times 8 = 80{,}000{,}000 \text{ bytes} \approx 76 \text{ MB}
$$

And that does not include pandas overhead, index structures, and object columns.

### Combination storage cost

Every generated combination is stored as a tuple of strings. The total memory for combinations depends on:

- number of combos,
- average combo length,
- overhead from Python objects.

Even a moderate search space can consume much more memory than expected because Python tuples and strings are relatively heavyweight.

### NumPy vs pandas memory usage

NumPy arrays are generally more compact than pandas objects for numeric data. This is why the reaction engine uses NumPy arrays heavily for the forward-reaction calculations.

### Object allocations

The project creates many temporary objects during:

- rolling window calculations,
- boolean mask operations,
- DataFrame concatenation,
- reaction measurement.

Repeated object allocations can increase GC pressure and slow down larger runs.

### Copies vs views

A key subtlety in pandas and NumPy is that some operations create copies while others create views. Copies increase memory pressure. The project uses several operations that can allocate temporary arrays automatically, especially during indicator generation and reaction measurement.

### Memory bottlenecks

The most likely bottlenecks are:

- large DataFrames with many indicator columns,
- storing the full match index for every accepted combination,
- creating large temporary matrices for lookahead windows,
- repeated concatenation of DataFrames during feature engineering.

This is why large datasets can become slow or unstable very quickly.

---

## 8. Limiter System

The payload contains several limits that keep the search tractable.

### Minimum matches

- key: `min_samples`
- default: 5 in the current payload

Purpose:
- prevent very rare patterns from dominating the report.

If removed:
- the engine would consider many weak events and produce a lot of noisy results.

### Direction threshold

- key: `min_direction_pct`
- default: 65.0 in the current payload

Purpose:
- require strong directional preference before a candidate is retained.

If removed:
- the report would include more weak or nearly random setups.

### ATR magnitude filter

- key: `max_mag_cv`
- default: 0.85

Purpose:
- remove candidates whose magnitude estimates are too unstable.

If removed:
- large volatility-driven noise could enter the report.

### Frequency filters

- keys: `min_freq_pct`, `max_freq_pct`

Purpose:
- require the condition to occur often enough to be meaningful, but not so often that it becomes a trivial regime marker.

If removed:
- the pipeline may return either trivial conditions or ultra-frequent but useless ones.

### Combination size limits

- key: `max_depth`

Purpose:
- control how large the search space becomes.

If removed or raised too high:
- the number of combinations can explode quickly.

### Maximum combinations

- key: `max_combinations`

Purpose:
- hard cap the search space.

In the current payload, this value is effectively enormous, so the cap is essentially disabled.

### Worker limits

The current project does not expose a worker-pool system in the main pipeline. The computation is effectively single-threaded over combinations.

### Chunk size limits

The loader supports chunked reads via `chunksize` and can limit the loaded number of rows. This helps control memory use.

---

## 9. Statistics and Metrics

This section explains how each reported metric is computed.

### Consistency Score

The consistency score is calculated in [analysis/ranker.py](../analysis/ranker.py).

It uses a weighted blend of:

- directional consistency,
- magnitude consistency,
- frequency,
- sample size,
- stability.

The formula is:

$$
Score = 0.35 \cdot dir\_score + 0.25 \cdot mag\_score + 0.15 \cdot freq\_score + 0.15 \cdot sample\_score + 0.10 \cdot stability\_score
$$

Where:

- $dir\_score = \frac{dir\_consistency}{100}$
- $mag\_score = \max(0, 1 - CV)$
- $freq\_score = \min\left(\frac{freq\_pct}{2}, 1\right)$
- $sample\_score = \min\left(\frac{valid\_count}{200}, 1\right)$
- $stability\_score = \frac{\text{number of successful splits}}{\text{total splits}}$

Meaning:
- higher score means the candidate is more statistically attractive,
- lower CV and higher consistency improve the score.

### Match Count

This is the number of valid reaction windows after filtering the positions that run out of data.

In the code this is represented as `valid_count`.

Meaning:
- higher is usually better,
- but it must be interpreted with frequency and stability.

### Dominant Direction

The engine measures three categories:

- bullish,
- bearish,
- neutral.

The dominant direction is the category with the highest count among those three.

Meaning:
- it tells you which directional outcome occurred most often for that condition.

### Direction %

This is the percentage of the candidate’s reaction outcomes that fall into the dominant direction.

The code computes:

$$
dir\_pct = \max(bull\_pct, bear\_pct)
$$

Meaning:
- if a candidate is 57.1% bullish, that means the dominant direction accounted for 57.1% of the observed outcomes.

### Mag ATR Mean

For every matched event, the engine computes a magnitude in ATR units.

The magnitude is the larger of the bullish or bearish excursion normalized by ATR:

$$
mag\_atr = \max\left(\frac{up\_move}{ATR}, \frac{down\_move}{ATR}\right)
$$

The reported mean is the average of these magnitudes over all valid outcomes.

Meaning:
- larger values imply stronger average reaction magnitude in ATR terms.

### Mag ATR Std

This is the standard deviation of the per-event ATR-normalized magnitude values.

Meaning:
- a lower standard deviation means the setup produces more consistent magnitudes.

### Mag CV

The magnitude coefficient of variation is:

$$
CV = \frac{std}{mean}
$$

Meaning:
- low CV means the magnitude is stable,
- high CV means the magnitude is volatile.

### Timing

Timing measures how many candles it takes for the dominant directional move to reach its best excursion within the lookahead window.

Meaning:
- lower timing values imply the move happened earlier in the lookahead window.

### Persistence

Persistence measures how many future candles remain on the same side of the entry close as the dominant direction.

For a bullish candidate, the engine counts how many future closes are above the entry close. For a bearish candidate, it counts how many future closes are below the entry close.

Meaning:
- higher persistence means the signal held longer after the condition occurred.

### Frequency

Frequency is computed as:

$$
frequency\_pct = \frac{valid\_count}{total\_candles} \times 100
$$

Meaning:
- it tells you how often the condition occurred in the full history.

### Overfit Status

The system labels a candidate as `STABLE` only if it passes the validation logic.

The validator checks whether the candidate remains directionally consistent across splits and does not degrade too significantly.

---

## 10. Validation System

### Why validation exists

The project is vulnerable to overfitting because it scans many combinations. A setup that looks good on one part of history might fail later.

Validation is therefore used to test whether a candidate is robust.

### Train / validation / OOS splits

The validator splits the dataframe into three regions:

- `train`
- `val`
- `oos`

The split boundaries are based on the configured `validation_split`:

- $train$ = first $1 - 2 \cdot split$ fraction of the data
- $val$ = middle fraction
- $oos$ = final fraction

With a default of $0.2$, the splits are roughly:

- train: 60% of the data,
- validation: 20%,
- out-of-sample: 20%.

### Why each split exists

- `train`: used to discover the candidate pattern.
- `val`: used to check whether the setup still behaves reasonably during a middle segment.
- `oos`: used to check robustness on a truly unseen tail segment.

### How data leakage is prevented

The validator re-measures the condition using only the candles in the split under consideration. This prevents the same historical event from being evaluated in ways that leak information from neighboring periods.

### Stability criteria

A candidate is considered stable if:

- it has enough support in the split,
- the dominant direction is not flipped,
- the directional percentage does not degrade too much.

The `dir_grace` setting controls how much degradation is allowed.

---

## 11. Result Ranking

### Sorting algorithm

After validation, candidates are sorted by `consistency_score` in descending order.

The ranking is implemented in [analysis/ranker.py](../analysis/ranker.py).

### Ranking criteria

The score includes:

- direction quality,
- magnitude stability,
- frequency,
- sample size,
- split stability.

### Tie breakers

There are no explicit tie-breakers beyond the order of the input list and the score. In practice, if two candidates have the same score, the one that appears first in the validated list will rank higher.

### Filtering pipeline

The full pipeline before final ranking is:

1. minimum sample threshold,
2. directional filter,
3. magnitude CV filter,
4. frequency filter,
5. validation stability filter,
6. ranking.

---

## 12. Report Generation

The final report is generated by [analysis/reporter.py](../analysis/reporter.py) and saved as:

- [results/report.md](../results/report.md)
- [results/final_results.csv](../results/final_results.csv)

### Example report entry

The report example in the prompt is a condition label such as:

```text
ADX_strong_trend + EMA50_above_EMA100 + MACD_bear_cross + vol_spike_3x
```

The engine produces the report entry using the same pipeline regardless of the exact names. The precise steps are:

### 1. How this combination was found

The combination was found because the payload defined the corresponding condition names and the search engine generated all combinations up to the configured depth. Each condition was evaluated against the DataFrame using the condition engine. When all conditions in the tuple were simultaneously true, the event was recorded as a match.

### 2. How 136 matches were obtained

The number 136 corresponds to the number of valid positions where the composite condition fired and where the future reaction window had enough data to be evaluated.

The pipeline does this by:

1. evaluating the boolean mask for the composite condition,
2. counting how many candles satisfied all component conditions,
3. discarding those that do not have valid forward lookahead data,
4. counting the remaining valid entries.

### 3. How 55.1% bullish was calculated

The reaction engine evaluates the future reaction for each match. It computes whether the next several candles move bullish or bearish relative to the entry close. The `bull_pct` value is the proportion of outcomes in the bullish category.

If the candidate had 75 bullish outcomes and 61 bearish outcomes out of 136 total valid events, then the bullish percentage would be:

$$
\frac{75}{136} \times 100 \approx 55.1\%
$$

### 4. How 1.3723 ATR was calculated

For each event, the engine computes the maximum favorable or adverse excursion normalized by ATR. These per-event magnitudes are then averaged.

If the per-event ATR-normalized magnitudes are $m_1, m_2, ..., m_n$, then:

$$
\text{Mag ATR Mean} = \frac{1}{n} \sum_{i=1}^{n} m_i
$$

### 5. How Mag CV was calculated

The magnitude standard deviation is divided by the magnitude mean:

$$
CV = \frac{\sigma}{\mu}
$$

If the magnitude mean is $1.3723$ and the standard deviation is $0.6799$, then:

$$
CV \approx \frac{0.6799}{1.3723} \approx 0.4954
$$

### 6. How persistence was calculated

The engine counts how many future closes remain on the dominant side of the entry close.

For a bullish candidate, it counts future closes above the entry close. For a bearish candidate, it counts future closes below the entry close.

The reported persistence is the mean of those counts across all events.

### 7. How frequency was calculated

Frequency is computed from the total number of candles in the loaded dataset:

$$
frequency\_pct = \frac{valid\_count}{total\_candles} \times 100
$$

If the dataset has 117,000 candles and the candidate has 136 valid events, the frequency would be:

$$
\frac{136}{117000} \times 100 \approx 0.116\%
$$

### 8. How split validation values were produced

The validator re-measures the same candidate on the train, validation, and out-of-sample portions of the dataset. It reuses the same logic but with only the split-specific candle range.

The output shows values such as:

- train count and direction,
- validation count or insufficient status,
- OOS count and direction.

### 9. Why the result was labeled STABLE

The result is labeled `STABLE` when the candidate passes the validation logic, meaning:

- it has enough support in at least two splits,
- the dominant direction does not flip across splits,
- its directional quality does not degrade too much.

---

## 13. Performance Analysis

### Time complexity

The dominant cost is the brute-force scan.

If there are $C$ candidate combinations and $n$ candles, the scan is roughly:

$$
O(C \cdot n)
$$

The reaction measurement step is another significant cost, especially with larger lookahead windows.

### Memory complexity

Memory grows roughly with:

- the size of the enriched DataFrame,
- the number of surviving matches,
- the number of per-event reactions stored if requested.

### Worst-case scenarios

Worst-case performance happens when:

- the search space is large,
- the lookahead is large,
- the history is long,
- many combinations pass the minimum sample filter.

### Scalability limitations

The current implementation is practical for exploratory research on moderate datasets, but it does not scale gracefully to extremely large search spaces without additional optimization.

### Bottlenecks

The main bottlenecks are:

- scanning all combinations,
- generating many temporary arrays,
- storing match indices,
- repeated evaluation of forward reactions.

---

## 14. Developer Notes

### Hidden assumptions

The project assumes that:

- the input data is already clean enough for technical indicator computation,
- the conditions in the payload are meaningful,
- the generated DataFrame is the single source of truth for analysis,
- the report is intended for research purposes rather than live execution.

### Potential bugs or fragility

Possible areas of concern include:

- some indicator modules create columns using pandas concatenation in ways that may be memory-intensive,
- the current payload includes a very large `max_combinations` value, which effectively disables the cap,
- the code relies heavily on the presence of specific column names in the enriched DataFrame,
- the validator’s split logic assumes that the input data is ordered chronologically.

### Technical debt

The codebase is functional but still research-oriented. Some notable technical debt includes:

- a lot of logic is embedded directly in the analysis pipeline rather than abstracted into reusable utilities,
- the project does not yet expose a more sophisticated parallel execution framework,
- there is room to reduce temporary allocations and improve memory efficiency.

### Areas for future optimization

Potential future improvements include:

- chunked or streaming evaluation for very large datasets,
- more aggressive pruning,
- parallel evaluation of combinations,
- compressed or sparse representations for match indexes,
- caching of intermediate indicator columns.

---

## Closing Summary

AlphaHunter is a research-oriented brute-force pattern discovery system. Its purpose is not to provide a single ready-to-trade strategy, but to identify conditions that have historically produced measurable and statistically interesting reactions.

The project works because it combines:

- a rich feature engineering stage,
- a combinational search engine,
- a forward-reaction measurement layer,
- statistical filters,
- a validation system,
- and report generation.

Understanding these pieces is the key to making sense of the generated reports and to extending the project responsibly.
