import pandas as pd

# Define the file paths
file1_path = './Stage5/USA/USA_M1.csv'
file2_path = './Stage5/USA/USA_InflationData.csv'
file3_path = './Stage5/USA/USDNGN.csv'
file4_path = './Stage5/USA/Wilshire.csv'
file5_path = './Stage5/USA/HistoricalPrices.csv'

# Read the CSV files
df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)
df3 = pd.read_csv(file3_path)
df4 = pd.read_csv(file4_path)
df5 = pd.read_csv(file5_path)

# Merge the DataFrames on the Date column using outer join
merged_df = df1.merge(df2, on='Date', how='outer')
merged_df = merged_df.merge(df3, on='Date', how='outer')
merged_df = merged_df.merge(df4, on='Date', how='outer')
merged_df = merged_df.merge(df5, on='Date', how='outer')

# Trim any leading or trailing spaces from column names
merged_df.columns = merged_df.columns.str.strip()

# Print the cleaned header of merged_df
print("Cleaned columns in merged_df:", merged_df.columns.tolist())

# Define the correct column names to keep
columns_to_keep = ['Date', 'Inflation', 'M1SL', 'SharePrice', 'Ccc']

# Check if all columns_to_keep are in merged_df
missing_cols = [col for col in columns_to_keep if col not in merged_df.columns]
if missing_cols:
    raise ValueError(f"The following columns are missing in the DataFrame: {missing_cols}")

# Keep only the specified columns
merged_df = merged_df[columns_to_keep]

# Convert 'Date' column to datetime to ensure proper sorting
merged_df['Date'] = pd.to_datetime(merged_df['Date'])

# Sort the DataFrame by the 'Date' column
merged_df = merged_df.sort_values(by='Date')

# Save the merged and sorted DataFrame to a CSV file
output_file_path = './Stage5/USA/MergedData.csv'
merged_df.to_csv(output_file_path, index=False)

print(f"Merged and sorted file saved to: {output_file_path}")
