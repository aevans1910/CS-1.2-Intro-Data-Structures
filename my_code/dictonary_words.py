import os
import random

def read_words():
    '''A function that reads a text file of words'''

    pathname = '/usr/share/dict/words'
    
    f = open(pathname, 'r')
    words_list = f.readlines()
    f.close()

    return words_list

def select_random_words(number_of_words):
    '''A function that selects random words from the words file'''
    
    words = read_words()
    selected_words = []
    for _ in range(number_of_words):
        selected_words.append(random.choice(words)[:-2])
    
    return selected_words

def display_words():
    '''A function that displays a sentence of the number of random 
    words a user wants to string together'''

    how_many_words = input (
        'How many words would you like your sentence to be composed of? ')
    number_of_words = int(how_many_words)

    random_word = select_random_words(number_of_words)

    print(' '.join (random_word).capitalize()+'.')

display_words()

if __name__ == "__main__":
    filename = '/usr/share/dict/words'
    word_list = read_words()
    display_words()








