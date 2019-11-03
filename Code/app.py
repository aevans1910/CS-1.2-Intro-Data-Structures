from flask import Flask
import stochastic_sampling
app = Flask(__name__)

@app.route('/')
def sampling():
    histo = stochastic_sampling.histogram(stochastic_sampling.get_text())
    random_words = stochastic_sampling.sample_frequency(histo)
    
    return random_words