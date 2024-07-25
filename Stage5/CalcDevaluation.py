import pandas as pd

# Load the data
data = pd.read_csv('./Stage5/USA/MergedData.csv')  
data['Date'] = pd.to_datetime(data['Date'])
data = data.set_index('Date')

# Calculate the percentage change in M1SL
data['M1SL_Change'] = data['M1SL'].pct_change() * 100  # Percentage change in M1SL

# Calculate real currency devaluation
# Here, we'll use the percentage change in M1SL minus the inflation rate
data['Real_Devaluation'] = data['M1SL_Change'] - data['Inflation']

# Save the results to a new CSV file
output_file_path = 'real_currency_devaluation.csv'  # Replace with your desired output file path
data.to_csv(output_file_path)

print("Data with real currency devaluation has been saved to", output_file_path)