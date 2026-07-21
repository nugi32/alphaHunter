import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import main


def test_resolve_project_path_uses_repo_root_for_relative_inputs(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    resolved = main.resolve_project_path("payload.json")

    assert resolved == Path(main.__file__).resolve().parent / "payload.json"
    assert resolved.exists()


def test_payload_includes_richer_signal_conditions():
    payload = json.loads((ROOT / "payload.json").read_text())
    condition_names = {condition["name"] for condition in payload["conditions"]}

    assert "RSI21_oversold" in condition_names
    assert "RSI21_overbought" in condition_names
    assert "RSI13_oversold" in condition_names
    assert "STO_K14_oversold" in condition_names
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

    assert not any(
        condition.get("col") == "EMA_50" or condition.get("col2") == "EMA_50"
        for condition in payload["conditions"]
    )
    assert not any(
        condition.get("col") == "RSI_50" or condition.get("col2") == "RSI_50"
        for condition in payload["conditions"]
    )
    assert not any(
        condition.get("col") == "ATR_55" or condition.get("col2") == "ATR_55"
        for condition in payload["conditions"]
    )

    assert payload["memory_spill_threshold_percent"] == 20
    assert payload["storage_backend"] == "sqlite"
    assert payload["storage_path"] == "./spool.db"
