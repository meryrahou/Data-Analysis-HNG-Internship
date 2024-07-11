import pandas as pd

# Define file path
file_path = './Stage2/lagos_rain_data_2002_to_2024.csv'

# Load the data from the file, specifying date parsing and format
Historical_data = pd.read_csv(file_path)

# Check if the datetime column exists
if 'Datetime' in Historical_data.columns:
    Historical_data['Datetime'] = pd.to_datetime(Historical_data['Datetime'], format='%d/%m/%Y', errors='coerce')
else:
    print("Error: 'Datetime' column not found in the data")

# Remove rows with NaT in 'Datetime' column
Historical_data = Historical_data.dropna(subset=['Datetime'])

# Set 'Datetime' column as the index
Historical_data.set_index('Datetime', inplace=True)

# Ensure index is monotonic
Historical_data.sort_index(inplace=True)

# Set frequency (D for daily data, adjust as needed)
Historical_data = Historical_data.asfreq('D')

# Debug: Check frequency
print(Historical_data.index.freq)
