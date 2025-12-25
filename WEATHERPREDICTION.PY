# Descriptive Analysis of Weather Patterns
# For Climate Trend Identification
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# -------------------------------
# 1. Load Data
# -------------------------------
file_path = r"C:\Users\aksha\Downloads\weather_data.csv"
data = pd.read_csv(file_path)

# -------------------------------
# 2. Data Preprocessing
# -------------------------------
data['Date'] = pd.to_datetime(data['Date'], errors='coerce', utc=True)
data = data.dropna(subset=['Date'])
data = data.ffill()
data['Date'] = data['Date'].dt.tz_localize(None)
data['Month'] = data['Date'].dt.month
data['Year'] = data['Date'].dt.year

# -------------------------------
# Function to Add Name Annotation
# -------------------------------
def add_name_annotation():
    plt.text(0.95, 0.01, "Akshat Tripathi Roll 04914202023",
             verticalalignment='bottom', horizontalalignment='right',
             transform=plt.gca().transAxes,
             color='gray', fontsize=10, alpha=0.7)

# -------------------------------
# 3. Descriptive Statistics
# -------------------------------
print("=== Overall Descriptive Statistics ===")
desc_stats = data[['Temperature','Humidity','Pressure']].describe()
print(desc_stats)

median_values = data[['Temperature','Humidity','Pressure']].median()
print("\nMedian Values:")
print(median_values)

# -------------------------------
# 4. Monthly Aggregation & Plot
# -------------------------------
monthly_stats = data.groupby('Month')[['Temperature','Humidity','Pressure']].agg(['mean','median','std','min','max'])
print("\n=== Monthly Aggregated Statistics ===")
print(monthly_stats)

monthly_avg_temp = data.groupby('Month')['Temperature'].mean()
plt.figure(figsize=(10,6))
sns.lineplot(x=monthly_avg_temp.index, y=monthly_avg_temp.values, marker='o', color='red')
plt.title('Monthly Average Temperature Trend')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.grid(True)
add_name_annotation()
plt.show()

# -------------------------------
# 5. Yearly Aggregation & Plot
# -------------------------------
yearly_stats = data.groupby('Year')[['Temperature','Humidity','Pressure']].agg(['mean','median','std','min','max'])
print("\n=== Yearly Aggregated Statistics ===")
print(yearly_stats)

yearly_avg_temp = data.groupby('Year')['Temperature'].mean()
plt.figure(figsize=(10,6))
sns.lineplot(x=yearly_avg_temp.index, y=yearly_avg_temp.values, marker='o', color='orange')
plt.title('Yearly Average Temperature Trend')
plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.grid(True)
add_name_annotation()
plt.show()

# -------------------------------
# 6. Seasonal Temperature Variation
# -------------------------------
plt.figure(figsize=(10,6))
sns.boxplot(x='Month', y='Temperature', data=data)
plt.title('Seasonal Temperature Variations')
add_name_annotation()
plt.show()

# -------------------------------
# 7. Precipitation Analysis
# -------------------------------
precip_counts = data['PrecipType'].value_counts()
print("\n=== Precipitation Frequency ===")
print(precip_counts)

monthly_precip = data.groupby(['Year','Month'])['PrecipType'].apply(lambda x: (x != 'None').sum())
print("\n=== Monthly Precipitation Days ===")
print(monthly_precip)

plt.figure(figsize=(8,5))
sns.barplot(x=precip_counts.index, y=precip_counts.values, palette='Blues_d')
plt.title('Precipitation Type Frequency')
plt.ylabel('Number of Days')
plt.xlabel('Precipitation Type')
add_name_annotation()
plt.show()

# -------------------------------
# 8. Correlation Analysis & Heatmap
# -------------------------------
correlation_matrix = data[['Temperature','Humidity','Pressure']].corr()
print("\n=== Correlation Matrix ===")
print(correlation_matrix)

plt.figure(figsize=(6,4))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix of Weather Parameters")
add_name_annotation()
plt.show()

# -------------------------------
# 9. Extreme Events
# -------------------------------
extreme_temp = data[data['Temperature'] > data['Temperature'].quantile(0.95)]
print("\n=== Extreme Temperature Events (Top 5%) ===")
print(extreme_temp[['Date','Temperature','DailySummary']])

extreme_pressure = data[data['Pressure'] < data['Pressure'].quantile(0.05)]
print("\n=== Extreme Low Pressure Events (Top 5%) ===")
print(extreme_pressure[['Date','Pressure','DailySummary']])

# -------------------------------
# 10. Summary
# -------------------------------
print("\n=== Summary for Regional Planning ===")
print("1. Overall trends in Temperature, Humidity, and Pressure analyzed.")
print("2. Monthly and yearly variations identified.")
print("3. Frequency of precipitation types and rainy days per month calculated.")
print("4. Correlations between weather parameters assessed.")
print("5. Extreme temperature and low-pressure events detected for climate risk assessment.")
