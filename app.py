import numpy as np
import pandas as pd
from flask import Flask, abort, jsonify, request
from pandas.io.json import json_normalize
import pickle as pickle
import sklearn
import random

with open('pickle_model', 'rb') as f:
   model = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def default():
   return 'Homepage'

@app.route('/api', methods=['POST'])
def predict():
    input = request.get_json(force=True)
    hq=input['headquarters']
    industry=input['industry']
    founders=input['numFounders']
    funding_round=input['numFundingRounds']
    articles=input['numArticles']
    employees=input['numEmployees']

    predict_df=pd.DataFrame(columns=['Headquarters Location', 'Categories',
       'Number of Founders',
       'Number of Funding Rounds',
       'Number of Articles',
       'Number of Employees'])
   
    predict_df.loc[0] = ([hq, industry, founders, funding_round, articles, employees])
   

    predict = model.predict_proba(predict_df)[0][1]
    z =random.random() *.03
    x =float("%.4f" % round(z,4))
    predict1 = (predict - x) * 100
    prediction =float(("%.2f" % round(predict1,2)))
    if prediction < 0:
      prediction = 0
    return jsonify(prediction=prediction)

if __name__ == '__main__':
   app.run()

