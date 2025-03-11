# Bird-Migration-and-Climate-Change-A-Data-Science-Experimentation
This project investigates the relationship between bird migration patterns and climate change using real-time data from eBird API and OpenWeather API. The project collects data on bird sightings, merges it with weather data, and performs exploratory analysis and machine learning modeling to study patterns.

# Bird Migration and Climate Change: A Data Science Experimentation  

This project investigates the relationship between **bird migration patterns** and **climate change** using real-time data from the **eBird API** and **OpenWeather API**. The project collects **bird sighting data**, merges it with corresponding weather conditions, and applies **exploratory data analysis (EDA)** and **visualization techniques** to study patterns.

## Project Workflow  
1. **Data Collection** (`super_pull.py`)  
   - Fetches bird migration data from the **eBird API** (last 30 days).  
   - Fetches corresponding weather data (temperature, humidity, and weather conditions) from **OpenWeather API**.  
   - Merges and stores the data into `super_dataset_csv.csv`.  

2. **Data Wrangling** (`data_wrangling.py`)  
   - Cleans and structures raw data.  
   - Removes missing values and standardizes columns.  
   - Outputs a processed dataset for further analysis.  

3. **Data Preprocessing** (`data_preprocessing.py`)  
   - Encodes categorical variables.  
   - Handles outliers and normalizes numerical values.  
   - Prepares data for visualization and machine learning.  

4. **Data Profiling** (`data_profiling.py`)  
   - Generates an **automated profiling report** for exploratory data analysis.  
   - Provides insights into missing values, distributions, and correlations.  

5. **Data Visualization** (`data_visualization.py`)  
   - Creates interactive **heatmaps**, **scatter plots**, and **bar charts**.  
   - Shows the relationship between **temperature, humidity, and bird migration**.  

## Technologies Used  
- **Python**  
- **pandas**, **NumPy** (Data Manipulation)  
- **Matplotlib**, **Seaborn**, **Plotly** (Visualization)  
- **YData Profiling** (Automated Data Insights)  
- **eBird API**, **OpenWeather API** (Data Collection)  


