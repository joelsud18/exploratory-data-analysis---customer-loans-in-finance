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
    
    def calculate_column_percentage(self, DataFrame: pd.DataFrame, target_column_name: str, total_column_name: str):

        '''
        This method is used to calculate the percentage of one column's sum over another column's sum.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            target_column_name (str): The name of the column for which the percentage will be calculated.
            total_column_name (str): The name of the column for which the percentage will be calculated out of, the total.

        Returns:
            percentage (float): The percentage that the target column's sum occupies out of the total column's sum.
        '''

        target_column_sum = DataFrame[target_column_name].sum() # Sum of values in target column.
        total_column_sum = DataFrame[total_column_name].sum() # Sum of values in total column.

        percentage = (target_column_sum / total_column_sum) * 100 # Calculate of target value over total value.
        return percentage

    def calculate_percentage(self, target, total):

        '''
        This method is used to calculate the percentage of one value over another.

        Parameters:
            target: The value for which the percentage will be calculated.
            total: The value which the percentage will be calculated out of, the total.

        Returns:
            percentage (float): The percentage that the target occupies out of the total.
        '''

        percentage = (target/total)*100
        return percentage
    
    def calculate_total_collections_over_period(self, DataFrame: pd.DataFrame, period: int):
        
        '''
        This method is used to provide a projection on the total collections over a period in months.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            period (int): The number of months the forecast is for.
        
        Returns:
            dict: the total collections, loan amount and loan outstanding over the period.
        '''

        collections_df = DataFrame.copy() # Create copy of the dataframe.

        final_payment_date = collections_df['last_payment_date'].max() # identifies the final payment date.

        def calculate_term_end(row): # Function used to calculate term end according to term length and issue date.
            if row['term'] == '36 months': # In 36 month terms
                return row['issue_date'] + 36 # Term end will be 36 months after issue date.
            elif row['term'] == '60 months': # In 60 month terms
                return row['issue_date'] + 60 # Term end will be 60 months after issue date.

        # Apply the function to create the new 'term_end_date' column
        collections_df['term_end_date'] = collections_df.apply(calculate_term_end, axis=1)

        collections_df['mths_left'] = collections_df['term_end_date'] - final_payment_date # calculate number of months between term end and final payment date.
        collections_df['mths_left'] = collections_df['mths_left'].apply(lambda x: x.n) # Extract integer value from 'mths_left' column.

        collections_df = collections_df[collections_df['mths_left']>0] # filter in only current loans.

        def calculate_collections(row): # Define function to sum collections over projection period.
            if row['mths_left'] >= period: # If months left in term are equal to or greater than projection period.
                return row['instalment'] * period #  projection period * Installments.
            elif row['mths_left'] < period: # If less than projection period months left in term.
                return row['instalment'] * row['mths_left'] # number of months left * installments.

        collections_df['collections_over_period'] = collections_df.apply(calculate_collections, axis=1) # Apply method to each row to get total collections in projected perid.

        collection_sum = collections_df['collections_over_period'].sum()
        total_loan = collections_df['loan_amount'].sum()
        total_loan_left = total_loan - collections_df['total_payment'].sum()

        return {'total_collections': collection_sum, 'total_loan': total_loan, 'total_loan_outstanding': total_loan_left}
    
    def monthly_collection_percentage_projections(self, DataFrame: pd.DataFrame, period: int):

        '''
        This method applies the calculate_total_collections_over_period() method over a range of months and for each month retrieves the percentage of collection out of 1) the total loan amount and 2) the outstanding loan amount.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            period (int): The number of months the forecast is for.
        
        Returns:
            dict: a sictionary containing two lists: 
                1) collections as a percentage of total loan amount for each month in period.
                2) collections as a percentage of outstanding loan amount for each month in period.
        '''

        # Generate empty lists that will contain percentages of collection out of total and outstanding loan.
        percentage_of_loan = []
        percentage_of_outstanding = []

        for month in range(1, (period+1)): # For each month in 1-6.
            projections = DataFrameInfo.calculate_total_collections_over_period(self, DataFrame, period=month) # produce dictionaries containing collection, total loan and outstaniding loan amounts.
            
            total_collections = projections['total_collections'] # Extract total collection amount from dictionary.
            total_loan = projections['total_loan'] # Extract total loan amount from dictionary.
            total_loan_outstanding = projections['total_loan_outstanding'] # Extract total loan amount outstanding from dictionary.
            
            percent_total_loan = DataFrameInfo.calculate_percentage(self, total_collections, total_loan) # Calculate percentage of collections out of total loan.
            percent_outstanding_loan = DataFrameInfo.calculate_percentage(self, total_collections, total_loan_outstanding) # Calculate percentage of collections out of outstanding loan.

            # Add percentages to lists.
            percentage_of_loan.append(percent_total_loan)
            percentage_of_outstanding.append(percent_outstanding_loan)
        
        return {'total_loan_percent': percentage_of_loan, 'outstanding_loan_percent': percentage_of_outstanding}
    
    def count_value_in_column(self, DataFrame: pd.DataFrame, column_name: str, value):

        '''
        This method returns a count of the number of times a value appears in a column.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            column_name (str): The name of the column that will be checked.
            value: The value that will be counted.

        Returns:
            int: The number of times the value appears in the column.
        '''

        return len(DataFrame[DataFrame[column_name]==value]) # Return length of dataframe that only contains specified value.
    
    def revenue_lost_by_month(self, DataFrame: pd.DataFrame):

        '''
        This method is used to return a list with the cumulative revenue lost for each month of the remaining term.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method is applied.
        
        Returns:
            revenue_lost (list): A list which contains the cumulative revenue lost value for each month of the remaining term.
        '''

        df = DataFrame.copy() # Create a copy of dataframe to avoid altering original.

        df['term_completed'] = (df['last_payment_date'] - df['issue_date']) # Calculating how much of each term was completed.
        df['term_completed'] = df['term_completed'].apply(lambda x: x.n) # Converting the row into an integer.

        def calculate_term_remaining(row): # Function used to calculate months remaining in term for each row.
            if row['term'] == '36 months': # In 36 month terms
                return 36 - row['term_completed'] # Term remaining is term length - how much of term was completed.
            elif row['term'] == '60 months': # In 60 month terms
                return 60 - row['term_completed'] # Term remaining is term length - how much of term was completed.

        df['term_left'] = df.apply(calculate_term_remaining, axis=1) # Applying function to calculate term left for each loan.
        
        revenue_lost = [] # Empty list
        cumulative_revenue_lost = 0
        for month in range(1, (df['term_left'].max()+1)): # For each month in the maximum number of months left in any term.
            df = df[df['term_left']>0] # Filter out any terms which have no months left.
            cumulative_revenue_lost += df['instalment'].sum() # Cumulatively sum the total number of monthly instalments.
            revenue_lost.append(cumulative_revenue_lost) # Add this cumulative sum to list of revenue projected to be lost.
            df['term_left'] = df['term_left'] - 1 # Take away one from the number of terms left.
        
        return revenue_lost

    def calculate_total_expected_revenue(self, DataFrame: pd.DataFrame):
        
        '''
        This method is used to calculate the total expected revenue from a dataframe:
        
        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
        
        Returns:
            total_expected_revenue (int): The total expected revenue.
        '''

        def calculate_total_revenue(row): # Function used to calculate total expected revenue for each loan.
            if row['term'] == '36 months': # In 36 month terms
                return 36 * row['instalment'] # Number of instalments * value of instalments = Total expected revenue.
            elif row['term'] == '60 months': # In 60 month terms
                return 60 * row['instalment'] # Number of instalments * value of instalments = Total expected revenue.

        DataFrame['total_revenue'] = DataFrame.apply(calculate_total_revenue, axis=1)
        total_expected_revenue = DataFrame['total_revenue'].sum()

        return total_expected_revenue

