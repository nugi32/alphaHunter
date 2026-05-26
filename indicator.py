import pandas as pd

from loader import loadPrice

from indicators import (
    adx,
    advanced,
    atr,
    bollinger,
    cci,
    fibonacci,
    ichimoku,
    macd,
    momentum,
    pivot_points,
    rsi,
    stochastic,
    trend_ma,
    volatility,
    volume,
)


modules = [
    trend_ma,
    macd,
    bollinger,
    rsi,
    stochastic,
    atr,
    adx,
    cci,
    momentum,
    volume,
    volatility,
    ichimoku,
    fibonacci,
    pivot_points,
    advanced,
]

"""
def main():
    df = loadPrice()

    for module in modules:
        df = module.apply(df)

    print(df.tail())
    df.to_csv("XAU_USD_all_indicators.csv", index=False)


if __name__ == "__main__":
    main()
"""


def main():
    data = loadPrice()

    for tf, df in data.items():
        for module in modules:
            df = module.apply(df)

        print(f"\n=== {tf} ===")
        print(df.tail())

        df.to_csv(f"XAU_USD_{tf}_all_indicators.csv", index=False)


if __name__ == "__main__":
    main()