import pandas as pd


class DataTransform:

    '''
    This class is used to apply transformations to columns within the data.
    '''

    def extract_integer_from_string(self, DataFrame: pd.DataFrame, column_name: str):

        '''
        This method is used to extract integers that are contained within strings in columns.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            column_name (str): The name of the column to which this method will be applied.

        Returns:
            DataFrame (pd.DataFrame): The updated DataFrame.
        '''

        DataFrame[column_name] = DataFrame[column_name].str.extract('(\d+)').astype('Int32') # The first method extracts any digits from the string in the desired column
        # the second method casts the digits into the 'Int32' data type, this is because this type of integer is a nullable type of integer.
        return DataFrame

    def replace_string_text(self, DataFrame: pd.DataFrame, column_name: str, original_string: str, new_string: str):

        '''
        This method is used to replace strings with an alternative string.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            column_name (str): The name of the column to which this method will be applied.
            original_string (str): the string that will be replaced.
            new_string (str): the string that will replace the original_string.

        Returns:
            DataFrame (pd.DataFrame): the updated DataFrame.
        '''

        DataFrame[column_name] = DataFrame[column_name].str.replace(original_string, new_string)
        return DataFrame

    def convert_string_to_date(self, DataFrame: pd.DataFrame, column_name: str):

        '''
        This method is used to convert a date in string format into a date in period format. The reason for period format is because dates within the loan database only have a resolution of the month and year.

        Parameters:
            column_name (str): The name of the column to which this method will be applied.

        Returns:
            DataFrame (pd.DataFrame): the updated DataFrame.
        '''
            
        DataFrame[column_name] = pd.to_datetime(DataFrame[column_name], errors='coerce').dt.to_period('M') # The first method converts the string in the column to a datetime.
        # The second method converts the datetime to a period (M) which is a date that contains only the month and year since this is the resolution of the data provided.
        return DataFrame