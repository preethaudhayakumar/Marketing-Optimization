import pandas as pd
bold_s = '\033[1m' #----- To print bold font
bold_e = '\033[0m'

def file_read(dataset_name):
    """
    Excel file reading
    
    Parameters
    ----------
    dataset_name : str
    Name of the dataset to be read
    Example: data = 'Soc_Dem', data = 'Sales_Revenues'
    
    """
    return pd.read_excel('./DataScientist_CaseStudy_Dataset.xlsx', sheet_name = dataset_name) 
    


class Preprocess:  
    def display_data(self, data , name, no_of_rows = 5):
        """
        Performs basic exploratory operations on a given dataset

        Operations:
        1. Displays sample rows of the provided dataset.
        2. Prints the number of observations in the dataset.
        3. Displays the data types of each feature in the dataset.

        Parameters
        ----------
        data : DataFrame
        dataset
        Example: data = Soc_Dem, data = Sales_Revenues

        name : str
        Name of the dataset.
        Example: name = 'Soc_Dem', name = 'Sales_Revenues'

        no_of_rows : int
        Number of data samples (rows) to display.
        """
        
        print(f'\n\n{bold_s}#----- Displaying top {no_of_rows} rows of data-group:{name}{bold_e}')
        display(data.head(no_of_rows))
        print(f'\n{bold_s}#----- No.of observations{bold_e}\n{data.shape[0]}')
        print(f'\n{bold_s}#----- features\' datatypes and other info{bold_e}')
        print(f'\n{data.info()}')

    def inspect_missing_values(self, data):
        """
        Prints the sum of missing (null) values of given datasets' features.

        Parameters
        ----------
        data : DataFrame
        dataset
        Example: data = Soc_Dem, data = Sales_Revenues
        """
        print(f'\n\n{bold_s}#----- Inspecting missing values{bold_e}')
        print(data.isna().sum())

    def remove_missing_values(self, data, feature):
        """
        Deletes rows where specified features contain null (NaN) values and returns the cleaned dataset.

        Parameters
        ----------
        data : DataFrame
        dataset
        Example: data = Soc_Dem, data = Sales_Revenues

        feature : list
        List of column names (features) to check for missing values.

        Returns
        -------
        DataFrame
        Null values removed dataset
        """
        data.dropna(inplace = True, subset = feature)
        self.inspect_missing_values(data)

    def replace_missing_values(self, data):
        """
        Replace all the null (NaN) values to 0.

        Parameters
        ----------
        data : DataFrame
        dataset
        Example: data = Soc_Dem, data = Sales_Revenues

        """
        data.fillna(0 ,inplace = True)
        self.inspect_missing_values(data)

    def descriptive_stats(self, data, name, feature):
        """
        Prints statistical summaries (mean, standard deviation, minimum, and maximum) 
        for the specified features of the dataset

        Parameters
        ----------
        data : DataFrame
        dataset 
        Example: data = Soc_Dem, data = Sales_Revenues

        feature : list
        List of column names (features) for which to compute statistics.
        feature = list of column ids 
        """
        for i in feature:
            print(f'\n{bold_s}#----- Descriptive Stats of feature: {i} of data-group:{name}{bold_e}')
            print(f'Mean:{data[i].mean()} Std:{data[i].std()}')
            print(f'Min_value :{data[i].min()} Max_value:{data[i].max()}')

    
