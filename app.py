from flask import Flask, request
import rasa_nlu.train


app = Flask(__name__)


@app.route('/')
def index():

    return 'Derp'

@app.route('/ask', methods=['POST'])
def ask():
    query = request.data



app.run(port=8080, debug=True)