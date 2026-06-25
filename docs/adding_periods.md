# Adding a new moving-average period

This project computes indicators such as RSI, stochastic, MACD, ATR, CCI, Bollinger Bands, and moving averages during the prepare step. If you want a new period or a new signal to participate in the analysis, you need to make sure it exists in two places:

1. The indicator module that creates the column.
2. The payload file that tells the condition engine which columns to evaluate.

For higher-quality signals across high and low timeframes, keep the payload varied by combining:
- oscillator thresholds such as RSI and stochastic,
- trend cross conditions such as EMA and MACD,
- volatility and range conditions such as ATR and Bollinger Bands,
- pattern flags such as engulfing and squeeze.

## Example: add RSI 21

### 1) Make sure the indicator creates the column
The RSI indicator already computes RSI values for 7, 14, and 21 in [indicators/rsi.py](../indicators/rsi.py), so the column RSI_21 is produced automatically.

### 2) Add a condition to the payload
Add one or more conditions to [payload.json](../payload.json) and [payload.md](../payload.md).

Example:

```json
{
  "name": "RSI21_oversold",
  "type": "threshold",
  "col": "RSI_21",
  "op": "<",
  "val": 30
}
```

For a 21-period moving average, you can also add:

```json
{
  "name": "EMA21_above_Close",
  "type": "cross",
  "col": "EMA_21",
  "op": ">",
  "col2": "Close"
}
```

### 3) Rebuild the enriched payload
Run:

```bash
python main.py prepare --tf D1
```

Then run analysis:

```bash
python main.py run --tf D1 --payload payload.json
```

## General rule

If you add a new period to an indicator, the matching column name must be present in the prepared dataframe, and the payload must reference that column name explicitly.
