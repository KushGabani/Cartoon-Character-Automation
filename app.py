import os
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model
from flask import Flask, url_for, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

characters = ['abraham_grampa_simpson',
 'agnes_skinner',
 'apu_nahasapeemapetilon',
 'barney_gumble',
 'bart_simpson',
 'carl_carlson',
 'charles_montgomery_burns',
 'chief_wiggum',
 'cletus_spuckler',
 'comic_book_guy',
 'disco_stu',
 'edna_krabappel',
 'fat_tony',
 'gil',
 'groundskeeper_willie',
 'homer_simpson',
 'kent_brockman',
 'krusty_the_clown',
 'lenny_leonard',
 'lionel_hutz',
 'lisa_simpson',
 'maggie_simpson',
 'marge_simpson',
 'martin_prince',
 'mayor_quimby',
 'milhouse_van_houten',
 'miss_hoover',
 'moe_szyslak',
 'ned_flanders',
 'nelson_muntz',
 'otto_mann',
 'patty_bouvier',
 'principal_skinner',
 'professor_john_frink',
 'rainier_wolfcastle',
 'ralph_wiggum',
 'selma_bouvier',
 'sideshow_bob',
 'sideshow_mel',
 'snake_jailbird',
 'troy_mcclure',
 'waylon_smithers']

def get_prediction_from_cnn(file_path):
    model = load_model("./cnn_model/character-recognition-model.h5")

    image = cv2.imread(file_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (100, 100))
    image = np.reshape(image, (1, 100, 100, 3))
    prediction = model.predict(image)
    char_index = np.argmax(prediction, axis = 0)
    return characters[char_index]
    return str(image.shape)

@app.route('/', methods=['GET'])
def index():
    return render_template('character-recognition.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == "POST":
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        prediction = get_prediction_from_cnn(file_path)
        return prediction
    return 'GET Request /predict'

if __name__ == "__main__":
    app.run(debug=True)
