import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# File path
FILE_PATH = r"C:\Data Science\wrangled_data.csv"

def load_data():
    """Load and clean the dataset."""
    df = pd.read_csv(FILE_PATH)

    # Ensure correct column names
    df.columns = df.columns.str.strip()  # Remove extra spaces
    
    # Drop unnamed empty columns
    df = df.loc[:, ~df.columns.str.contains('Unnamed')]
    
    return df

def plot_temperature_chart(df):
    """Plot a temperature trend over time."""
    plt.figure(figsize=(12, 6))
    df["Date"] = pd.to_datetime(df["Date"])  # Convert to datetime
    df = df.sort_values("Date")  # Ensure it's in time order

    plt.plot(df["Date"], df["Temperature (°C)"], marker='o', linestyle='-', color='b', label="Temperature (°C)")
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Temperature (°C)", fontsize=12)
    plt.title("Temperature Trend Over Time", fontsize=14)
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_bird_species_count(df):
    """Plot the count of bird species."""
    plt.figure(figsize=(12, 6))
    species_count = df["Species"].value_counts()

    sns.barplot(y=species_count.index[:10], x=species_count.values[:10], palette="viridis")
    plt.xlabel("Count", fontsize=12)
    plt.ylabel("Bird Species", fontsize=12)
    plt.title("Top 10 Most Sighted Bird Species", fontsize=14)
    plt.show()

def plot_heatmaps(df):
    """Generate meaningful heatmaps for data insights."""
    numeric_cols = df.select_dtypes(include=["number"])  # Select numeric data

    # 🔥 1️⃣ Standard Correlation Heatmap (Only if enough numeric data exists)
    if len(numeric_cols.columns) > 1:  
        plt.figure(figsize=(10, 6))
        sns.heatmap(numeric_cols.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
        plt.title("Correlation Heatmap of Numeric Features", fontsize=16)
        plt.show()
    else:
        print("⚠️ Not enough numeric features for correlation heatmap.")

    # 🔥 2️⃣ Heatmap for Weather Conditions vs. Temperature & Humidity
    if "Weather" in df.columns and "Temperature (°C)" in df.columns and "Humidity (%)" in df.columns:
        plt.figure(figsize=(12, 6))
        pivot_table = df.pivot_table(index="Weather", values=["Temperature (°C)", "Humidity (%)"], aggfunc="mean")
        sns.heatmap(pivot_table, annot=True, cmap="coolwarm", linewidths=0.5)
        plt.title("Weather vs. Avg Temperature & Humidity", fontsize=16)
        plt.xlabel("Metric", fontsize=14)
        plt.ylabel("Weather Condition", fontsize=14)
        plt.show()
    else:
        print("⚠️ Missing required columns for Weather vs. Temperature/Humidity heatmap.")

if __name__ == "__main__":
    df = load_data()
    plot_temperature_chart(df)  # 📊 Improved Temperature Chart
    plot_bird_species_count(df)  # 📊 Clearer Bird Species Count
    plot_heatmaps(df)  # 🔥 Better Heatmaps
