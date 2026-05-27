import pandas as pd
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from report_generator import generate_report

def main():
    """Run report generation from existing CSV files"""
    
    # Find CSV files in current directory
    import glob
    csv_files = glob.glob("output_*.csv")
    
    if not csv_files:
        csv_files = glob.glob("*.csv")
    
    if not csv_files:
        print("No CSV files found. Run analysis.py first.")
        print("\nUsage:")
        print("  python ../analysis.py --tf D1")
        print("  python run_report.py")
        return
    
    for csv_file in csv_files:
        print(f"Processing {csv_file}...")
        
        try:
            df = pd.read_csv(csv_file, parse_dates=["UTC"])
            
            # Extract timeframe from filename (e.g., output_D1.csv -> D1)
            parts = csv_file.replace("output_", "").replace(".csv", "")
            tf = parts.split("_")[0] if "_" in parts else parts
            
            pattern = "all"
            
            generate_report(df, tf, pattern)
            
        except Exception as e:
            print(f"Error processing {csv_file}: {e}")
            continue
    
    print("\nReport generation complete!")

if __name__ == "__main__":
    main()
