# Exploratory Data Analysis: Customer Loans in Finance
By **Joel Sud**
## Table of Contents:
- [Description](#description)
- [Installation Instructions](#installation_instructions)
- [Usage Instructions](#usage_instructions)
- [File Structure](#file_structure)
    - [File Description](#understanding-the-files)


## Description: 
This is an Ai Core project with the aim of conducting Exploratory Data Analysis (EDA) on tabular customer loan payments data. This involves extracting the data from an AWS Relational Database and writing it to a pandas dataframe and a csv file ready for processing and analysis. 

This data is then transformed to impute and remove nulls, optimise skewness, remove outliers and identify correlation. Analysis and visualisation is then performed on this data to gain insights on the current state of loans, current and potential losses as well as identifying indicators of risk.

## Installation_Instructions:
1. **Download and clone repository:**
- copy the repository URL by clicking '*<> Code*' above the list of files in GitHub Repo. Then copy and paste the '*HTTPS*' URL:
- in your CLI go to the location where you wish to clone your directory.
- Type the following '***git clone***' command with the '*HTTPS*' URL:

***<p style="text-align: center;">git clone https://github.com/joelsud18/exploratory-data-analysis---customer-loans-in-finance.git***</p>

- Press 'Enter'.

2. **Ensure there is the '*environment.yaml*' file.** This will be used to clone the conda environment with all the packages and versions needed to run the code in this repository. Using conda on the CLI on your machine write the following command:

***<p style="text-align: center;">conda env create -f environment.yml***
</p>
    
- you can add the ***--name*** flag to give a name to this environment.

## Usage_Instructions
1. First ensure the appropriate conda environment is set up.
2. Run the '*db_utils.py*' file to extract the data from an AWS Relational Database and write it into the appropriate csv file. This requires the .yaml credentials for the AWS RDS.
    - Since this is confidential, **SKIP THIS STEP**, This file has already been run and the csv file has been included within this repository, as '*loan_payments.csv*'.
3. Open and run the '*EDA.ipynb*' notebook. This contains the exploratory data analysis where the data is transformed to remove and impute nulls, optimise skewness, remove outliers and identify correlation.
    - Read through this notebook to understand the EDA process.
4. The '*skewness_transformations_visualisation.ipynb*' and '*outlier_removal_visualisation.ipynb*' notebooks **can** be run to be updated and to see in more detail the transformations that were done on every column at these steps.
5. The '*analysis_and_visualisation.ipynb*' notebook should then be run. This provides insights, conclusions and visualisations from the transformed data. Analysis on the current state of loans, current and potential losses as well as identifying risk indicating variables are provided in this notebook.
## File_Structure:
- EDA
    - loan_payments_versions
        - loan_payments.csv *[Raw Data]*
        - loan_payments_post_null_imputation.csv
        - loan_payments_post_skewness_correction.csv
        - loan_payments_post_outlier_removal.csv
        - loan_payments_transformed.csv
    - environment.yaml
    - EDA.ipynb
    - analysis_and_visualisation.ipynb
    - db_utils.py
    - datatransform.py
    - dataframeinfo.py
    - dataframetransform.py
    - plotter.py
    - loan_payments.csv
    - skewness_transformations_visualisation.ipynb
    - outlier_removal_visualisation.ipynb
    - README.md

#### Understanding the Files:
- **EDA.ipynb**: This is the notebook in which the exploratory data analysis is conducted, this should be run and read to understand the EDA and dataframe transformation process.
- **analysis_and_visualisation.ipynb**: This is the notebook that contains analysis and visualisations of the transformed dataframe. This interactive notebook contains insights on and conclusions from the data.
- **loan_payments_versions**: This is a folder that contains versions of the 'loan_payments' data at different stages of the EDA process in .csv format.
- **environment.yaml**: This is a .yaml file containing the conda environment configuration. This should be imported during installation so that all the necessary modules, libraries and versions to run this repository are set up.
- **db_utils.py**: This is a python script that extracts the data from an AWS RDS using .yaml credentials that are not provided due to confidentiality. This file has already been run and the subsequent .csv file ('*loan_payments.csv*') has been included in this repository.
- **datatransform.py**: This is a python script which defines the DataTransform() class which is used to transform the format of the dataframe. This is imported as a module into the '*EDA.ipynb*' notebook.
- **dataframeinfo.py**: This is a python script that defines the DataFrameInfo() class which is used to retrive information and insights from the dataframe. This is imported as a module into the '*EDA.ipynb*' notebook.
- **dataframetransform.py**: This is a python script which defines the DataFrameTransformation() class which is used to conduct transformations on the dataframe. This is imported as a module into the '*EDA.ipynb*' notebook.
- **plotter.py**: This is a python script that defines the Plotter() class, this class is used to provide visualisations on the dataframe. This is imported as a module into the '*EDA.ipynb*' notebook.
- **skewness_transformations_visualisation.ipynb**: This is a notebook which contains more detail on the skewness corrections than shown in the '*EDA.ipynb*'. It shows every transformation done on columns.
- **outlier_removal_visualisation.ipynb**: This is a notebook which contains more detail on the outlier removal than shown in the '*EDA.ipynb*'. It shows every transformation done on columns.