import pandas as pd

# Load Data
df = pd.read_csv('./Stage2/Dataset.csv')
print(df.head())

# Define initial threshold
initial_threshold = 50

# Analyze flood occurrence with the initial threshold
df['Flood'] = df['Precipitation'].apply(lambda x: 1 if x > initial_threshold else 0)

# Check the number of floods detected with the initial threshold
floods_detected = df['Flood'].sum()
print(f"Number of floods detected with {initial_threshold}mm threshold: {floods_detected}")

# Test different thresholds
thresholds = [40, 50, 30, 20]
for threshold in thresholds:
    df['Flood'] = df['Precipitation'].apply(lambda x: 1 if x > threshold else 0)
    floods_detected = df['Flood'].sum()
    print(f"{floods_detected} flood detected with {threshold}mm threshold")
