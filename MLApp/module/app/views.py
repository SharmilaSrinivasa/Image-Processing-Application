from flask import render_template, request
from flask import redirect, url_for
import os
from PIL import Image
from app.utils import pipeline_model

UPLOAD_FOLDER = 'static/uploads'


def base():
    return render_template('base.html')


def index():
    return render_template('index.html')


def gender():
    return render_template('gender.html')


def getWidth(path):
    img = Image.open(path)
    size = img.size
    aspect = size[0]/size[1]
    w = 300 * aspect
    return int(w)


def genderModel():
    if request.method == 'POST':
        f = request.files['image']
        filename = f.filename
        path = os.path.join(UPLOAD_FOLDER, filename)
        f.save(path)
        w = getWidth(path)
        # prediction
        pipeline_model(path, filename, color='bgr')
        return render_template('genderModel.html', fileupload=True, img_name=filename, w=w)
    return render_template('genderModel.html', fileupload=False, img_name="test.png", w=300)
