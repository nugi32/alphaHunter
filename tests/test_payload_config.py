import json
from pathlib import Path


def test_payload_includes_richer_signal_conditions():
    payload = json.loads(Path("payload.json").read_text())
    condition_names = {condition["name"] for condition in payload["conditions"]}

    assert "RSI21_oversold" in condition_names
    assert "RSI21_overbought" in condition_names
    assert "RSI13_oversold" in condition_names
    assert "STO_K_14_oversold" in condition_names
    assert "EMA13_above_EMA21" in condition_names
    assert "close_above_BB_UPPER_20_2" in condition_names
    assert "MACD_9_21_bull_cross" in condition_names
    assert "CCI21_oversold" in condition_names
    assert "ATR14_vs_close_ratio" in condition_names

    rsi21_condition = next(
        condition
        for condition in payload["conditions"]
        if condition["name"] == "RSI21_oversold"
    )
    assert rsi21_condition["col"] == "RSI_21"
