import cv2
import numpy as np
import os
import sys 
from flask import (
     Flask, 
     request, 
     render_template)
from model import predict
from size import predict_size



UPLOAD_FOLDER='./static/dog_image'

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/photo')
def photo():
   return render_template('photo.html')

@app.route('/top')
def top():
   return render_template('top.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_user_files():
    if request.method == 'POST':
        upload_file = request.files["upload_file"]
        img_path = os.path.join(UPLOAD_FOLDER,upload_file.filename)
        upload_file.save(img_path)
        result, score = predict(img_path)

        length = predict_size(img_path)

        return render_template('result.html', score=int(score*100), result=result, img_path=img_path, length=length)


if __name__ == "__main__":
    app.run(debug=True)