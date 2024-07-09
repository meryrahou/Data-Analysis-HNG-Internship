import pandas as pd

# Load Data
df = pd.read_csv('./Stage2/Dataset.csv')
print(df.head())

# Define the threshold for a flood (example: 50mm of precipitation)
flood_threshold = 30

# Add a column 'Flood' to indicate if a flood occurred
df['Flood'] = df['Precipitation'].apply(lambda x: 1 if x > flood_threshold else 0)

# Check the number of floods detected
floods_detected = df['Flood'].sum()
print(f"Number of floods detected with {flood_threshold}mm threshold: {floods_detected}")

# Save the updated dataset
df.to_csv('./Stage2/Updated.csv', index=False)
