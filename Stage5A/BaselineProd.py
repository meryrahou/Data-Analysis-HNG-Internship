import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = './Stage5/USA/MergedData.csv'
data = pd.read_csv(file_path)

# Ensure 'Date' column is in datetime format
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

# Drop any rows with NaN values (if 'Date' conversion fails or other columns have NaNs)
data.dropna(inplace=True)

# Calculate Productivity
data['Productivity'] = data['SharePrice'] / (data['Inflation'] * data['M1SL'])

# Define the period of stability (adjust as needed)
baseline_period = data[data['Date'] < '2015-01-01']

# Calculate baseline productivity (mean or median)
baseline_productivity = baseline_period['Productivity'].mean()
print(f'\n\nBaseline Productivity: {baseline_productivity}')


