import pandas as pd

# File paths
FILE_PATH = r"C:\Data Science\super_dataset_csv.csv"
WRANGLED_FILE_PATH = r"C:\Data Science\wrangled_data.csv"

def wrangle_data():
    """Perform data cleaning and save to a new CSV file."""
    
    # Load dataset with proper encoding
    df = pd.read_csv(FILE_PATH, encoding="latin1")

    # 🔥 Print column names before renaming
    print("📌 Columns before renaming:", df.columns.tolist())

    # Rename columns correctly
    df.rename(columns=lambda x: x.strip(), inplace=True)  # Remove hidden spaces
    df.rename(columns={"Temperature": "Temperature (°C)", "Humidity": "Humidity (%)"}, inplace=True)

    # 🔥 Print column names after renaming
    print("✅ Columns after renaming:", df.columns.tolist())

    # Drop unnecessary columns
    drop_cols = ["Latitude", "Longitude"]
    df.drop(columns=drop_cols, inplace=True, errors='ignore')

    # Convert 'Date' to datetime format
    df["Date"] = pd.to_datetime(df["Date"], errors='coerce')

    # Handle missing values safely
    df.fillna({
        "Species": "Unknown",
        "Weather": "Unknown",
        "Temperature (°C)": df["Temperature (°C)"].mean(),
        "Humidity (%)": df["Humidity (%)"].mean()
    }, inplace=True)

    # ✅ Save cleaned dataset to a new file (overwrite if exists)
    df.to_csv(WRANGLED_FILE_PATH, index=False)

    print(f"✅ Data wrangling complete! Cleaned file saved at: {WRANGLED_FILE_PATH}")

if __name__ == "__main__":
    wrangle_data()
