import pandas as pd
import matplotlib.pyplot as plt
import os
from pathlib import Path

def ensure_reports_dir(base_path="reports"):
    """Ensure reports directory exists"""
    Path(base_path).mkdir(parents=True, exist_ok=True)

def generate_histogram(df, base_path="reports", filename="histogram.png"):
    """Generate histogram for PriceMove distribution"""
    ensure_reports_dir(base_path)
    
    path = os.path.join(base_path, filename)
    
    plt.figure(figsize=(9, 5))
    
    price_move = (df["Close"] - df["Open"]) / df["Open"] * 100
    plt.hist(
        price_move,
        bins=35,
        alpha=0.75
    )
    
    plt.axvline(
        price_move.mean(),
        linestyle="--",
        linewidth=2,
        label=f"Mean: {price_move.mean():.2f}%"
    )
    
    plt.axvline(
        price_move.median(),
        linestyle=":",
        linewidth=2,
        label=f"Median: {price_move.median():.2f}%"
    )
    
    plt.grid(alpha=0.25, axis="y")
    plt.xlabel("Price Move (%)")
    plt.ylabel("Count")
    plt.title("Price Movement Distribution")
    plt.legend()
    plt.savefig(path, dpi=100, bbox_inches='tight')
    plt.close()
    
    return path

def generate_scatter(df, base_path="reports", filename="scatter.png"):
    """Generate scatter plot if RSI_14 exists"""
    ensure_reports_dir(base_path)
    
    path = os.path.join(base_path, filename)
    
    plt.figure(figsize=(9, 5))
    
    price_move = (df["Close"] - df["Open"]) / df["Open"] * 100
    if "RSI_14" in df.columns:
        plt.scatter(
            df["RSI_14"],
            price_move,
            alpha=0.25,
            s=18
        )
        plt.xlabel("RSI_14")
    else:
        plt.scatter(
            df.index,
            price_move,
            alpha=0.25,
            s=18
        )
        plt.xlabel("Time Index")
    
    plt.axhline(0, linestyle="--", linewidth=1)
    plt.grid(alpha=0.2)
    plt.ylabel("Price Move")
    plt.title("Price Movement Analysis")
    plt.savefig(path, dpi=100, bbox_inches='tight')
    plt.close()
    
    return path

def build_stats(df):
    """Build statistics from dataframe"""
    total = len(df)
    
    # Reaction move within each candle as percentage of open
    price_move = (df["Close"] - df["Open"]) / df["Open"] * 100
    
    bullish = int((price_move > 0).sum())
    bearish = int((price_move < 0).sum())
    neutral = int((price_move == 0).sum())
    
    avg = float(price_move.mean())
    median = float(price_move.median())
    std = float(price_move.std())
    var = float(price_move.var())

    return {
        "total": total,
        "bullish": bullish,
        "bearish": bearish,
        "neutral": neutral,
        "bullish_pct": round(bullish / total * 100, 2) if total else 0,
        "bearish_pct": round(bearish / total * 100, 2) if total else 0,
        "neutral_pct": round(neutral / total * 100, 2) if total else 0,
        "avg_move": round(avg, 4),
        "median_move": round(median, 4),
        "std_move": round(std, 4),
        "var_move": round(var, 4),
    }
    

def generate_insight(df):
    """Generate insights from data"""
    price_move = (df["Close"] - df["Open"]) / df["Open"] * 100
    
    total = len(price_move)
    bullish_pct = (price_move > 0).sum() / total if total else 0
    bearish_pct = (price_move < 0).sum() / total if total else 0
    neutral_pct = (price_move == 0).sum() / total if total else 0
    avg = float(price_move.mean())
    std = float(price_move.std())
    
    dominant = "bullish" if bullish_pct >= bearish_pct and bullish_pct >= neutral_pct else "bearish" if bearish_pct >= bullish_pct and bearish_pct >= neutral_pct else "neutral"
    directional_confidence = max(bullish_pct, bearish_pct, neutral_pct) * 100
    dispersion = std
    
    text = [
        f"Dominant price reaction: {dominant} ({directional_confidence:.1f}% of candles).",
        f"Average move: {avg:.3f}%.",
        f"Move dispersion (std): {dispersion:.3f}%."
    ]
    
    if dispersion < abs(avg) * 0.5 if abs(avg) > 0 else False:
        text.append("Move sizes are relatively clustered around the mean.")
    else:
        text.append("Move sizes show wider dispersion, investigate stability further.")
    
    return " ".join(text)

from jinja2 import Environment, FileSystemLoader

def generate_report(df, tf, pattern, base_path="report/templates", pattern_discovery_results=None):
    """Generate HTML report from dataframe"""
    
    ensure_reports_dir("report/reports")
    
    env = Environment(
        loader=FileSystemLoader(base_path)
    )
    
    template = env.get_template("report.html")
    
    stats = build_stats(df)
    
    hist = generate_histogram(df, base_path="report/reports", filename=f"{tf}_{pattern}_histogram.png".replace(">", "gt").replace("<", "lt"))
    scatter = generate_scatter(df, base_path="report/reports", filename=f"{tf}_{pattern}_scatter.png".replace(">", "gt").replace("<", "lt"))
    
    # Prepare sample data
    sample_cols = [col for col in df.columns if col in ['UTC', 'Open', 'High', 'Low', 'Close', 'Volume']]
    sample_table = df[sample_cols].head(10).to_html(classes='table table-sm', index=False) if sample_cols else df.head(10).to_html(classes='table table-sm')
    
    # Prepare pattern discovery table
    pattern_discovery_table = ""
    if pattern_discovery_results and pattern_discovery_results.get('patterns'):
        pattern_rows = []
        for p in pattern_discovery_results['patterns']:
            pattern_rows.append(f"""
            <tr>
                <td>{p['indicators']}</td>
                <td>{p['frequency']}</td>
                <td>{p['dominant_direction']}</td>
                <td>{p['directional_confidence']}</td>
                <td>{p['avg_move']}</td>
                <td>{p['move_std']}</td>
                <td>{p['p10']}</td>
                <td>{p['p90']}</td>
                <td>{p['quality_score']}</td>
            </tr>
            """)
        
        pattern_discovery_table = f"""
        <h2>🎯 Discovered Patterns (Top 10)</h2>
        <p>These patterns are automatically discovered combinations of indicators that show repeatable directional reaction behavior and clustered move magnitude.</p>
        <table class="table table-sm table-striped">
            <thead style="background-color: #f0f0f0;">
                <tr>
                    <th>Indicator Combination</th>
                    <th>Frequency</th>
                    <th>Dominant Direction</th>
                    <th>Directional Confidence</th>
                    <th>Avg Move %</th>
                    <th>Std Dev</th>
                    <th>P10</th>
                    <th>P90</th>
                    <th>Quality Score</th>
                </tr>
            </thead>
            <tbody>
                {''.join(pattern_rows)}
            </tbody>
        </table>
        """
    
    html = template.render(
        title=f"{tf} | {pattern}",
        total=stats["total"],
        bullish=stats["bullish"],
        bearish=stats["bearish"],
        neutral=stats["neutral"],
        avg_move=stats["avg_move"],
        median_move=stats["median_move"],
        std_move=stats["std_move"],
        var_move=stats["var_move"],
        hist_chart=os.path.basename(hist),
        scatter_chart=os.path.basename(scatter),
        sample_table=sample_table,
        insight=generate_insight(df),
        pattern_discovery_table=pattern_discovery_table,
    )
    
    output = (
        f"report/reports/{tf}_{pattern}.html"
        .replace(">", "gt")
        .replace("<", "lt")
    )
    
    os.makedirs(os.path.dirname(output), exist_ok=True)
    
    with open(output, "w", encoding="utf-8") as f:
        f.write(html)
    
    return output