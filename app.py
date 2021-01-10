import numpy as np
import pandas as pd
from flask import Flask,request,render_template
import pickle

app=Flask(__name__)
@app.route('/')
def home():
    print('home')
    return render_template('Demo.html')

def ValuePredictor(to_predict_list):
    to_predict=np.array(to_predict_list).reshape(1,18)
    loaded_model=pickle.load(open('Agent_Bonus.pkl',"rb"))
    result=loaded_model.predict(to_predict)
    return result[0]

@app.route('/predict',methods=['POST'])

def predict():
    if request.method=='POST':
        print('predict')
        to_predict_list=request.form.to_dict()
        to_predict_list=list(to_predict_list.values())
        to_predict_list=list(map(int,to_predict_list))
        result=ValuePredictor(to_predict_list)
        return render_template('predict.html',prediction="Agent Bonus should be ${}".format(round(result,2)))
    
if __name__=="__main__":
    print('main')
    app.run(debug=True)
    app.config['TEMPLATES_AUTO_RELOAD'] = True

                             