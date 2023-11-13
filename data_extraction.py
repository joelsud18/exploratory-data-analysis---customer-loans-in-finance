import yaml
from sqlalchemy import create_engine, text
import sqlalchemy
import pandas as pd

# Extract the credentials from the yaml file into a dictionary.
def extract_credentials():
    with open('credentials.yaml', 'r') as file:
        return yaml.safe_load(file)

# Store the dictionary into a variable.
credentials = extract_credentials()

# Creates class object to connect to RDS database and extract data.
class RDSDatabaseConnector():
    def __init__(self, credentials_dict):
        self.credentials_dict = credentials_dict # when class is initiated it requires the credentials argument.

    # Initialises SQLAlchemy engine.
    def create_engine(self):
        self.engine = create_engine(f"postgresql+psycopg2://{self.credentials_dict['RDS_USER']}:{self.credentials_dict['RDS_PASSWORD']}@{self.credentials_dict['RDS_HOST']}:{self.credentials_dict['RDS_PORT']}/{self.credentials_dict['RDS_DATABASE']}")

    # Establishes a connection to the database and creates a pandas dataframe from the 'loan payments' table.
    def extract_loans_data(self):
        with self.engine.connect() as connection:
            self.loan_payments = pd.read_sql_table('loan_payments', self.engine)
            return self.loan_payments
    
    # Writes the pandas dataframe into a csv file.
    def save_data_to_csv(self):
        with open('loans_payments.csv', 'w') as file:
            self.loan_payments.to_csv(file, encoding= 'utf-8', index= False)

# Instantiates the 'RDSDatabaseConnector' class and calls all the methods to create the engine, extract the
# into a pandas dataframe and then loads it into a csv file.
connector = RDSDatabaseConnector(credentials)
connector.create_engine()
connector.extract_loans_data()
connector.save_data_to_csv()