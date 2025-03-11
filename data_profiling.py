import pandas as pd
import os
from ydata_profiling import ProfileReport
import webbrowser

# File path
FILE_PATH = r"C:\Data Science\super_dataset_csv.csv"
REPORT_PATH = r"C:\Data Science\super_dataset_profile.html"

def generate_profiling_report():
    """Generate and save a YData profiling report with error handling and user-friendly messages."""
    
    if not os.path.exists(FILE_PATH):
        print(f"❌ Error: The file '{FILE_PATH}' does not exist. Please check the file path.")
        return

    print("📊 Loading dataset...")
    df = pd.read_csv(FILE_PATH)

    print("🔍 Generating YData profiling report. This may take a few minutes...")
    profile = ProfileReport(df, title="Super Dataset Profiling Report", explorative=True)
    
    print("💾 Saving the report...")
    profile.to_file(REPORT_PATH)

    print(f"✅ Data profiling report saved at {REPORT_PATH}")

    # Optional: Open the report automatically in the default web browser
    webbrowser.open(REPORT_PATH)

if __name__ == "__main__":
    generate_profiling_report()
