from dictogram import Dictogram
import random

class MarkovChain(dict):

    def __init__(self, words_list=None):
        '''Initilising the Markiv Chain'''
        super(MarkovChain, self).__init__()

        if words_list is not None:
            self.create_markov_chain(words_list)


    def create_markov_chain(self, words_list):
        '''Creating the markov chain'''
        previous = None
        for word in words_list:
            #This first part checks if the word is already in
            #the histogram
            if self.get(word) == None:
                self[word] = Dictogram()
            if previous != None:
                if self[previous][word] != None:
                    self[previous][word] += 1
                if self[previous][word] == None:
                    self[previous][word] = 1
            previous = word


    def sample(self, word):
        '''Samples a word from histogram with '''
        histo = self.get(word, None)

        if histo is not None:
            return histo.sample(1)
        else:
            return None

    def random_sentence(self):
        random_word = random.choice(list(self.keys))
        first_word = random_word.capitalize()
        words = [first_word]
        other_random_words = random.choice(list(self.keys))

        for _ in range(len - 1):
            
            other_random_words = self.sample(other_random_words)[0]
            words.append(other_random_words)

        return ' '.join(words) + '.'

def clean_up_words(file_name):
    '''Cleans up words so we can use them anywhere
    in the sentence'''
    with open(file_name, 'r') as f:
        words = f.read().split()

    word_list = []
    for word in words:
        word = word.strip(".@'/").lower()
        word_list.append(word)

    return word_list

if __name__ == "__main__":
    words_list = clean_up_words('random_sentence.txt')
    markov_sentence = MarkovChain(words_list=words_list)

    print(markov_sentence.random_sentence())