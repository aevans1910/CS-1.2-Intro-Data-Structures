from dictogram import Dictogram
import random

class MarkovChain(dict):

    def __init__(self, word_list=None):
        '''Initilising the Markiv Chain'''
        super().__init__()

        if word_list is not None:
            self.create_markov_chain(word_list)


    def create_markov_chain(self, word_list):
        for index, word in enumerate(words_list):

            #This first part checks if the word is already in
            #the histogram
            if self.get(word) == None:
                self[word] = Dictogram()

            #This second part makes sure that the range 
            #stays within the limits of the text
            if index + 1 < len(words_list) - 1:
                next_word = words_list[index + 1]
                self.get(word).add_count(next_word)