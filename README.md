# 🌦️ Descriptive Analysis of Weather Patterns

**Project by:** Akshat Tripathi (Roll: 04914202023)

## 📌 Project Overview
This project performs a comprehensive descriptive analysis of historical weather data to identify climate trends, seasonal variations, and extreme weather events. Using Python, Pandas, and Seaborn, the system processes raw meteorological data to generate actionable insights for regional planning.

---

## 🛠️ Tech Stack
- **Language:** Python
- **Data Manipulation:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Input Data:** CSV format (Time-series weather data)

---

## 📊 Key Analyses Performed

### 1. Data Preprocessing
- Date normalization and time-zone handling.
- Missing value imputation using forward-fill methods.
- Extraction of Month/Year features for time-series aggregation.

### 2. Statistical Analysis
- **Descriptive Statistics:** Calculation of Mean, Median, and Standard Deviation for Temperature, Humidity, and Pressure.
- **Correlation Analysis:** Heatmap generation to understand relationships between weather variables.

### 3. Visualization Modules
- **Monthly/Yearly Trends:** Line graphs tracking temperature changes over time.
- **Seasonal Variations:** Box plots showing temperature distribution across months.
- **Precipitation Analysis:** Bar charts displaying frequency of rain/snow events.
- **Correlation Matrix:** Heatmap visualizing variable dependencies.

### 4. Extreme Event Detection
- Identification of **Heatwaves** (Top 5% temperature).
- Identification of **Low-Pressure Systems** (Bottom 5% pressure).

---

## 📂 Project Structure
```text
weather-analysis/
│
├── analysis.py          # Main Python script
├── weather_data.csv     # Dataset (Input)
├── requirements.txt     # Dependencies
└── README.md            # Project Documentation

🚀 How to Run
1. Install Dependencies: 
pip install -r requirements.txt

2. Run the Analysis:
python analysis.py

3.View Results:

The script will print statistical summaries to the console.
5 interactive visualization windows will pop up showing the trends.


📉 Visualizations
The script generates the following charts:

1. Monthly Average Temperature Trend (Line Plot)
2. Yearly Average Temperature Trend (Line Plot)
3. Seasonal Temperature Variations (Box Plot)
4. Precipitation Type Frequency (Bar Chart)
5. Correlation Matrix of Weather Parameters (Heatmap)

📋 Summary of Findings
1. Overall trends in Temperature, Humidity, and Pressure analyzed.
2. Monthly and yearly variations identified.
3. Frequency of precipitation types and rainy days per month calculated.
4. Correlations between weather parameters assessed.
5. Extreme temperature and low-pressure events detected for climate risk assessment.


