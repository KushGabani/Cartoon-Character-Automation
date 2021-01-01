import os
import io
import sys
import warnings
import shutil
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Embedding
from flask import Flask, url_for, request, render_template
from werkzeug.utils import secure_filename

warnings.filterwarnings("ignore")

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

punctuations = {
    '.' : "period", 
    '[' : "leftbraces",
    ']' : "rightbraces",
    '(' : "leftparen",
    ')' : "rightparen",
    ';' : "semicolon",
    '$' : "price",
    '%' : "percentage",
    '&' : "and",
    '#' : "hash",
    '\n' : "newline",
    ':' : "colon", 
    "'" : "apostrophe",
    '/' : "or",
    '"' : "quote",
    ',' : "comma",
    '?' : "question",
    '*' : "asterisk",
    '!' : "exclamation",
    '-' : "hyphen",
}

def get_prediction_from_cnn(file_path):
    model = load_model("./neural_networks/character-recognition-model.h5")

    image = cv2.imread(file_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (100, 100))
    image = np.reshape(image, (1, 100, 100, 3))
    prediction = model.predict(image)
    char_index = np.argmax(prediction, axis = 1)
    return characters[char_index[0]]

def preprocess_text(text):
  for punc, alt in punctuations.items():
    text = text.replace(punc, ' ' + alt + ' ')
  text = text.replace("\n", punctuations["\n"])
  tokens = text.split()
  return tokens

def get_tokenizer():
    with io.open("./script_data/moes_tavern_lines.txt", encoding = "utf-8-sig") as f:
        text = f.read().lower()
        text = text[81:]

    print("Loaded script as a text file.")

    tokens = preprocess_text(text)
    print("Preprocessed data.")
    sequence_length = 50 + 1
    lines = []

    for i in range(sequence_length, len(tokens)):
        sequence = tokens[i - sequence_length : i]
        lines.append(' '.join(sequence))
    print("Built sequences")

    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(lines)
    print("Fit tokenizer on data.")
    return tokenizer

def generate_script_from_lstm(text_input, n_words):
    sequence_length = 50
    tokenizer = get_tokenizer()
    vocab_size = len(tokenizer.word_index) + 1

    model = Sequential()
    model.add(Embedding(vocab_size, 50, input_length=50))
    model.add(LSTM(256))
    model.add(Dense(128, activation='relu'))
    model.add(Dense(vocab_size, activation='softmax'))
    model.load_weights("./neural_networks/script-generation-model-weights-with-punctuation.h5")
    model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

    model = load_model("./neural_networks/script-generation-model-with-punctuation.h5")
    print("Loaded Model")

    text = ""
    for _ in range(n_words):
        encoded = tokenizer.texts_to_sequences([text_input])[0]
        encoded = pad_sequences([encoded], maxlen = sequence_length, truncating='pre')

        y_predict = model.predict_classes(encoded)

        predicted_word = ''
        for word, index in tokenizer.word_index.items():
            if index == y_predict:
                predicted_word = word
                break
        text_input = text_input + ' ' + predicted_word

        if predicted_word in list(punctuations.values()):
            predicted_word = list(punctuations.keys())[list(punctuations.values()).index(predicted_word)]
        text += predicted_word + " "
        if predicted_word == ".":
            text += "<br/>"
    return text

@app.route('/', methods=['GET'])
def index():
    return render_template('character-recognition.html')

@app.route('/script-generation', methods=['GET', 'POST'])
def script_generation():
    if request.method == "GET":
        return render_template('script-generation.html', result = False)
    else:
        beginning = request.form['input']
        input_text = beginning.replace("<br/>", "")
        n_words = int(request.form['word']) if request.form['word'] else 100
        output = generate_script_from_lstm(input_text, n_words)
        output = beginning + "<br/>" + output
        return render_template('script-generation.html', result = output)

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
