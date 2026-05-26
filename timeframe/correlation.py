def analyze(df):
    pairs = [
        ("EMA_20", "M15_EMA_20"),
        ("RSI_14", "H1_RSI_14"),
        ("ATR_14", "H4_ATR_14"),
    ]

    for a, b in pairs:
        if a in df.columns and b in df.columns:
            corr = df[a].corr(df[b])
            print(a, b, corr)
