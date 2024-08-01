import pandas as pd
from sqlalchemy import create_engine

# Database connection details
db_config = {
    'user': 'mery',
    'password': 'yessir',
    'host': 'localhost',
    'database': 'DA_mery'
}

# Create a connection using SQLAlchemy
engine = create_engine(f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}")

# Load CSV into a DataFrame
customer_df = pd.read_csv('/Users/mery/GitHub/Data-Analysis-HNG-Internship/Stage5B/Data/customer.csv')

# Insert data into the Customer table
customer_df.to_sql('Customer', con=engine, if_exists='append', index=False)

