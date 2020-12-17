import os
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model
from flask import Flask, url_for, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

characters = ['Abraham Grampa Simpson',
 'Agnes Skinner',
 'Apu Nahasapeemapetilon',
 'Barney Gumble',
 'Bart Simpson',
 'Carl Carlson',
 'Charles Montgomery Burns',
 'Chief Wiggum',
 'Cletus Spuckler',
 'Comic Book Guy',
 'Disco Stu',
 'Edna Krabappel',
 'Fat Tony',
 'Gil',
 'Groundskeeper Willie',
 'Homer Simpson',
 'Kent Brockman',
 'Krusty The Clown',
 'Lenny Leonard',
 'Lionel Hutz',
 'Lisa Simpson',
 'Maggie Simpson',
 'Marge Simpson',
 'Martin Prince',
 'Mayor Quimby',
 'Milhouse Van Houten',
 'Miss Hoover',
 'Moe Szyslak',
 'Ned Flanders',
 'Nelson Muntz',
 'Otto Mann',
 'Patty Bouvier',
 'Principal Skinner',
 'Professor John Frink',
 'Rainier Wolfcastle',
 'Ralph Wiggum',
 'Selma Bouvier',
 'Sideshow Bob',
 'Sideshow Mel',
 'Snake Jailbird',
 'Troy Mcclure',
 'Waylon Smithers']

def get_prediction_from_cnn(file_path):
    model = load_model("./cnn_model/character-recognition-model.h5")

    image = cv2.imread(file_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (100, 100))
    image = np.reshape(image, (1, 100, 100, 3))
    prediction = model.predict(image)
    char_index = np.argmax(prediction, axis = 1)
    return characters[char_index[0]]

@app.route('/', methods=['GET'])
def index():
    return render_template('character-recognition.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == "POST":
        print("Reached Here")
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        prediction = get_prediction_from_cnn(file_path)
        return prediction
    return 'GET Request /predict'

if __name__ == "__main__":
    app.run(debug=True)