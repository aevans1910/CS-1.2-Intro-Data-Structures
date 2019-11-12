from flask import Flask
import sample
app = Flask(__name__)

@app.route('/')
def sampling():
    '''This function calls the histogram function on a sample text. This will then pick a 
    random word and return it'''
    histo = sample.histogram(sample.get_text())
    random_words = sample.sample_frequency(histo)
    
    return random_words