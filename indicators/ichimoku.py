import pandas as pd


def apply(df):
    """
    Calculate complete Ichimoku Kinko Hyo indicator.
    Includes: Tenkan, Kijun, Senkou Span A, Senkou Span B, Chikou Span, Cloud.
    """
    # Tenkan-sen (9-period high + low) / 2
    tenkan = (df["High"].rolling(9).max() + df["Low"].rolling(9).min()) / 2

    # Kijun-sen (26-period high + low) / 2
    kijun = (df["High"].rolling(26).max() + df["Low"].rolling(26).min()) / 2

    # Senkou Span A: (Tenkan + Kijun) / 2, shifted forward 26 periods
    senkou_a = ((tenkan + kijun) / 2).shift(26)

    # Senkou Span B: (52-period high + low) / 2, shifted forward 26 periods
    senkou_b = ((df["High"].rolling(52).max() + df["Low"].rolling(52).min()) / 2).shift(26)

    # Chikou Span: Close shifted back 26 periods (for future reference)
    chikou = df["Close"].shift(-26)

    extra = {
        "TENKAN": tenkan,
        "KIJUN": kijun,
        "SENKOU_A": senkou_a,
        "SENKOU_B": senkou_b,
        "CHIKOU": chikou,
        "CLOUD_TOP": pd.concat([senkou_a, senkou_b], axis=1).max(axis=1),
        "CLOUD_BOTTOM": pd.concat([senkou_a, senkou_b], axis=1).min(axis=1),
    }

    return pd.concat([df, pd.DataFrame(extra, index=df.index)], axis=1)
