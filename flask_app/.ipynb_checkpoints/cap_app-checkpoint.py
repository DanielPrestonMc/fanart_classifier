# imports
import numpy as np
import pickle
import os

from matplotlib.pyplot import imshow
from flask import Flask, request, Response, render_template, flash, redirect, url_for
from werkzeug.utils import secure_filename
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from PIL import Image

app = Flask('my_app')

# folder to save images to use in html and store images uploaded to model
upload_folder = 'static/'

# specifying folder to save/load image files
app.config['upload_folder'] = upload_folder

# home page with form html template
@app.route('/')
def home():
    return render_template('form.html')

# results page after submitting image to model
@app.route('/results', methods=['GET', 'POST'])
def results():
    # Reference: https://dev.to/svencowart/multi-value-query-parameters-with-flask-3a92
    # Reference: https://pythonise.com/series/learning-flask/the-flask-request-object#url-info
    # Reference: https://tutorial101.blogspot.com/2021/04/python-flask-upload-and-display-image.html
    # Reference: https://stackoverflow.com/questions/11262518/how-to-pass-uploaded-image-to-template-html-in-flask
    # save submitted image file to variable
    data = request.files['results']

    # secure file name to variable
    filename = secure_filename(data.filename)

    # create string with path and image file name for where to store submitted image
    path = os.path.join(app.config['upload_folder'], filename)

    # save the image file to local path name
    data.save(path)

    # load in trained model
    model = load_model('./model')

    # Reference: https://keras.io/api/preprocessing/image/
    # load image file from local path and change image dimensions for model
    test_img = image.load_img(path=(path),
                          target_size=(255,350)
                          )
    # convert image to array data
    test_data = image.img_to_array(test_img)
    # change array data to numpy array specifically for model
    test_data = np.array([test_data])

    # make prediction on user submitted image
    pred = np.round(model.predict(test_data))

    # dictionary mapping prediction values to character names and matching image for output
    pred_names = {
        '"Soul King" Brook': ['[[1. 0. 0. 0. 0. 0. 0. 0. 0.]]', 'brook'],
        'Tony Tony Chopper': ['[[0. 1. 0. 0. 0. 0. 0. 0. 0.]]', 'chopper'],
        'Cyborg Franky': ['[[0. 0. 1. 0. 0. 0. 0. 0. 0.]]', 'franky'],
        'Monkey D. Luffy': ['[[0. 0. 0. 1. 0. 0. 0. 0. 0.]]', 'luffy'],
        '"Cat Burglar" Nami': ['[[0. 0. 0. 0. 1. 0. 0. 0. 0.]]', 'nami'],
        'Nico Robin': ['[[0. 0. 0. 0. 0. 1. 0. 0. 0.]]', 'robin'],
        '"Black Foot" Sanji': ['[[0. 0. 0. 0. 0. 0. 1. 0. 0.]]', 'sanji'],
        'God Usopp': ['[[0. 0. 0. 0. 0. 0. 0. 1. 0.]]', 'usopp'],
        'Roronoa Zoro': ['[[0. 0. 0. 0. 0. 0. 0. 0. 1.]]', 'zoro']
    }

    # looping through dictionary to identify correct prediction and output character name and images
    for n,p in pred_names.items():
        if str(pred) == p[0]:
            pred = n
            char = p[1]


    return render_template('results.html', data=pred, filename=filename, char=char)


if __name__ == '__main__':
    app.run(debug=True)
