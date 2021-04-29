# imports
import numpy as np
import pickle

from flask import Flask, request, render_template

app = Flask('my_app')

@app.route('/')
def home():
    return '"One Piece" Fanart Classification Project'

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/result')
def result():
    model = pickle.load(open('../cap_model/saved_model.pb', 'rb'))

    return render_template('results.html')


if __name__ == '__main__':
    app.run(debug=True)
