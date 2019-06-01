import numpy as np
import pandas as pd
from flask import Flask, abort, jsonify, request
import random

app = Flask(__name__)

@app.route('/')
def default():
   return 'API Baseline Deployed'

@app.route('/fake', methods=['POST'])
def fake():
    test = np.random.randint(10)
    return jsonify(test=test)

if __name__ == '__main__':
   app.run()
