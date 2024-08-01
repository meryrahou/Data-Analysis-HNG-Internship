import pandas as pd
from sqlalchemy import create_engine

db_config = {
    'user': 'mery',
    'password': 'yessir',
    'host': 'localhost',
    'database': 'da_mery'
}

# Create a connection using SQLAlchemy
engine = create_engine(f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}")

file_path = '/Users/mery/GitHub/Data-Analysis-HNG-Internship/Stage5B/Data/vehicle.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame for inspection
print("Original DataFrame:")
print(df.head())

# Drop the 'Owner' column
df.drop(columns=['OwnerName'], inplace=True)

# Rename columns to match the Vehicle table schema
df.rename(columns={
    'Reg#': 'Registration_Number'
}, inplace=True)

# Display the DataFrame after renaming columns
print("Edited DataFrame:")
print(df.head())

# Insert data into the Vehicle table
try:
    df.to_sql('Vehicle', con=engine, if_exists='append', index=False)
    print("Data inserted into Vehicle table successfully")
except Exception as e:
    print(f"An error occurred while inserting data: {e}")
