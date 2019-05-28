#importing libraries
import os
import numpy as np
import flask
from sklearn.externals import joblib
from flask import Flask, render_template, request
#import pandas as pd

#creating instance of the class
app=Flask(__name__)

#to tell flask what url shoud trigger the function index()
@app.route('/')
#@app.route('/index')
def index():
    return flask.render_template('test.html')
	
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list)
    loaded_model = joblib.load('model.pkl')
    result = loaded_model.predict(to_predict)
    return result

@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list=np.array([list(map(int,list(to_predict_list.values())))])
        result = ValuePredictor(to_predict_list)
        #result = 2
        if int(result)==1:
            prediction='Approved'
        else:
            prediction='Declined'
        return render_template("result.html",prediction=prediction)


	
if __name__=='__main__':
	app.run(debug=True)
