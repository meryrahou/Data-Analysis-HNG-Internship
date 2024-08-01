import pandas as pd

# Load the data from a CSV file
file_path = './Stage5/USA/USA_M1.csv'
df = pd.read_csv(file_path)

# Convert 'Date' to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Prepare an empty list to hold the expanded data
expanded_data = []

# Iterate through each row and generate daily data
for index, row in df.iterrows():
    date = row['Date']
    inflation = row['M1SL']
    
    # Create a date range for the entire month
    start_date = date.replace(day=1)
    end_date = (start_date + pd.DateOffset(months=1)) - pd.DateOffset(days=1)
    
    # Create a date range from start_date to end_date
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')
    
    # Append the daily data to the list
    for day in date_range:
        expanded_data.append({
            'Date': day,
            'Inflation': inflation
        })

# Convert the list to a DataFrame
expanded_df = pd.DataFrame(expanded_data)

# Optionally, save the expanded data to a new CSV file
expanded_df.to_csv('expanded_data.csv', index=False)

print(expanded_df)
