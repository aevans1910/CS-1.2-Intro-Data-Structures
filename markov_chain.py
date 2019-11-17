from dictogram import Dictogram
import random

class MarkovChain():

    def __init__(self, word_list=None):
        '''Initilising the Markiv Chain'''
        super().__init__()

        if word_list is not None:
            self.create_markov_chain(word_list)


    def create_markov_chain(self, word_list):
        for index, word in enumerate(words_list):
            if self.get(word) == None:
                self[word] = Dictogram()

            