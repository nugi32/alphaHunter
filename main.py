#!/usr/bin/env python3
"""
Main orchestrator for alphaHunter analysis and report generation.
Runs analysis for multiple timeframes and generates reports.
"""

import argparse
import sys
import pandas as pd
from pathlib import Path
from analysis import run_analysis
from report.report_generator import generate_report

TIMEFRAMES = ["M1", "M5", "M15", "H1", "H4", "D1", "W1", "MN1"]

def run_single_analysis(tf, pattern=None, save_report=True):
    """Run analysis for a single timeframe"""
    print(f"\n{'='*70}")
    print(f"Running analysis for {tf}")
    print(f"{'='*70}")
    
    csv_name = f"output_{tf}.csv"
    
    try:
        result = run_analysis(
            save_csv=True,
            csv_name=csv_name,
            timeframe=tf,
            pattern_spec=pattern
        )
        
        if save_report and result["merged"] is not None:
            df = result["merged"]
            pattern_label = pattern if pattern else "all"
            print(f"\nGenerating report for {tf}...")
            pattern_discovery_results = result.get("pattern_discovery_results")
            # Generate report (do not print the file path)
            _ = generate_report(df, tf, pattern_label, pattern_discovery_results=pattern_discovery_results)

            # Log analysis results to terminal for debugging and verification
            print("\n--- Pattern discovery results ---")
            if pattern_discovery_results:
                total_found = pattern_discovery_results.get('total_patterns_found', None)
                patterns_list = pattern_discovery_results.get('patterns', [])
                if total_found is None:
                    total_found = len(patterns_list)
                print(f"Total patterns found: {total_found}")
                if patterns_list:
                    print("Top patterns summary:")
                    for p in patterns_list[:10]:
                        ind = p.get('indicators')
                        freq = p.get('frequency')
                        dom = p.get('dominant_direction')
                        conf = p.get('directional_confidence')
                        print(f" - {ind} | freq={freq} | dir={dom} | conf={conf}")
                else:
                    print("No pattern entries in pattern_discovery_results.")
            else:
                print("No patterns discovered or pattern discovery results empty.")

            print("\n--- Correlations ---")
            correlations = result.get("correlations")
            if correlations is None:
                print("No correlations computed.")
            else:
                try:
                    # If correlations is a DataFrame-like object, show shape and head
                    if hasattr(correlations, 'shape') and hasattr(correlations, 'head'):
                        print(f"Correlations: shape={correlations.shape}")
                        try:
                            print(correlations.head().to_string())
                        except Exception:
                            print(repr(correlations.head()))
                    elif isinstance(correlations, dict):
                        print(f"Correlations keys: {list(correlations.keys())}")
                        for k in list(correlations.keys())[:10]:
                            print(f" - {k}: {correlations[k]}")
                    else:
                        print(repr(correlations))
                except Exception as e:
                    print(f"Error printing correlations: {e}")
        
        # Print summary if pattern was specified
        if pattern and result["pattern_summary"]:
            summary = result["pattern_summary"]
            print(f"\n[Pattern Analysis] {tf}")
            print(f"  Matches: {len(summary.get('matches', []))}")
            
        return result
        
    except Exception as e:
        print(f"✗ Error analyzing {tf}: {e}", file=sys.stderr)
        return None

def run_all_timeframes(pattern=None, timeframes=None):
    """Run analysis for all or specified timeframes"""
    if timeframes is None:
        timeframes = TIMEFRAMES
    
    results = {}
    
    for tf in timeframes:
        print(f"\n[{tf}] Processing...")
        result = run_single_analysis(tf, pattern=pattern, save_report=True)
        if result:
            results[tf] = result
    
    print(f"\n{'='*70}")
    print("Analysis complete!")
    print(f"{'='*70}")
    print(f"Processed {len(results)}/{len(timeframes)} timeframes")
    
    return results

def run_with_patterns(patterns_list):
    """Run analysis for each pattern in the list"""
    print(f"\nRunning analysis for {len(patterns_list)} patterns...")
    
    results = {}
    for pattern in patterns_list:
        pattern_clean = pattern.replace(">", "gt").replace("<", "lt").replace(",", "_")
        print(f"\n[Pattern] {pattern}")
        result = run_single_analysis("D1", pattern=pattern, save_report=True)
        if result:
            results[pattern] = result
    
    return results

def main():
    parser = argparse.ArgumentParser(
        description="AlphaHunter - Multi-timeframe analysis and report generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py                                    # Run all timeframes
  python main.py --tf D1 H4 H1                      # Run specific timeframes
  python main.py --tf D1 --pattern "RSI>50,ADX>=20" # Run with pattern
  python main.py --patterns file.txt                # Run multiple patterns from file
        """
    )
    
    parser.add_argument(
        "--tf",
        nargs="+",
        choices=TIMEFRAMES,
        help="Timeframes to analyze (default: all)"
    )
    
    parser.add_argument(
        "--pattern",
        default=None,
        help="Pattern condition to analyze (e.g., RSI_14>70,MACD>MACD_SIGNAL)"
    )
    
    parser.add_argument(
        "--patterns",
        default=None,
        help="File containing list of patterns (one per line)"
    )
    
    parser.add_argument(
        "--no-report",
        action="store_true",
        help="Skip report generation"
    )
    
    args = parser.parse_args()
    
    # Determine what to run
    if args.patterns:
        # Load patterns from file
        if not Path(args.patterns).exists():
            print(f"Error: Pattern file not found: {args.patterns}", file=sys.stderr)
            sys.exit(1)
        
        with open(args.patterns, 'r') as f:
            patterns = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        
        run_with_patterns(patterns)
        
    elif args.pattern:
        # Single pattern analysis
        timeframes = args.tf or ["D1"]
        for tf in timeframes:
            run_single_analysis(tf, pattern=args.pattern, save_report=not args.no_report)
            
    else:
        # Regular multi-timeframe analysis
        timeframes = args.tf or TIMEFRAMES
        run_all_timeframes(pattern=None, timeframes=timeframes)

if __name__ == "__main__":
    main()
