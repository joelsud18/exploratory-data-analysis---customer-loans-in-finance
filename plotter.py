from matplotlib import pyplot
import missingno as msno
import numpy as np
import pandas as pd
import plotly.express as px
from scipy import stats
import seaborn as sns
from statsmodels.graphics.gofplots import qqplot


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

    def bar_chart(self, independant_categories: list, dependant_variables: list, title: str=None, y_label: str=None, x_label: str=None):
        
        '''
        This method is used to generate a bar chart plot of categorical data.

        Parameters:
            independant_categories (list): The names of the categories in a list.
            dependant_variables (list): The respective dependant variables in a list.
            title (str): DEFAULT = None, the title of the plot.
            y_label (str): DEFAULT = None, the label for the y-axis.
            x_label (str): DEFAULT = None, the label for the x-axis.

        Returns:
            matplotlib.pyplot.figure: a bar plot of the data.
        '''
        pyplot.figure(figsize=(16, 8))
        sns.barplot(x=independant_categories, y=dependant_variables) # Generating the bar plot and setting the independant and dependant variables.
        if y_label != None: # If a 'y_label' is provided.
            pyplot.ylabel(y_label)
        if x_label != None: # If a 'x_label' is provided.
            pyplot.xlabel(x_label)
        if title != None: # If a 'title' is provided.
            pyplot.title(title)
        return pyplot.show()

    def pie_chart(self, labels: list, sizes: list, title: str=None):

        '''
        This method is used to generate a bar chart plot of categorical data.

        Parameters:
            labels (list): The names of the categories in a list.
            sizes (list): The respective dependant variables in a list.
            title (str): DEFAULT = None, the title of the plot.

        Returns:
            matplotlib.pyplot.figure: a pie chart plot of the data.
        '''

        pyplot.pie(sizes, labels=labels, colors=['#66b3ff', '#ffff99', '#00FF00'], autopct='%1.1f%%', startangle=180) # Generate pie chart.
        if title != None: # If a title is provided.
            pyplot.title(title)
        pyplot.show()
    
    def two_pie_charts(self, labels_1: list, sizes_1: list, labels_2: list, sizes_2: list, plot_title: str=None, title_1: str=None, title_2: str=None):

        '''
        This method is used to generate a grid with two pie chart subplots.

        Parameters:
            labels_1 (list): The names of the categories in a list for first pie chart.
            sizes_1 (list): The respective dependant variables in a list for first pie chart.
            labels_2 (list): The names of the categories in a list for second pie chart.
            sizes_2 (list): The respective dependant variables in a list for second pie chart
            plot_title (str): DEFAULT = None, the title of the plot.
            title_1 (str): DEFAULT = None, the title of the first sub-plot.
            title_2 (str): DEFAULT = None, the title of the second sub-plot.

        Returns:
            matplotlib.pyplot.subplots.figure: a plot with two pie chart sub-plots of the data.
        '''

        fig, axes = pyplot.subplots(nrows=1, ncols=2, figsize=(16, 8)) # Creating 1x2 grid

        if title_1 != None: # If a title for first plot is provided.
            axes[0].set_title(title_1)
        if title_2 != None: # If a title for second plot is provided.
            axes[1].set_title(title_2)

        axes[0].pie(sizes_1, labels=labels_1, colors=['#66b3ff', '#ffff99', '#00FF00'], autopct='%1.1f%%', startangle=90) # Generate pie chart in first plot
        axes[1].pie(sizes_2, labels=labels_2, colors=['#66b3ff', '#ffff99', '#00FF00'], autopct='%1.1f%%', startangle=90) # Generate pie chart in second plot

        if plot_title != None: # If a title is provided.
            pyplot.suptitle(plot_title, fontsize='xx-large')

        return pyplot.show()

    def two_bar_charts(self, independant_categories_1: list, dependant_variables_1: list, independant_categories_2: list, dependant_variables_2: list, plot_title: str=None, title_1: str=None, title_2: str=None, y_label_1: str=None, x_label_1: str=None, y_label_2: str=None, x_label_2: str=None):
        
        '''
        This method is used to generate a grid with two bar chart subplots.

        Parameters:
            independant_categories_1 (list): The names of the categories in a list, for first subplot.
            dependant_variables_1 (list): The respective dependant variables in a list, for first subplot.
            independant_categories_2 (list): The names of the categories in a list, for second subplot.
            dependant_variables_2 (list): The respective dependant variables in a list, for second subplot.
            plot_title (str): DEFAULT = None, the title of the plot.
            title_1 (str): DEFAULT = None, the title of the first sub-plot.
            title_2 (str): DEFAULT = None, the title of the second sub-plot.
            y_label_1 (str): DEFAULT = None, the label for the y-axis of first subplot.
            x_label_1 (str): DEFAULT = None, the label for the x-axis of first subplot.
            y_label_2 (str): DEFAULT = None, the label for the y-axis of second subplot.
            x_label_2 (str): DEFAULT = None, the label for the x-axis of second subplot.

        Returns:
            matplotlib.pyplot.subplots.figure: a plot with two bar chart sub-plots of the data.
        '''

        fig, axes = pyplot.subplots(nrows=1, ncols=2, figsize=(12, 6)) # Creating 1x2 grid

        if title_1 != None: # If a title for first plot is provided.
            axes[0].set_title(title_1)
        if title_2 != None: # If a title for second plot is provided.
            axes[1].set_title(title_2)

        sns.barplot(x=independant_categories_1, y=dependant_variables_1, ax=axes[0]) # Generating the bar plot and setting the independant and dependant variables for first plot.
        sns.barplot(x=independant_categories_2, y=dependant_variables_2, ax=axes[1]) # Generating the bar plot and setting the independant and dependant variables for second plot.

        if y_label_1 != None: # If a 'y_label_1' is provided.
            axes[0].set_ylabel(y_label_1)
        if x_label_1 != None: # If a 'x_label_1' is provided.
            axes[0].set_xlabel(x_label_1)

        if y_label_2 != None: # If a 'y_label_2' is provided.
            axes[1].set_ylabel(y_label_2)
        if x_label_2 != None: # If a 'x_label_2' is provided.
            axes[1].set_xlabel(x_label_2)

        if plot_title != None: # If a title is provided.
            pyplot.suptitle(plot_title, fontsize='xx-large')

        return pyplot.show()
    
    def discrete_population_distribution(self, DataFrame: pd.DataFrame, column_name: str, title: str=None, y_label: str=None, x_label: str=None):

        '''
        This method is used to produce a discrete population distribution bar plot for a column in a dataframe.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            column_name (str): The name of the column in the dataframe to which this method will be applied.
            title (str): DEFAULT = None, the title of the plot.
            y_label (str): DEFAULT = None, the label for the y-axis.
            x_label (str): DEFAULT = None, the label for the x-axis.
        
        Returns:
            matplotlib.pyplot.figure: a bar plot showing the probability distribution of discrete values in a population.
        '''

        probabilities = DataFrame[column_name].value_counts(normalize=True) # Calculate value counts and convert to probabilities

        pyplot.figure(figsize=(16, 8)) # Create figure size.
        pyplot.rc("axes.spines", top=False, right=False) # Remove top and right spine
        sns.barplot(y=probabilities.index, x=probabilities.values, color='b') # Create bar plot

        if y_label != None: # If a 'y_label' is provided.
            pyplot.ylabel(y_label)
        if x_label != None: # If a 'x_label' is provided.
            pyplot.xlabel(x_label)
        if title != None: # If a 'title' is provided.
            pyplot.title(title)
        return pyplot.show()

    def scatter_plot(self, DataFrame: pd.DataFrame, x_variable: str, y_variable: str, title: str=None):

        '''
        This method is used to produce a scatter plot to show the relationship between two variables in a dataframe.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            x_variable (str): The name of the column in the dataframe that will be the x-axis variable.
            y_variable (str): The name of the column in the dataframe that will be the y-axis variable.
            title (str): DEFAULT = None, the title of the plot.
        
        Returns:
            matplotlib.pyplot.figure: a scatter plot showing the relationship between two variables.
        '''

        pyplot.figure(figsize=(16, 8)) # Create figure size.
        sns.scatterplot(data=DataFrame, x=x_variable, y=y_variable) # Generate scatter plot between two variables

        if title != None: # If a 'title' is provided.
            pyplot.title(title)
        return pyplot.show()
    
    def pair_plot(self, DataFrame: pd.DataFrame):

        '''
        This method is used to return a pairplot showing scatter subplots of all pairs of variables in a dataframe.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
        
        Returns:
            sns.pairplot: a pairplot of the dataframe.
        '''

        return sns.pairplot(DataFrame)

    def column_pie_chart(self, DataFrame: pd.DataFrame, column_name: str, title: str=None, y_label: str=None, x_label: str=None):

        '''
        This method is used to produce a pie chart for a column in a dataframe.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            column_name (str): The name of the column in the dataframe to which this method will be applied.
            title (str): DEFAULT = None, the title of the plot.
            y_label (str): DEFAULT = None, the label for the y-axis.
            x_label (str): DEFAULT = None, the label for the x-axis.
        
        Returns:
            matplotlib.pyplot.figure: a pie chart showing proportions of discrete values in a population.
        '''

        probabilities = DataFrame[column_name].value_counts(normalize=True) # Calculate value counts and convert to probabilities

        pyplot.figure(figsize=(16, 8)) # Create figure size.
        pyplot.pie(list(probabilities.values), labels=list(probabilities.index), colors=['#66b3ff', '#ffff99', '#00FF00'], autopct='%1.1f%%', startangle=180) # Generate pie chart.

        if y_label != None: # If a 'y_label' is provided.
            pyplot.ylabel(y_label)
        if x_label != None: # If a 'x_label' is provided.
            pyplot.xlabel(x_label)
        if title != None: # If a 'title' is provided.
            pyplot.title(title)
        return pyplot.show()

    def discrete_value_risk_comparison(self, DataFrame: pd.DataFrame, column_name: str):

        '''
        This method is used to return a plot containing 2 rows of subplots, the first row contains pie charts, the second row contains bar plots. 
        This is to show the probability of discrete values in the dataframe, as well as subsets of the dataframe: Fully Paid Loans, Charged Off and Defaulted Loans, as well as, Risky Loans.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            column_name (str): The name of the column in the dataframe to which this method will be applied.
        
        Returns:
            matplotlib.pyplot.subplots.figure: a grid containing pie chart and bar plot subplots.
        '''

        # Defining DataFrames that contain subsets of loan status.
        df = DataFrame # All loans
        paid_df = df[df['loan_status'] == 'Fully Paid'] # Fully Paid Loans
        charged_default_df = df[df['loan_status'].isin(['Charged Off','Default'])] # Charged off or defaulted loans
        risky_df = df[df['loan_status'].isin(['Late (31-120 days)','In Grace Period', 'Late (16-30 days)'])] # Risky Loans

        # Getting proportions of discrete values in column, only selecting the top 8.
        probabilities = DataFrame[column_name].value_counts(normalize=True).head(8)
        paid_probabilities = paid_df[column_name].value_counts(normalize=True).head(8)
        charged_default_probabilities = charged_default_df[column_name].value_counts(normalize=True).head(8)
        risky_probabilities = risky_df[column_name].value_counts(normalize=True).head(8)

        # Generate main plot
        fig, axes = pyplot.subplots(nrows=2, ncols=4, figsize=(16, 8)) # Creating 2x4 grid

        # Set titles
        axes[0, 0].set_title('All Loans')
        axes[0, 1].set_title('Fully Paid Loans')
        axes[0, 2].set_title('Charged off and Default Loans')
        axes[0, 3].set_title('Risky Loans')

        colour_palette = ['#a6cee3', '#fdbf6f', '#b2df8a', '#fb9a99', '#cab2d6', '#ffff99', '#1f78b4']

        # Generate subplot pie charts
        axes[0, 0].pie(list(probabilities.values), labels=list(probabilities.index), colors=colour_palette, autopct='%1.1f%%', startangle=90) # Generate all loans pie chart in first plot
        axes[0, 1].pie(list(paid_probabilities.values), labels=list(paid_probabilities.index), colors=colour_palette, autopct='%1.1f%%', startangle=90) # Generate fully paid pie chart in second plot
        axes[0, 2].pie(list(charged_default_probabilities.values), labels=list(charged_default_probabilities.index), colors=colour_palette, autopct='%1.1f%%', startangle=90) # Generate charged off and defaulted pie chart in third plot
        axes[0, 3].pie(list(risky_probabilities.values), labels=list(risky_probabilities.index), colors=colour_palette, autopct='%1.1f%%', startangle=90) # Generate pie chart in fourth plot

        # Remove top and right spine for bottom plots
        axes[1, 0].spines["top"].set_visible(False)
        axes[1, 0].spines["right"].set_visible(False)
        axes[1, 1].spines["top"].set_visible(False)
        axes[1, 1].spines["right"].set_visible(False)
        axes[1, 2].spines["top"].set_visible(False)
        axes[1, 2].spines["right"].set_visible(False)
        axes[1, 3].spines["top"].set_visible(False)
        axes[1, 3].spines["right"].set_visible(False)

        # Generate bar plots
        sns.barplot(y=probabilities.index, x=probabilities.values, color='#a6cee3', ax=axes[1,0]) # Generate subplot for all loans
        sns.barplot(y=paid_probabilities.index, x=paid_probabilities.values, color='#a6cee3', ax=axes[1,1]) # Generate subplot for fully paid loans
        sns.barplot(y=charged_default_probabilities.index, x=charged_default_probabilities.values, color='#a6cee3', ax=axes[1,2]) # Generate subplot for charged off and defaulted loans
        sns.barplot(y=risky_probabilities.index, x=risky_probabilities.values, color='#a6cee3', ax=axes[1,3]) # Generate subplot for risky loans

        pyplot.suptitle(column_name, fontsize='xx-large') # Overall Plot title
        pyplot.tight_layout()

        return pyplot.show()

    def continuous_value_risk_comparison(self, DataFrame: pd.DataFrame, column_name: str, z_score_threshold: float=3):

        '''
        This method is used to return a plot containing 2 rows of subplots, the first row contains histograms, the second row contains violin plots. 
        This is to show the distribution and averages of continuous values in the dataframe, as well as subsets of the dataframe: Fully Paid Loans, Charged Off and Defaulted Loans, as well as, Risky Loans.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            column_name (str): The name of the column in the dataframe to which this method will be applied.
            z_score_threshold (float): DEFAULT = 3, The threshold in terms of z_score for filtering outliers out of the data.
        
        Returns:
            matplotlib.pyplot.subplots.figure: a grid containing histogram and violin subplots.
        '''
        
        def drop_outliers(Data_Frame: pd.DataFrame, column_name: str, z_score_threshold: float):
            mean = np.mean(Data_Frame[column_name]) # Identify the mean of the column.
            std = np.std(Data_Frame[column_name]) # Identify the standard deviation of the column.
            z_scores = (Data_Frame[column_name] - mean) / std # Identofy the 'z score' for each value in the column.
            abs_z_scores = pd.Series(abs(z_scores)) # Create a series with the absolute values of the 'z_score' stored.
            mask = abs_z_scores < z_score_threshold
            Data_Frame = Data_Frame[mask] # Only keep rows where the 'z score' is below the threshold.        
            return Data_Frame

        # Defining DataFrames that contain subsets of loan status.
        df = drop_outliers(DataFrame, column_name, z_score_threshold) # All loans excluding outliers
        paid_df = df[df['loan_status'] == 'Fully Paid'] # Fully Paid Loans
        charged_default_df = df[df['loan_status'].isin(['Charged Off','Default'])] # Charged off or defaulted loans
        risky_df = df[df['loan_status'].isin(['Late (31-120 days)','In Grace Period', 'Late (16-30 days)'])] # Risky Loans

        # Generate main plot
        fig, axes = pyplot.subplots(nrows=2, ncols=4, figsize=(20, 10)) # Creating 2x4 grid

        # Set titles
        axes[0, 0].set_title(f'All Loans\nMean: {round(df[column_name].mean(),1)}')
        axes[0, 1].set_title(f'Fully Paid Loans\nMean: {round(paid_df[column_name].mean(),1)}')
        axes[0, 2].set_title(f'Charged off and Default Loans\nMean: {round(charged_default_df[column_name].mean(),1)}')
        axes[0, 3].set_title(f'Risky Loans\nMean: {round(risky_df[column_name].mean(),1)}')

        colour_palette = ['#a6cee3', '#fdbf6f', '#b2df8a', '#fb9a99', '#cab2d6', '#ffff99', '#1f78b4']

        # Generating subplot histograms
        sns.histplot(data=df, x=column_name, kde=True, color='#a6cee3', ax=axes[0, 0])
        sns.histplot(data=paid_df, x=column_name, kde=True, color='#a6cee3', ax=axes[0, 1])
        sns.histplot(data=charged_default_df, x=column_name, kde=True, color='#a6cee3', ax=axes[0, 2])
        sns.histplot(data=risky_df, x=column_name, kde=True, color='#a6cee3', ax=axes[0, 3])
        
        # Acdding vertical mean lines
        axes[0, 0].axvline(df[column_name].mean(), color='blue', linestyle='dashed', linewidth=1.5, label='Mean')
        axes[0, 1].axvline(paid_df[column_name].mean(), color='blue', linestyle='dashed', linewidth=1.5, label='Mean')
        axes[0, 2].axvline(charged_default_df[column_name].mean(), color='blue', linestyle='dashed', linewidth=1.5, label='Mean')
        axes[0, 3].axvline(risky_df[column_name].mean(), color='blue', linestyle='dashed', linewidth=1.5, label='Mean')

        # Remove spine from histograms
        sns.despine(ax=axes[0, 0])
        sns.despine(ax=axes[0, 1])
        sns.despine(ax=axes[0, 2])
        sns.despine(ax=axes[0, 3])

        # Generate violin plots
        sns.violinplot(data=df, y=column_name, color='#fb9a99', ax=axes[1, 0])
        sns.violinplot(data=paid_df, y=column_name, color='#fb9a99', ax=axes[1, 1])
        sns.violinplot(data=charged_default_df, y=column_name, color='#fb9a99', ax=axes[1, 2])
        sns.violinplot(data=risky_df, y=column_name, color='#fb9a99', ax=axes[1, 3])

        # Adding horizontal mean lines
        axes[1, 0].axhline(df[column_name].mean(), color='red', linestyle='dashed', linewidth=1.5, label='Mean')
        axes[1, 1].axhline(paid_df[column_name].mean(), color='red', linestyle='dashed', linewidth=2, label='Mean')
        axes[1, 2].axhline(charged_default_df[column_name].mean(), color='red', linestyle='dashed', linewidth=2, label='Mean')        
        axes[1, 3].axhline(risky_df[column_name].mean(), color='red', linestyle='dashed', linewidth=2, label='Mean')

        pyplot.suptitle(column_name, fontsize='xx-large') # Overall Plot title
        pyplot.tight_layout()

        return pyplot.show()
