import requests
import pandas as pd
import os
from datetime import datetime, timedelta

# API Keys (Replace with actual keys)
EBIRD_API_KEY = "5m1p0bvck5uk"  # Replace with your eBird API key
WEATHER_API_KEY = "47ca69a0b05533cbc2a79d1321ec212e"  # Replace with your OpenWeather API key

# API URLs
EBIRD_BASE_URL = "https://api.ebird.org/v2/data/obs"
WEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Super dataset filename
SUPER_DATASET = "super_dataset_csv.csv"

# **Regions to Fetch Data From**
REGIONS = {
    "India": ["IN-TN", "IN-KA", "IN-MH", "IN-DL"],
    "USA": ["US-CA", "US-TX", "US-NY", "US-FL"],
    "Africa": ["ZA-GT", "KE-30", "NG-LA", "EG-C"],
    "South America": ["BR-SP", "AR-B", "CO-DC", "PE-LI"]
}

# Function to get bird migration data
def get_bird_migration(region):
    """Fetches bird observations from eBird API for a given region (last 30 days)."""
    url = f"{EBIRD_BASE_URL}/{region}/recent"
    headers = {"X-eBirdApiToken": EBIRD_API_KEY}
    params = {"back": 30}  # Max allowed days

    for attempt in range(3):
        print(f"🔍 Requesting: {url} (Attempt {attempt + 1})")

        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"⚠️ Error {response.status_code}: {response.json()}")

    print(f"⚠️ No bird data found for {region}. Skipping...")
    return []

# Function to get weather data
def get_weather(lat, lon):
    """Fetches weather data for a given latitude and longitude."""
    params = {"lat": lat, "lon": lon, "appid": WEATHER_API_KEY, "units": "metric"}
    response = requests.get(WEATHER_BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        return {
            "Weather": data["weather"][0]["description"],
            "Temperature (°C)": data["main"]["temp"],
            "Humidity (%)": data["main"]["humidity"],
        }
    else:
        return {"Weather": "N/A", "Temperature (°C)": "N/A", "Humidity (%)": "N/A"}

# Function to save data
def save_data(data):
    """Saves data to a CSV file, avoiding duplicates."""
    df_new = pd.DataFrame(data)

    if os.path.exists(SUPER_DATASET):
        df_existing = pd.read_csv(SUPER_DATASET)
        df_combined = pd.concat([df_existing, df_new]).drop_duplicates().reset_index(drop=True)
    else:
        df_combined = df_new

    df_combined.to_csv(SUPER_DATASET, index=False)
    print(f"✅ {len(df_new)} new records added to {SUPER_DATASET}")

# Main function to collect data for all regions
def main():
    print("\n🔹 Collecting Bird Migration Data for Multiple Countries 🔹\n")

    all_data = []
    
    for country, states in REGIONS.items():
        for state in states:
            print(f"📍 Fetching data for {state} ({country})...")

            bird_data = get_bird_migration(state)
            if not bird_data:
                continue  # Skip if no data found

            # Process data
            for bird in bird_data:
                weather_info = get_weather(bird["lat"], bird["lng"])

                all_data.append({
                    "Country": country,
                    "Region": state,
                    "Species": bird["comName"],
                    "Location": bird["locName"],
                    "Date": bird["obsDt"],
                    "Latitude": bird["lat"],
                    "Longitude": bird["lng"],
                    **weather_info,
                })

    # Save to CSV
    if all_data:
        save_data(all_data)
        print("\n✅ Data collection complete!")
    else:
        print("\n⚠️ No new data collected.")

if __name__ == "__main__":
    main()
