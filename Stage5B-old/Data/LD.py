import pandas as pd
from sqlalchemy import create_engine
import os

# Database connection details
db_config = {
    'user': 'mery',
    'password': 'yessir',
    'host': 'localhost',
    'database': 'DA_mery'
}

# Create a connection using SQLAlchemy
engine = create_engine(f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}")

# Path to the directory containing CSV files
csv_directory = '/Users/mery/GitHub/Data-Analysis-HNG-Internship/Stage5B/Data'

# Dictionary of table names based on CSV filenames
table_names = {
    'customer.csv': 'Customer',
    'vehicle.csv': 'Vehicle',
    'invoice.csv': 'Invoice',
    'job.csv': 'Job',
    'part.csv': 'Part'
}

# Loop through each CSV file and load it into the corresponding table
for csv_file, table_name in table_names.items():
    file_path = os.path.join(csv_directory, csv_file)
    print(f"Processing {file_path} into {table_name} table...")
    
    # Load CSV into a DataFrame
    df = pd.read_csv(file_path)
    
    # Insert data into the corresponding table
    df.to_sql(table_name, con=engine, if_exists='append', index=False)
    print(f"Data imported into {table_name} table.")

print("All files have been processed.")
