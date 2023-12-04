import pandas as pd


class DataFrameInfo:

    '''
    This class is used to retrieve information from the DataFrame.
    '''

    def describe_dtypes(self, DataFrame: pd.DataFrame, column_name: str = None): # If no column_name argument is provided the method assumes a column_name value of None.
        # This is so the method can be applied to a specific column or the entire DataFrame.
        
        '''
        This method will describes the datatype(s) of a column or DataFrame.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            column_name (str): The name of the column to which this method will be applied (Has a default value of None, in which case the method is applied to the entire DataFrame).
        
        Returns:
            pd.Series: IF column_name is NOT specified, The data type of each column in the DataFrame.
            pd.Series: IF column_name is specified, The data type of the specified column.
        '''
        
        if column_name is not None: # In the case that a column name IS provided.
            if column_name not in DataFrame.columns: # In the case the provided column_name is NOT in the DataFrame.
                raise ValueError(f"Column '{column_name}' not found in the dataframe.") # Raises an error.
            return DataFrame[column_name].dtypes # Applies method to specified column.
        else: # In the case a column name IS NOT provided.
            return DataFrame.dtypes # Applies method to every column in the DataFrame.
    
    def median(self, DataFrame: pd.DataFrame, column_name: str = None): # If no column_name argument is provided the method assumes a column_name value of None.
        # This is so the method can be applied to a specific column or the entire DataFrame.

        '''
        This method will provide the median value of a column or DataFrame.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            column_name (str): The name of the column to which this method will be applied (Has a default value of None, in which case the method is applied to the entire DataFrame).
        
        Returns:
            pd.Series: IF column_name is NOT specified, The median value of each column in the DataFrame.
            pd.Series: IF column_name is specified, The median value of the specified column.
        '''

        if column_name is not None: # In the case that a column name IS provided.
            if column_name not in DataFrame.columns: # In the case the provided column_name is NOT in the DataFrame.
                raise ValueError(f"Column '{column_name}' not found in the dataframe.") # Raises an error.
            return DataFrame[column_name].median(numeric_only=True) # Applies method to specified column.
        else: # In the case a column name IS NOT provided.
            return DataFrame.median(numeric_only=True) # Applies method to every column in the DataFrame.
    
    def standard_deviation(self, DataFrame: pd.DataFrame, column_name: str = None): # If no column_name argument is provided the method assumes a column_name value of None.
        # This is so the method can be applied to a specific column or the entire DataFrame.

        '''
        This method will provide the standard deviation of a column or DataFrame.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            column_name (str): The name of the column to which this method will be applied (Has a default value of None, in which case the method is applied to the entire DataFrame).
        
        Returns:
            pd.Series: IF column_name is NOT specified, The standard deviation of each column in the DataFrame.
            pd.Series: IF column_name is specified, The standard deviation of the specified column.
        '''

        if column_name is not None: # In the case that a column name IS provided.
            if column_name not in DataFrame.columns: # In the case the provided column_name is NOT in the DataFrame.
                raise ValueError(f"Column '{column_name}' not found in the dataframe.") # Raises an error.
            return DataFrame[column_name].std(skipna=True, numeric_only=True) # Applies method to specified column.
        else: # In the case a column name IS NOT provided.
            return DataFrame.std(skipna=True, numeric_only=True) # Applies method to every column in the DataFrame.
        
    def mean(self, DataFrame: pd.DataFrame, column_name: str = None): # If no column_name argument is provided the method assumes a column_name value of None.
        # This is so the method can be applied to a specific column or the entire DataFrame.

        '''
        This method will provide the mean value of a column or DataFrame.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            column_name (str): The name of the column to which this method will be applied (Has a default value of None, in which case the method is applied to the entire DataFrame).
        
        Returns:
            pd.Series: IF column_name is NOT specified, The mean value of each column in the DataFrame.
            pd.Series: IF column_name is specified, The mean value of the specified column.
        '''

        if column_name is not None: # In the case that a column name IS provided.
            if column_name not in DataFrame.columns: # In the case the provided column_name is NOT in the DataFrame.
                raise ValueError(f"Column '{column_name}' not found in the dataframe.") # Raises an error.
            return DataFrame[column_name].mean(skipna=True, numeric_only=True) # Applies method to specified column.
        else: # In the case a column name IS NOT provided.
            return DataFrame.mean(skipna=True, numeric_only=True) # Applies method to every column in the DataFrame.
    
    def count_distinct(self, DataFrame: pd.DataFrame, column_name: str):

        '''
        This method will count the number of unique or distinct values within a specified column.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            column_name (str): The name of the column to which this method will be applied.

        Returns:
            int: The number of unique or distinct values within the column.
        '''

        return len(DataFrame[column_name].unique())

    def shape(self, DataFrame: pd.DataFrame):

        '''
        This method will provide the number of rows and columns within the DataFrame.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.

        Returns:
            tuple: The number of rows and columns within the DataFrame
        '''

        print(f'The DataFrame has {DataFrame.shape[1]} columns and {DataFrame.shape[0]} rows.')
        return DataFrame.shape

    def null_count(self, DataFrame: pd.DataFrame, column_name: str = None): # If no column_name argument is provided the method assumes a column_name value of None.
        # This is so the method can be applied to a specific column or the entire DataFrame.

        '''
        This method will count the number of null values (e.g. NaN) within a column or DataFrame.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            column_name (str): The name of the column to which this method will be applied (Has a default value of None, in which case the method is applied to the entire DataFrame).
        
        Returns:
            pd.Series: IF column_name is NOT specified, The count of null values of each column in the DataFrame.
            pd.Series: IF column_name is specified, The count of null values of the specified column.
        '''

        if column_name is not None: # In the case that a column name IS provided.
            if column_name not in DataFrame.columns: # In the case the provided column_name is NOT in the DataFrame.
                raise ValueError(f"Column '{column_name}' not found in the dataframe.") # Raises an error.
            return DataFrame[column_name].isna().sum() # Applies method to specified column.
        else: # In the case a column name IS NOT provided.
            return DataFrame.isna().sum() # Applies method to every column in the DataFrame.
        
    def null_percentage(self, DataFrame: pd.DataFrame, column_name: str = None): # If no column_name argument is provided the method assumes a column_name value of None.
        # This is so the method can be applied to a specific column or the entire DataFrame.

        '''
        This method will provide the percentage of null values (e.g. NaN) within a column or DataFrame.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            column_name (str): The name of the column to which this method will be applied (Has a default value of None, in which case the method is applied to the entire DataFrame).
        
        Returns:
            pd.Series: IF column_name is NOT specified, The percentage of null values within each column in the DataFrame.
            pd.Series: IF column_name is specified, The percentage of null values within the specified column.
        '''

        if column_name is not None: # In the case that a column name IS provided.
            if column_name not in DataFrame.columns: # In the case the provided column_name is NOT in the DataFrame.
                raise ValueError(f"Column '{column_name}' not found in the dataframe.") # Raises an error.
            percentage = (DataFrame[column_name].isna().sum())/(len(DataFrame[column_name]))*100 # Divides the number of nulls by the total number of values in the column, then multiplies by 100.
            # Applies method to specified column.
            return percentage
        else: # In the case a column name IS NOT provided.
            percentage = (DataFrame.isna().sum())/(len(DataFrame))*100  # Divides the number of nulls by the total number of values in each column, then multiplies by 100.
            # Applies method to every column in the DataFrame.
            return percentage
        
    def get_null_columns(self, DataFrame: pd.DataFrame, print: bool = False):

        '''
        This method is used to retrieve a list of columns that contain null values as well as print the percentage of null values for each of those columns.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            print (bool): IF True then these columns are printed with their respective percentages.
        
        Returns:
            columns_with_null (list): List of column names that contain null values.
        '''

        columns_with_null = list(DataFrame.columns[list(DataFrameInfo.null_count(self, DataFrame=DataFrame)>0)]) # Creating a list of columns that contain null values.
        if print == True:
            for col in columns_with_null:
                print(f'{col}: {round(DataFrameInfo.null_percentage(self, DataFrame=DataFrame, column_name=col),1)} %') # For each column in the list print the column name and the percentage of null values.
        return columns_with_null
    
    def identify_conditional_null_columns(self, DataFrame: pd.DataFrame, comparison_operator: str, null_percentage_condition: int):
        
        '''
        This method is used to produce a list of column names that contain null values based on conditions on the proportion of null values.
        TO_NOTE: only columns that contain null values will be considered in this method.
        
        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            comparison_operator (str): either '>' or '<', this is the condition that will be used to specify the proportion of null values to be included.

            null_percentage_condition (int): the percentage of null values present in each column that will be used in the condition.

        Returns:
            columns (list): a list of the columns that meet the criteria in terms of percentage of null values.
        '''
        
        columns = [] # Create empty list.
        for col in DataFrame.columns: # For each column in the dataframe
            if '>' in comparison_operator and '<' not in comparison_operator: # If greater than condition specified.
                if DataFrameInfo.null_percentage(self, DataFrame=DataFrame, column_name=col) > null_percentage_condition: # If percentage of nulls in column is greater than specified integer.
                    columns.append(col) # Add column to list.
            elif '<' in comparison_operator and '>' not in comparison_operator: # If less than condition specified.
                if DataFrameInfo.null_percentage(self, DataFrame=DataFrame, column_name=col) < null_percentage_condition and DataFrameInfo.null_percentage(self, DataFrame=DataFrame, column_name=col) > 0: # If percentage of nulls in column is less than specified integer but greater than 0.
                        columns.append(col) # Add column to list.
            else:
                raise ValueError(f"'{comparison_operator}' is not a comparison operator please input either '>' or '<'.") # Otherwise raise ValueError requesting valid conditional operator.
        return columns
    
    def get_numeric_columns(self, DataFrame: pd.DataFrame):

        '''
        This method is used to obtain a list of all numeric columns in a dataframe.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.

        Returns:
            _numeric_columns (list): A list containing the names of all the numeric columns in the dataframe.
        '''

        numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64'] # List of numeric datatypes in string format.
        numeric_columns = [] # Empty list.
        for column in DataFrame.columns: # For each column in the dataframe.
            if DataFrame[column].dtypes in numerics: # If the columns datatype is numeric.
                numeric_columns.append(column) # Add column to list.
        return numeric_columns

    def get_skewed_columns(self, DataFrame: pd.DataFrame, threshold: int):
        
        '''
        This method is used to obtain a list of all columns that meet skewness threshold criteria.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            threshold (int): The absolute value of the skewness threshold.

        Returns:
            skewed_numeric_columns (list): A list containing the names of all the columns that exceed the skewness threshold.
        '''

        numerics_columns = DataFrameInfo.get_numeric_columns(self, DataFrame) # Call 'DataFrameInfo.get_numeric_columns()' method to get list of numeric columns.
        skewed_columns = [] # Empty list.
        for column in numerics_columns: # For each numeric column in the dataframe.
            if abs(DataFrame[column].skew()) >= threshold: # If the absolute value of the skewness of column is greater than or equal to the threshold.
                skewed_columns.append(column) # Add column to list.
        return skewed_columns
    
    def get_skewness(self, DataFrame: pd.DataFrame, column_names: list):
        
        '''
        This method is used to obtain a dictionary of skewness' for a list of columns.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            column_names (list): A list of columns for which the skewness will be computed.

        Returns:
            skewness (dict): A dictionary containing the column as a key with its skewness as a value.
        '''

        skewness = {} # Empty dictionary. 
        for column in column_names: # For each column in list of columns.
            print(f'{column}: {round(DataFrame[column].skew(),2)}') # Print column name and skewness rounded to 2 d.p.
            skewness[column] = DataFrame[column].skew() # Add column and its skewness to dictionary.
        return skewness
