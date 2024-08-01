import pandas as pd
from sqlalchemy import create_engine

# Database connection details
db_config = {
    'user': 'mery',
    'password': 'yessir',
    'host': 'localhost',
    'database': 'da_mery'
}

# Create a connection using SQLAlchemy
engine = create_engine(f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}")

file_path = '/Users/mery/GitHub/Data-Analysis-HNG-Internship/Stage5B/Data/parts.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame for inspection
print("Original DataFrame:")
print(df.head())

# Select relevant columns and rename them
df = df[['Part#', 'PartName', 'Quantity', 'UnitPrice']]
df.rename(columns={
    'Part#': 'Part_Number',
    'PartName': 'Part_Name',
    'UnitPrice': 'Unit_Price'
}, inplace=True)

# Display the DataFrame after selecting and renaming columns
print("Edited DataFrame:")
print(df.head())

# Insert data into the Parts table
try:
    df.to_sql('Parts', con=engine, if_exists='append', index=False)
    print("Data inserted into Parts table successfully")
except Exception as e:
    print(f"An error occurred while inserting data: {e}")
