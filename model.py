import pandas as pd  
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
import data_loader
import pre_processing
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin

# class Model:

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) # To render Homepage
@cross_origin()
def home_page():
    return render_template('index.html')


@app.route("/model", methods=['POST'])
@cross_origin()

        # def __init__(self):
        #     pass

def trainingModel():
    if (request.method=='POST'):

        # Getting the data from the source

        try:
            data=request.form['data']
                
            data=data_loader.Data_Getter().get_data() 

            data=pre_processing.Preprocessor().remove_column(data, ['explicit'])

            data=pre_processing.Preprocessor().remove_null_values(data)

            data=pre_processing.Preprocessor().change_index(data, ['release_date'])

            data=pre_processing.Preprocessor().time_duration(data)

            data=pre_processing.Preprocessor().correlations(data)

                # asd=data.info()
            return render_template('results.html', data=data)

        except:
            print("Model is failed")
            


if __name__ == '__main__':
    app.run()



# a=Model()
# print(a.trainingModel(),'********************************aad')




            
