from analysis.consistency import diagnose_thresholds


def test_diagnose_thresholds_handles_empty_enriched_results(capsys):
    diagnose_thresholds([])

    captured = capsys.readouterr()
    assert "THRESHOLD DIAGNOSTICS" in captured.out
    assert "n=0" in captured.out
