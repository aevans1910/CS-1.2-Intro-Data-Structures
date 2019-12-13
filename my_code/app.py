from flask import Flask, render_template
import sample
from markov_chain import MarkovChain
from clean_up_text import read_text


app = Flask(__name__)

@app.route('/')
def index():
    '''This function calls the histogram function on a sample text. This will then pick a 
    random word and return it'''
    words_list = read_text('corpus.txt')
    markov_sentence = MarkovChain(words_list, 3).random_sentence(15)
    return render_template('index.html', gen=markov_sentence)
    # return markov_sentence.random_sentence(15)


if __name__ == "__main__":
    app.run(debug=True)