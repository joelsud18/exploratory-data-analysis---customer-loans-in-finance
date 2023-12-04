import pandas as pd
import numpy as np
import plotly.express as px
import missingno as msno
from statsmodels.graphics.gofplots import qqplot
from scipy import stats
from matplotlib import pyplot
import seaborn as sns


class Plotter:

    '''
    This class is used to plot visualisations of the data.
    '''
        
    def histogram(self, DataFrame: pd.DataFrame, column_name: str):
        
        '''
        This method plots a histogram for data within a column in the dataframe.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            column_name (str): The name of the column for which a histogram will be plotted.
        
        Returns:
            plotly.graph_objects.Figure: A histogram plot of the data within 'column_name'.
        '''

        fig = px.histogram(DataFrame, column_name)
        return fig.show()
    
    def skewness_histogram(self, DataFrame: pd.DataFrame, column_name: str):
        
        '''
        This method plots a histogram for data within a column in the dataframe with the skewness identified.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            column_name (str): The name of the column for which a histogram will be plotted.
        
        Returns:
            matplotlib.axes._subplots.AxesSubplot: A histogram plot of the data within 'column_name' with skewness identified.
        '''

        histogram = sns.histplot(DataFrame[column_name],label="Skewness: %.2f"%(DataFrame[column_name].skew()) )
        histogram.legend()
        return histogram

    def missing_matrix(self, DataFrame: pd.DataFrame):

        '''
        This method plots a matrix displaying missing or null data points within the DataFrame.
        
        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.

        Returns:
            matplotlib.axes._subplots.AxesSubplot: A matrix plot showing all the missing or null data points in each column in white.
        '''

        return msno.matrix(DataFrame)
    
    def qqplot(self, DataFrame: pd.DataFrame, column_name: str):

        '''
        This method is used to return a Quantile-Quantile (Q-Q) plot of a column.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            column_name (str): The name of the column which will be plotted.

        Returns:
            matplotlib.pyplot.figure: a Q-Q plot of the column.
        '''

        qq_plot = qqplot(DataFrame[column_name] , scale=1 ,line='q') 
        return pyplot.show()
    
    def facet_grid_histogram(self, DataFrame: pd.DataFrame, column_names: list):

        '''
        This method is used to return a Facet Grid containing Histograms with the distribution drawn for a list of columns.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            column_names (list): A list of names of columns which will be plotted.

        Returns:
            facet_grid (sns.FacetGrid): A facetgrid containing the histogram plots of each of the variables.
        '''

        melted_df = pd.melt(DataFrame, value_vars=column_names) # Melt the dataframe to reshape it.
        facet_grid = sns.FacetGrid(melted_df, col="variable",  col_wrap=3, sharex=False, sharey=False) # Create the facet grid
        facet_grid = facet_grid.map(sns.histplot, "value", kde=True) # Map histogram onto each plot on grid.
        return facet_grid
    
    def facet_grid_box_plot(self, DataFrame: pd.DataFrame, column_names: list):

        '''
        This method is used to return a Facet Grid containing box-plots for a list of columns.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            column_names (list): A list of names of columns which will be plotted.

        Returns:
            facet_grid (sns.FacetGrid): A facetgrid containing the box-plots of each of the variables.
        '''

        melted_df = pd.melt(DataFrame, value_vars=column_names) # Melt the dataframe to reshape it.
        facet_grid = sns.FacetGrid(melted_df, col="variable",  col_wrap=3, sharex=False, sharey=False) # Create the facet grid
        facet_grid = facet_grid.map(sns.boxplot, "value", flierprops=dict(marker='x', markeredgecolor='red')) # Map box-plot onto each plot on grid.
        return facet_grid
    
    def compare_skewness_transformations(self, DataFrame: pd.DataFrame, column_name: str):
        
        '''
        This method is used to return subplots showing histograms in axes[0] and Q-Q subplots in axes[1] to compare the effect of log, box-cox and yoe-johnson transformations on skewness.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            column_name (str): The name of the column within the dataframe to which this method will be applied.

        Returns:
            matplotlib.pyplot.subplots.figure: A plot containing subplots with histograms in axes[0] and Q-Q subplots in axes[1].
        '''

        transformed_df = DataFrame.copy() # Create a copy of the dataframe to perform transformations.

        # Apply transformations and create new column with transformed data
        transformed_df['log_transformed'] = DataFrame[column_name].map(lambda x: np.log(x) if x > 0 else 0) # Log transformation applied to value in column, if value is 0 then no transformation is done and added to new column in dataframe copy.
        if (DataFrame[column_name] <= 0).values.any() == False: # If column contains only positive values.
            transformed_df['box_cox'] = pd.Series(stats.boxcox(DataFrame[column_name])[0]).values # Perform box-cox transformation and add values as new column in dataframe copy.
        transformed_df['yeo-johnson'] = pd.Series(stats.yeojohnson(DataFrame[column_name])[0]).values # Perform yeo-johnson transformation and add values as new column in dataframe copy.

        # Create a figure and subplots:
        if (DataFrame[column_name] <= 0).values.any() == False: # If column contains only positive values.
            fig, axes = pyplot.subplots(nrows=2, ncols=4, figsize=(16, 8)) # Create a 2x4 grid.
        else: 
            fig, axes = pyplot.subplots(nrows=2, ncols=3, figsize=(16, 8)) # Create a 2x3 grid.

        # Set titles of subplots:
        axes[0, 0].set_title('Original Histogram')
        axes[1, 0].set_title('Original Q-Q Plot')
        axes[0, 1].set_title('Log Transformed Histogram')
        axes[1, 1].set_title('Log Transformed Q-Q Plot')
        if (DataFrame[column_name] <= 0).values.any() == False:        
            axes[0, 2].set_title('Box-Cox Transformed Histogram')
            axes[1, 2].set_title('Box-Cox Transformed Q-Q Plot')
            axes[0, 3].set_title('Yeo-Johnson Transformed Histogram')
            axes[1, 3].set_title('Yeo-Johnson Transformed Q-Q Plot')
        else:
            axes[0, 2].set_title('Yeo-Johnson Transformed Histogram')
            axes[1, 2].set_title('Yeo-Johnson Transformed Q-Q Plot')

        # Add Histograms to subplots:
        sns.histplot(DataFrame[column_name], kde=True, ax=axes[0, 0]) # Original Histogram
        axes[0, 0].text(0.5, 0.95, f'Skewness: {DataFrame[column_name].skew():.2f}', ha='center', va='top', transform=axes[0, 0].transAxes) # Add skewness
        sns.histplot(transformed_df['log_transformed'], kde=True, ax=axes[0, 1]) # Log transformed Histogram
        axes[0, 1].text(0.5, 0.95, f'Skewness: {transformed_df["log_transformed"].skew():.2f}', ha='center', va='top', transform=axes[0, 1].transAxes) # Add skewness
        if (DataFrame[column_name] <= 0).values.any() == False: # If column contains only positive values.
            sns.histplot(transformed_df['box_cox'], kde=True, ax=axes[0, 2]) # Box Cox Histogram
            axes[0, 2].text(0.5, 0.95, f'Skewness: {transformed_df["box_cox"].skew():.2f}', ha='center', va='top', transform=axes[0, 2].transAxes) # Add skewness
            sns.histplot(transformed_df['yeo-johnson'], kde=True, ax=axes[0, 3]) # Yeo Johnson Histogram
            axes[0, 3].text(0.5, 0.95, f'Skewness: {transformed_df["yeo-johnson"].skew():.2f}', ha='center', va='top', transform=axes[0, 3].transAxes) # Add skewness
        else: # If column contains non-positive values.
            sns.histplot(transformed_df['yeo-johnson'], kde=True, ax=axes[0, 2]) # Yeo Johnson Histogram
            axes[0, 2].text(0.5, 0.95, f'Skewness: {transformed_df["yeo-johnson"].skew():.2f}', ha='center', va='top', transform=axes[0, 2].transAxes) # Add skewness

        # Add Q-Q plots to subplots:
        stats.probplot(DataFrame[column_name], plot=axes[1, 0]) # Original Q-Q plot
        stats.probplot(transformed_df['log_transformed'], plot=axes[1, 1]) # Log transformed
        if (DataFrame[column_name] <= 0).values.any() == False: # If column contains only positive values.
            stats.probplot(transformed_df['box_cox'], plot=axes[1, 2]) # Box Cox Q-Q plot
            stats.probplot(transformed_df['yeo-johnson'], plot=axes[1, 3]) # Yeo Johnson Q-Q plot
        else: # If column contains non-positive values.
            stats.probplot(transformed_df['yeo-johnson'], plot=axes[1, 2]) # Yeo Johnson Q-Q plot

        pyplot.suptitle(column_name, fontsize='xx-large') # Add large title for entire plot.
        pyplot.tight_layout() # Adjust the padding between and around subplots.
        return pyplot.show()
    
    def before_after_skewness_transformation(self, DataFrame: pd.DataFrame, column_name: str):

        '''
        This method is used to return two subplots showing the before and after effects of a skewness transformation.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            column_name (str): The name of the column within the dataframe to which this method will be applied.

        Returns:
            matplotlib.pyplot.subplots.figure: A plot containing subplots with Q-Q subplots.
        '''

        # Importing original dataframe column data into seperate dataframe
        df_original = pd.read_csv('loan_payments_versions/loan_payments_post_null_imputation.csv')

        fig, axes = pyplot.subplots(nrows=1, ncols=2, figsize=(16, 8)) # Creating 1x2 grid

        # Creating Q-Q Sub-Plots
        stats.probplot(df_original[column_name], plot=axes[0]) # Original
        stats.probplot(DataFrame[column_name], plot=axes[1]) # transformed

        # Adding skewness
        axes[0].text(0.5, 0.95, f'Skewness: {df_original[column_name].skew():.2f}', ha='center', va='top', transform=axes[0].transAxes)
        axes[1].text(0.5, 0.95, f'Skewness: {DataFrame[column_name].skew():.2f}', ha='center', va='top', transform=axes[1].transAxes) 

        # Adding Sub-Plot titles
        axes[0].set_title('Q-Q Plot: Before', fontsize='x-large')
        axes[1].set_title('Q-Q Plot: After', fontsize='x-large')

        pyplot.suptitle(column_name, fontsize='xx-large') # Adding main plot title.
        return pyplot.show()
    
    def box_plot(self, DataFrame: pd.DataFrame, column_name: str):

        '''
        This method is used to create a box-plot of a column.
        
        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            column_name (str): The name of the column within the dataframe to which this method will be applied.

        Returns:
            pyplot.figure: A box-plot of the column data.
        '''

        sns.boxplot(x=column_name, data = DataFrame, flierprops=dict(marker='x', markeredgecolor='red')) # Make outliers marked as 'x' in red.
        return pyplot.show()
    
    def before_after_outlier_removal(self, DataFrame: pd.DataFrame, column_name: str):

        '''
        This method is used to return two subplots showing the before and after effects of a outlier removal transformation.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            column_name (str): The name of the column within the dataframe to which this method will be applied.

        Returns:
            matplotlib.pyplot.subplots.figure: A plot containing subplots with box-plot subplots.
        '''

        # Importing original dataframe column data into seperate dataframe
        df_original = pd.read_csv('loan_payments_versions/loan_payments_post_skewness_correction.csv')

        fig, axes = pyplot.subplots(nrows=2, ncols=2, figsize=(16, 8)) # Creating 2x2 grid

        # Add box-plots:
        sns.boxplot(x=column_name, data = df_original, flierprops=dict(marker='x', markeredgecolor='red'), ax=axes[0, 0]) # Original
        sns.boxplot(x=column_name, data = DataFrame, flierprops=dict(marker='x', markeredgecolor='red'), ax=axes[0, 1]) # Transformed

        # Add histograms:
        sns.histplot(df_original[column_name], ax=axes[1, 0]) # Original
        sns.histplot(DataFrame[column_name], ax=axes[1, 1]) # Transformed

        # Set sub-plot titles:
        axes[0, 0].set_title('Box Plot: Before')
        axes[0, 1].set_title('Box Plot: After')
        axes[1, 0].set_title('Histogram: Before')
        axes[1, 1].set_title('Histogram: After')

        pyplot.suptitle(column_name, fontsize='xx-large') # Adding main plot title.
        pyplot.subplots_adjust(hspace=0.3) # Adjusting space between subplots to avoid overlap.
        return pyplot.show()
    
    def correlation_matrix(self, DataFrame: pd.DataFrame):

        '''
        This method is used to produce a correlation matrix heatmap for a dataframes numeric columns.
        
        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this methdo will be applied.

        Raises:
            ValueError if the column data type is not numeric.

        Returns:
            matplotlib.pyplot.figure: A heatmap showing the correlation between columns.
        '''

        for column in DataFrame.columns: # For each column in the dataframe.
            if DataFrame[column].dtype not in ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']: # If the datatype is not one of the listed numeric types.
                raise ValueError(f"The '{column}' column is not numerical datatype.") # Raise a ValueError.

        corr = DataFrame.corr() # Compute the correlation matrix.

        mask = np.zeros_like(corr, dtype=np.bool_) # Generate a mask for the upper triangle
        mask[np.triu_indices_from(mask)] = True

        cmap = sns.color_palette("viridis", as_cmap=True) # set colour pallette.

        pyplot.figure(figsize=(14, 12)) # Generate plot.

        sns.heatmap(corr, mask=mask, square=True, linewidths=.5, annot=True, cmap=cmap, fmt=".2f") # Generate heatmap.
        pyplot.yticks(rotation=0)
        pyplot.title('Correlation Matrix of all Numerical Variables')
        return pyplot.show()