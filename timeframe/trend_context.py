import pandas as pd


def apply(df):
    result = df.copy()

    stacked = pd.concat(
        [
            pd.DataFrame(
                {
                    "TF_BULL_STACK": (
                        (result["EMA_20"] > result["EMA_50"])
                        & (result["M15_EMA_20"] > result["M15_EMA_50"])
                        & (result["H1_EMA_20"] > result["H1_EMA_50"])
                    ).astype(int),
                    "TF_BEAR_STACK": (
                        (result["EMA_20"] < result["EMA_50"])
                        & (result["M15_EMA_20"] < result["M15_EMA_50"])
                        & (result["H1_EMA_20"] < result["H1_EMA_50"])
                    ).astype(int),
                },
                index=result.index,
            )
        ],
        axis=1,
    )

    return pd.concat([result, stacked], axis=1)
