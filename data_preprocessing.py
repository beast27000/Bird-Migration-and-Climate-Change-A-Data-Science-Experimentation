import pandas as pd

# File paths
INPUT_FILE = r"C:\Data Science\super_dataset_csv.csv"
OUTPUT_FILE = r"C:\Data Science\wrangled_data.csv"

def wrangle_data():
    """Perform data cleaning and transformation, saving to a new file."""

    # Load dataset with proper encoding
    df = pd.read_csv(INPUT_FILE, encoding="latin1")

    # 🔥 Strip spaces from column names
    df.columns = df.columns.str.strip()

    # Rename columns for consistency
    df.rename(columns={"Temperature": "Temperature (°C)", "Humidity": "Humidity (%)"}, inplace=True)

    # Drop unnecessary columns
    drop_cols = ["Latitude", "Longitude", "Unnamed: 10"]  # Removing extra columns
    df.drop(columns=drop_cols, inplace=True, errors="ignore")

    # Convert 'Date' to datetime format
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # Handle missing values
    df.fillna({
        "Species": "Unknown",
        "Weather": "Unknown",
        "Temperature (°C)": df["Temperature (°C)"].mean(),
        "Humidity (%)": df["Humidity (%)"].mean()
    }, inplace=True)

    # ✅ Save the cleaned dataset to a NEW file (overwrite if exists)
    df.to_csv(OUTPUT_FILE, index=False)

    print(f"✅ Data wrangling complete! Cleaned file saved at: {OUTPUT_FILE}")

if __name__ == "__main__":
    wrangle_data()
