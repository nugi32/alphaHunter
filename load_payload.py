import argparse
from pathlib import Path
from typing import Optional

from analysis import prepare, timed_spinner
from loader import load_tf


def save_payload(timeframe: str, output_path: Optional[str] = None, limit: Optional[int] = None):
    """Load timeframe data, enrich with indicators and patterns, and save to CSV."""
    if output_path is None:
        output_path = f"payload_{timeframe}.csv"

    with timed_spinner(f"Loading timeframe data: {timeframe}"):
        df = load_tf(timeframe, limit=limit)

    with timed_spinner("Applying indicators and patterns"):
        df = prepare(df)

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False, encoding="utf-8")
    print(f"Payload saved: {output_path} ({len(df)} rows)")
    return output_path


def main():
    parser = argparse.ArgumentParser(
        description="Load candlestick payload, enrich with indicators and patterns, and save to CSV."
    )
    parser.add_argument(
        "--tf",
        default="D1",
        choices=["M1", "M5", "M15", "H1", "H4", "D1", "W1", "MN1"],
        help="Timeframe to load and enrich.",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Output CSV filename. Defaults to payload_{tf}.csv.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Optional number of candles to load from the end of the timeframe dataset.",
    )

    args = parser.parse_args()
    save_payload(args.tf, args.output, limit=args.limit)


if __name__ == "__main__":
    main()
