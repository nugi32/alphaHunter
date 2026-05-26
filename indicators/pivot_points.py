def apply(df):
    pivot = (df["High"] + df["Low"] + df["Close"]) / 3

    df["PIVOT"] = pivot
    df["R1"] = pivot * 2 - df["Low"]
    df["S1"] = pivot * 2 - df["High"]

    return df
