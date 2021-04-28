# imports
import numpy as np
import pickle

from flask import Flask, request, render_template

app = Flask('my_app')

@app.route('/')
def home():
    return 'Home Page'

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/result')
def result():
    data = request.args
    X_test = np.array([
    int(data['OverallQual']),
    int(data['FullBath']),
    int(data['GarageArea']),
    int(data['LotArea'])
    ]).reshape(1, -1)
    model = pickle.load(open('../cap_model/saved_model.pb', 'rb'))
    pred = f'{round(model.predict(X_test)[0], 2):,}'

    return render_template('results.html', prediction=pred)


if __name__ == '__main__':
    app.run(debug=True)
