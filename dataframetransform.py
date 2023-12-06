import numpy as np
import pandas as pd
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import RobustScaler
from sklearn.svm import SVC
# Auxiliary classes:
from dataframeinfo import DataFrameInfo as info
from plotter import Plotter as plotter


np.random.seed(123) # To ensure reproducibility, the random seed is set to '123'.

class DataFrameTransform:

    '''
    This class is used to apply transformations to the dataframe in regards to imputing or removing columns with missing data.
    '''

    def remove_null_columns(self, DataFrame: pd.DataFrame, column_name):

        '''
        This method is used to remove column(s) containing excess null or missing values.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            Column_name: the name(s) of columns that will be removed.

        Returns:
            DataFrame (pd.DataFrame): The updated dataframe.
        '''

        DataFrame.drop(column_name, axis=1, inplace=True)
        return DataFrame

    def remove_null_rows(self, DataFrame: pd.DataFrame, column_name):

        '''
        This method is used to remove rows within the dataframe where data points from a specified column are null.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            column_name: The name of the column which will be checked for null values, these rows will be removed.

        Returns:
            DataFrame (pd.DataFrame): The updated dataframe.
        '''
        DataFrame.dropna(subset=column_name, inplace=True)
        return DataFrame
    
    def fill_median(self, DataFrame: pd.DataFrame, column_name):
        
        '''
        This method is used to fill null values in a column with the median value.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            column_name: The name of the column which will be filled with the median value for nulls.

        Returns:
            DataFrame (pd.DataFrame): The updated dataframe.
        '''

        DataFrame[column_name].fillna(DataFrame[column_name].median(numeric_only=True), inplace=True)
        return DataFrame
    
    def fill_mean(self, DataFrame: pd.DataFrame, column_name):
    
        '''
        This method is used to fill null values in a column with the mean value.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            column_name: The name of the column which will be filled with the mean value for nulls.

        Returns:
            DataFrame (pd.DataFrame): The updated dataframe.
        '''

        DataFrame[column_name].fillna(DataFrame[column_name].mean(numeric_only=True, skipna=True), inplace=True)
        return DataFrame
    
    def linear_regression_fill(self, DataFrame: pd.DataFrame, column_to_fill: str, training_features: list = None, score: bool = False, check_distribution: bool = False):
        
        '''
        This method is used to impute null values in a numerical column based on a linear regression model that ignores other null columns.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            column_to_fill (str): The name of the column which will have null values imputed.
            training_features (list): list of columns to use as training features in the model (the default uses all non-null columns).
            score (bool): a boolean value that indicates whether the model accuracy score should be computed.
            check_distribution (bool): a boolean value that determines whether the histogram distribution of the data in the target column from before and after this method should be printed.

        Returns:
            DataFrame (pd.DataFrame): The updated dataframe.
        '''

        if check_distribution == True:
            print(f'\n({column_to_fill}) Initial Distribution:\n')
            plotter.histogram(self, DataFrame, column_to_fill) # Plots histogram to display distribution before method is applied.

        if training_features == None: # In the case no training features are provided.
            x = DataFrame.drop(info.get_null_columns(self, DataFrame), axis=1) # Only uses columns with no nulls for training.
        else:  # In the case training features are provided.
            x = DataFrame[training_features] # Using provided list for training.
        y = DataFrame[column_to_fill] # Identify target column.

        # Encode string columns to numeric type to be compatible with model.
        object_columns = x.select_dtypes(include=['object']).columns.tolist() # Adds all columns with 'object' as their data type into a list.
        x[object_columns] = x[object_columns].astype('category') # Changes the data type of the columns in this list to 'category'.
        x[object_columns] = x[object_columns].apply(lambda x: x.cat.codes) # Converts these categories into numerical codes.

        # Encode date columns to numeric type to be compatible with model.
        date_columns = x.select_dtypes(include=['period[M]']).columns.tolist() # Adds all columns with 'period [M]' as their data type into a list.
        x[date_columns] = x[date_columns].astype('category') # Changes the data type of the columns in this list to 'category'.
        x[date_columns] = x[date_columns].apply(lambda x: x.cat.codes) # Converts these categories into numerical codes.

        # Data Split
        x_train = x[~y.isna()] # Training input data: all columns except target column where target column values are known (not null).
        y_train = y[~y.isna()] # Training output data: all non null (known) values in target column.

        x_test = x[y.isna()] # Testing input data: all columns except target column where target column values are not known (null).
        # This will be input into the model to impute null values.

        # Train Linear Regression Model:
        model = LinearRegression()
        model.fit(x_train, y_train)

        # Run model and impute null values with predicted values:
        prediction = model.predict(x_test)
        DataFrame[column_to_fill].loc[y.isna()] = prediction # Where values in target column are null, impute the model's predicted value.
        
        if check_distribution == True:
            print(f'\n({column_to_fill}) Final Distribution:\n')
            plotter.histogram(self, DataFrame, column_to_fill) # Plots histogram to display distribution after method is applied.

        if score == True:
            print(f'\nScore: {round(model.score(x_train, y_train),2)}') # Provides an accuracy score for the model (based on the training data) which is rounded to 2 d.p.

        return DataFrame

    def support_vector_machine_fill(self, DataFrame: pd.DataFrame, column_to_fill: str, training_features: list = None, score: bool = False, check_distribution: bool = False):
        
        '''
        This method is used to impute null values in a categorical column based on a support vector machine (SVM) model that ignores other null columns.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            column_to_fill (str): The name of the column which will have null values imputed.
            training_features (list): list of columns to use as training features in the model (the default uses all non-null columns).
            score (bool): a boolean value that indicates whether the model accuracy score should be computed.
            check_distribution (bool): a boolean value that determines whether the normalised value count of the data in the target column from before and after this method should be printed.

        Returns:
            DataFrame (pd.DataFrame): The updated dataframe.
        '''

        if check_distribution == True:
            initial_distribution = DataFrame[column_to_fill].value_counts(normalize=True) # Stores the normalized value count (distribution of data) into a variable.

        if training_features == None: # In the case no training features are provided.
            x = DataFrame.drop(info.get_null_columns(self, DataFrame), axis=1) # Only uses columns with no nulls for training.
        else: # In the case training features are provided.
            x = DataFrame[training_features] # Using provided list for training.
        y = DataFrame[column_to_fill]  # Identify target column.

        # Encode string columns to numeric type to be compatible with model.
        object_columns = x.select_dtypes(include=['object']).columns.tolist() # Adds all columns with 'object' as their data type into a list.
        x[object_columns] = x[object_columns].astype('category') # Changes the data type of the columns in this list to 'category'.
        x[object_columns] = x[object_columns].apply(lambda x: x.cat.codes) # Converts these categories into numerical codes.

        # Encode date columns to numeric type to be compatible with model.
        date_columns = x.select_dtypes(include=['period[M]']).columns.tolist() # Adds all columns with 'period [M]' as their data type into a list.
        x[date_columns] = x[date_columns].astype('category') # Changes the data type of the columns in this list to 'category'.
        x[date_columns] = x[date_columns].apply(lambda x: x.cat.codes) # Converts these categories into numerical codes.

        # Scaling data for run time optimisation.
        scaler = RobustScaler()
        transformer = scaler.fit(x)
        transformer.transform(x)

        # Data Split:
        sample_size = (DataFrame[column_to_fill].isna().sum()) * 4 # To keep a 80:20 split between training data and testing data size,
        # the sample of training data is set to 4 times the size of testing (missing) data.
        if sample_size < 10000:
            sample_size = 10000 # If the training sample is less than 10,000, then it is set to 10,000 for accurate training.
        x_train = x[~y.isna()].sample(sample_size, random_state=123)# Training input data: all columns except target column where target column values are known (not null).
        # A random sample of at least 10,000 of these training data points are selected to optimise run time.
        # The random state parameter ensures every time this method is run it uses the exact same sample, for reproducibility.
        y_train = y[x.index.isin(x_train.index)] # Training output data: all non null (known) values in target column that correspond to x_train sample.

        x_test = x[y.isna()] # Testing input data: all columns except target column where target column values are not known (null).
        # This will be input into the model to impute null values.

        # Train SVM model
        model = SVC()
        model.fit(x_train, y_train)

        # Run model and impute null values with predicted values:
        prediction = model.predict(x_test)
        DataFrame[column_to_fill].loc[y.isna()] = prediction # Where values in target column are null, impute the model's predicted value.

        if check_distribution == True:
            final_distribution = DataFrame[column_to_fill].value_counts(normalize=True) # Stores the normalized value count (distribution of data) after method into a variable.
            distribution_df = pd.DataFrame({'Before': round(initial_distribution, 3),'After': round(final_distribution, 3)}) # combines both the before and after normalised value counts into a dataframe, rounded to 3 d.p.
            print('Distribution: Normalised Value Count')
            print(distribution_df)
        
        if score == True:
            print(f'\nScore: {round(model.score(x_train, y_train),2)}') # Provides an accuracy score for the model (based on the training data) which is rounded to 2 d.p.
        
        return DataFrame
    
    def box_cox_transform(self, DataFrame: pd.DataFrame, column_name: str):

        '''
        This method is used to apply Box-Cox transformation to normalise a column.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            column_name (str): The name of the column which will be transformed.

        Returns:
            boxcox_column (pd.Series): The transformed column.
        '''

        boxcox_column = stats.boxcox(DataFrame[column_name])
        boxcox_column = pd.Series(boxcox_column[0])
        return boxcox_column

    def yeo_johnson_transform(self, DataFrame: pd.DataFrame, column_name: str):

        '''
        This method is used to apply Yeo-Johnson transformation to normalise a column.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            column_name (str): The name of the column which will be transformed.

        Returns:
            yeojohnson_column (pd.Series): The transformed column.
        '''

        yeojohnson_column = stats.yeojohnson(DataFrame[column_name])
        yeojohnson_column = pd.Series(yeojohnson_column[0])
        return yeojohnson_column

    def drop_outlier_rows(self, DataFrame: pd.DataFrame, column_name: str, z_score_threshold: int):

        '''
        This method is used to remove rows based on the 'z score' of values in a specified column.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            column_name(str) : The name of the column which will be transformed.
            z_score_threshold (int)

        Returns:
            DataFrame (pd.DataFrame): The transformed dataframe.
        '''

        mean = np.mean(DataFrame[column_name]) # Identify the mean of the column.
        std = np.std(DataFrame[column_name]) # Identify the standard deviation of the column.
        z_scores = (DataFrame[column_name] - mean) / std # Identofy the 'z score' for each value in the column.
        abs_z_scores = pd.Series(abs(z_scores)) # Create a series with the absolute values of the 'z_score' stored.
        mask = abs_z_scores < z_score_threshold
        DataFrame = DataFrame[mask] # Only keep rows where the 'z score' is below the threshold.        
        return DataFrame