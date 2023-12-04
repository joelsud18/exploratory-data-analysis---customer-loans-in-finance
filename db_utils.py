import pandas as pd
from sqlalchemy import create_engine
import yaml


# Extract the credentials from the yaml file into a dictionary.
def extract_credentials():

    '''
    This function is used to extract the credentials from yaml to a dictionary to establish connection with the RDS.

    Returns:
        (dict): the credentials in dictionary format.
    '''

    with open('credentials.yaml', 'r') as file:
        return yaml.safe_load(file)

# Store the dictionary into a variable.
credentials: dict = extract_credentials()

# Creates class object to connect to RDS database and extract data.
class RDSDatabaseConnector():

    '''
    This class is used to establish a connection with the AiCore RDS containing loan payments information.

    Attributes:
        credentials_dict (dict): the dictionary containing the 'Host', 'Password', 'User', 'Database' and 'Port' required for the sqlalchemy to establish a connection with the RDS
    '''

    def __init__(self, credentials_dict: dict):

        '''
        This method is used to initialise this instance of the RDSDatabaseConnector class.

        Attributes:
            credentials_dict (dict): the dictionary containing the 'Host', 'Password', 'User', 'Database' and 'Port' required for the sqlalchemy to establish a connection with the RDS
        '''
        
        self.credentials_dict = credentials_dict # when class is initiated it requires the credentials argument.

    # Initialises SQLAlchemy engine.
    def create_engine(self):
        
        '''
        This method is used to create the SQLAlchemy engine which will be required to connect to the AiCore RDS.
        '''

        self.engine = create_engine(f"postgresql+psycopg2://{self.credentials_dict['RDS_USER']}:{self.credentials_dict['RDS_PASSWORD']}@{self.credentials_dict['RDS_HOST']}:{self.credentials_dict['RDS_PORT']}/{self.credentials_dict['RDS_DATABASE']}")

    # Establishes a connection to the database and creates a pandas dataframe from the 'loan payments' table.
    def extract_loans_data(self):

        '''
        This method is used to establish a connection to the RDS and extract the necessary 'loan_payments' table into a pandas dataframe.

        Returns:
            (pd.DataFrame): a dataframe containing all the data from the 'loan_payments' table in the RDS that will be analysed.
        '''

        with self.engine.connect() as connection:
            self.loan_payments_df = pd.read_sql_table('loan_payments', self.engine)
            return self.loan_payments_df
    
# Writes the pandas dataframe into a csv file.
def save_data_to_csv(loans_df: pd.DataFrame):

    '''
    This function is used to write the 'loan_payments' dataframe into a csv file using a context manager.

    Args:
        loans_df (pd.DataFrame): The 'loan_payments' dataframe that will be written into a csv file..
    '''

    with open('loan_payments.csv', 'w') as file:
        loans_df.to_csv(file, encoding= 'utf-8', index= False)

if __name__ == '__main__':
    connector = RDSDatabaseConnector(credentials) # Instantiates the 'RDSDatabaseConnector' class using the .
    # Calling all defined methods:
    connector.create_engine() # Creates the sqlalchemy engine to establish connection.
    extracted_data_frame: pd.DataFrame = connector.extract_loans_data() # Extracts sql data to a pandas dataframe.
    save_data_to_csv(extracted_data_frame) # Writes the dataframe into a csv file.