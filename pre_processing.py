import data_loader 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class Preprocessor:

    """ This class shall be used to clean and transform the data """
 
    def __init__(self):
        pass


    def remove_column(self, data, column):
        """
            Method Name: remove_column
            Description: This method removes the given columns from a pandas dataframe.
            Output: A pandas DataFrame after removing the specified columns.
            On Failure: Raise Exception
        """
        self.data=data
        self.column=column
        try:
            self.useful_data= self.data.drop(columns=self.column, axis=1)
            return self.useful_data
        except:
            print("Unable to remove the column")



    def remove_null_values(self, data):
        """
            Method Name: remove_null_values
            Description: This method is for replacing the null values.
            Output: The null values that are present in the DataFrame, are replaced by 'NA'.
            On Failure: Raise Exception
        """
        self.data=data
        try:
            self.no_null_values=self.data.fillna('NA')
            return self.no_null_values
        except:
            print('No null values found')


    
    def change_index(self, data, column):
        """
            Method Name: change_index
            Description: This method is for setting new index name.
            Output: The column index 'release_date' is now added the row index.
            On Failure: Raise Exception
        """
        self.data=data
        self.column=column
        try:     
           self.changed_index=self.data.set_index(self.column, inplace=True)
           self.changed_index=self.data.index=pd.to_datetime(self.data.index)
           self.changed_index=self.data.head()
           return self.changed_index
        except:
            print("Unable to change the Index")


    def time_duration(self, data):
        """
            Method Name: time_duration
            Description: This method coverted the time duration in secs of 'duration_ms' column which was in milisecs before
            Output: The new column 'duration' has been created which is the replacement of 'duration_ms' column.
            On Failure: Raise Exception
        """
        self.data=data
        try:
            self.new_duration= self.data["duration"]=self.data["duration_ms"].apply(lambda x: round(x/1000))
            self.new_duration=self.data.drop(["duration_ms"], inplace=True, axis=1)
            self.new_duration=self.data.head()
            return self.new_duration
        except:
            print("Unable to make changes in time duration column")

    
    def correlations(self, data): 
        """
            Method Name: correlation
            Description: This method shows the correlation of all columns.
            Output: The correlation chart in png format.
            On Failure: Raise Exception
        """
        self.data=data
        try:
            self.corr_data= self.data.corr(method="pearson")
            # self.corr_data=self.data.plt.figure(figsize=(14,16))
            self.heatmaps=sns.heatmap(self.corr_data, annot=True,fmt='.1g',vmin=-1, vmax=1, center=1, cmap='inferno', linewidths=1, linecolor="Black") 
            # self.heatmaps=self.heatmaps.set_title("Correlation Heatmap between variable")
            # self.heatmaps=self.heatmaps.set_xticklabels(self.heatmap.get_xticklabels(), rotation=90)
            plt.savefig('Corelation chart')
            return self.heatmaps
        except:
            print("Unable to plot the correlation chart")









