from flask import Flask
import sample
app = Flask(__name__)

@app.route('/')
def sampling():
    histo = sample.histogram(sample.get_text())
    random_words = sample.sample_frequency(histo)
    
    return random_words