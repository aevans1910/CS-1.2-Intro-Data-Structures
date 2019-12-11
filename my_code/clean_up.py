import sys
from re import split, sub, IGNORECASE

def read_text(filename):
    '''Opens and reads a text file'''
    with open(filename, 'r') as f:
        read_text_file = f.read()
    return read_text_file

def cleanup_text(corpus):
    '''Cleans up text in corpus.txt. Converts all letters to lower case, takes
    out odd symbols, and takes out punctuation'''
    corpus = corpus.lower()
    no_symbols = sub('([\-\()"]*)([a-z]+)([?:!.,;\-\)"]*)',r'\2', corpus)
    text = split(r'\s', no_symbols)
    return text