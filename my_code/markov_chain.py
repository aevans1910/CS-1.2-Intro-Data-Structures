from dictogram import Dictogram
from clean_up_text import read_text
import random

class MarkovChain(dict):
    def __init__ (self, words, order=1):
        self.order = order
        for index in range(len(words)-order):
            self.add_words(tuple(words[index:index+order]),tuple(words[index+1:index+order+1]))

        for key in self.keys():
            self[key] = Dictogram(self[key])   

    def add_words(self, word_1, word_2):
        if not word_1 in self.keys():
            self[word_1]=[]
        self[word_1].append(word_2)

    def random_sentence(self, length=8):
        sentence = []
        start_word = random.choice(list(self.keys()))
        next_word = self[start_word].sample()
        sentence += list(start_word)
        
        while len(sentence) < 10:
            start_word = random.choice(list(self.keys()))
            next_word = self[start_word].sample()

            sentence.append(next_word[self.order-1])

            start_word = next_word
        return ' '.join(sentence)


if __name__ == "__main__":
    words_list = read_text('corpus.txt')
    # words_list = ["a", "man", "a", "plan", "a", "canal"]
    markov_sentence = MarkovChain(words_list, 3)
    # print(markov_sentence)
    # for keys in markov_sentence.keys():
    #     print(keys, markov_sentence[keys])

    print(markov_sentence.random_sentence())