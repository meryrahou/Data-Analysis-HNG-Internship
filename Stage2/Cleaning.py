import pandas as pd

df = pd.read_csv('./Stage2/Lagos_weather_dataset.csv')

columns_to_keep_and_rename = {
    'datetime': 'Date', 
    'precip': 'Precipitation', 
    'precipprob': 'Precipitation probability', 
    'precipcover': 'Precipitation cover', 
    'preciptype': 'Precipitation type', 
    'sealevelpressure': 'Sea level pressure'
    }

# Select only the columns to keep
df_cleaned = df[list(columns_to_keep_and_rename.keys())].rename(columns=columns_to_keep_and_rename)

# Save the cleaned DataFrame to a new CSV file
df_cleaned.to_csv('./Stage2/Dataset.csv', index=False)
