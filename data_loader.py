import pandas as pd

class Data_Getter: 
    """ This class shall  be used for obtaining the data from the source for training. """


    def __init__(self):
        self.training_file="C:\\Users\\user\\Downloads\\Spotify dataset\\tracks.csv"
    


    def get_data(self):
        """
        Method Name: get_data
        Description: This method reads the data from source.
        Output: A pandas DataFrame.
        On Failure: Raise Exception
        
        """
        try:
            data= pd.read_csv(self.training_file) # reading the data file
            return data.head()
        except:
            print("Unable to load the dataset")


      



