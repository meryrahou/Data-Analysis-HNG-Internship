import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
import os

# Define file paths
file_path = './Stage2/lagos_rain_data_2002_to_2024.csv'
visuals_path = './Stage2/Visual'

# Create directory for visuals if it doesn't exist
os.makedirs(visuals_path, exist_ok=True)

# Load the data from the file
Historical_data = pd.read_csv(file_path)

# Ensure the 'Datetime' column is converted to datetime type
if 'Datetime' in Historical_data.columns:
    Historical_data['Datetime'] = pd.to_datetime(Historical_data['Datetime'], format='%d/%m/%Y', errors='coerce')
else:
    print("Error: 'Datetime' column not found in the data")

# Debug: Print first few rows to ensure datetime conversion
print(Historical_data.head())

# Remove rows with NaT in 'Datetime' column
Historical_data = Historical_data.dropna(subset=['Datetime'])

# Debug: Check for NaT values
print(Historical_data['Datetime'].isna().sum())

# Check for duplicate dates
duplicate_dates = Historical_data[Historical_data.duplicated(subset=['Datetime'], keep=False)]
print("Duplicate dates:")
print(duplicate_dates)

# If duplicates exist, drop them and keep the first occurrence
if not duplicate_dates.empty:
    Historical_data = Historical_data.drop_duplicates(subset=['Datetime'], keep='first')

# Set 'Datetime' column as the index
Historical_data.set_index('Datetime', inplace=True)

# Ensure index is monotonic
Historical_data.sort_index(inplace=True)

# Debug: Check the index type and first few index values
print(Historical_data.index)
print(Historical_data.index.is_monotonic_increasing)

# Set frequency (D for daily data, adjust as needed)
Historical_data = Historical_data.asfreq('D')

# Fill missing values using forward fill
Historical_data.fillna(method='ffill', inplace=True)

# Debug: Check frequency and filled values
print(Historical_data.index.freq)
print(Historical_data.head())

# Create 'Flood' column based on precipitation threshold
threshold = 30  # Precipitation threshold in mm
Historical_data['Flood'] = (Historical_data['Precip'] > threshold).astype(int)

# Debug: Print first few rows to ensure 'Flood' column is created
print(Historical_data.head())

# Fit ARIMA model
model = ARIMA(Historical_data['Precip'], order=(5, 1, 0))  # Example order, adjust as needed
model_fit = model.fit()

# Debug: Print summary of the model
print(model_fit.summary())

# Forecast future precipitation
forecast_steps = 365  # Number of future days to predict
forecast = model_fit.forecast(steps=forecast_steps)

# Debug: Print forecasted values
print(forecast)

# Handle last_date as a datetime object
last_date = Historical_data.index[-1]  # Using the last datetime from the index

# Create future dates
future_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=forecast_steps)

# Create a DataFrame for the forecast
future_data = pd.DataFrame({'Datetime': future_dates, 'Precipitation_forecast': forecast})
future_data.set_index('Datetime', inplace=True)

# Print future data
print(future_data.head())

# Add flood prediction based on the forecasted precipitation
future_data['Flood_forecast'] = (future_data['Precipitation_forecast'] > threshold).astype(int)

# Print future data with flood forecast
print(future_data.head())

# Plot historical precipitation and forecasted precipitation
plt.figure(figsize=(12, 6))
plt.plot(Historical_data.index, Historical_data['Precip'], label='Historical Precipitation')
plt.plot(future_data.index, future_data['Precipitation_forecast'], label='Forecasted Precipitation', linestyle='--')
plt.xlabel('Date')
plt.ylabel('Precipitation (mm)')
plt.title('Historical and Forecasted Precipitation')
plt.legend()
plt.savefig(os.path.join(visuals_path, 'precipitation_forecast.png'))
plt.show()

# Plot historical flood occurrences and forecasted flood predictions
plt.figure(figsize=(12, 6))
plt.plot(Historical_data.index, Historical_data['Flood'], label='Historical Floods', linestyle='', marker='o')
plt.plot(future_data.index, future_data['Flood_forecast'], label='Forecasted Floods', linestyle='', marker='x')
plt.xlabel('Date')
plt.ylabel('Flood Indicator')
plt.title('Historical and Forecasted Floods')
plt.legend()
plt.savefig(os.path.join(visuals_path, 'flood_forecast.png'))
plt.show()

# Combine historical and forecasted data
combined_data = pd.concat([Historical_data, future_data], sort=False)
combined_data.reset_index(inplace=True)

# Save combined data to CSV
combined_data.to_csv(os.path.join(visuals_path, 'combined_historical_forecast_data.csv'), index=False)

# Print combined data
print(combined_data.tail())

# Step 1: Define your threshold (adjust as needed)
threshold = 22  # Example threshold (in mm)

# Step 2: Create a flood indicator based on the threshold
future_data['Flood_forecast'] = (future_data['Precipitation_forecast'] > threshold).astype(int)

# Step 3: Check for flood days and identify the exact flood day
flood_days = future_data.loc[future_data['Flood_forecast'] == 1]
if not flood_days.empty:
    exact_flood_day = flood_days.index[0]
    print(f"Exact flood day predicted: {exact_flood_day}")
else:
    print("No flood days predicted in the forecast period.")
