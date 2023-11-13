# Exploratory Data Analysis: Customer Loans in Finance

## Description: 
This is an Ai Core project with the aim of conducting Exploratory Data Analysis (EDA) on tabular customer loan payments data. This involves extracting the data from an AWS Relational Database and writing it to a pandas dataframe and a csv file ready for processing and analysis.

## File Structure:
Within the repository is:
- 'data_extraction.py': This should be run to define the 'RDSDatabaseConnector' class which establishes a connection to the database by creating a SQLAlchemy engine then writing this to a csv file ('loan_payments.csv').