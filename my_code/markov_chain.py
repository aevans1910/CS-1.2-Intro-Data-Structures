from dictogram import Dictogram
from clean_up_text import read_text
import random

class MarkovChain(dict):
    def __init__ (self, words, order=1):
        self.order = order
        for index in range(len(words)-1):
            self.add_words(words[index],words[index+1])

        for key in self.keys():
            self[key] = Dictogram(self[key])   

    def add_words(self, word_1, word_2):
        if not word_1 in self.keys():
            self[word_1]=[]
        self[word_1].append(word_2)

    def random_sentence(self, length=8):
        # Pick a random word from the original histogram
        word = self.sample()
        # Create a sentence list with the first sampled word as its start
        sentence = [word]
        # Create a new markov chain from the histogram
        markov_histogram = self.create_markov_chain()
        # Until we reach the length of 8
        for _ in range(length-1):
            # The next word will be randomly sampled from the first words histogram
            next_word = markov_histogram[word].sample()
            # Make word the next word
            word = next_word
            # Add the next word to the sentence
            sentence.append(next_word)
        # Join the words together to return something like a string
        return ' '.join(sentence)


if __name__ == "__main__":
    words_list = read_text('corpus.txt')
    # words_list = ["a", "man", "a", "plan", "a", "canal"]
    markov_sentence = MarkovChain(words_list)
    # print(markov_sentence)
    for keys in markov_sentence.keys():
        print(keys, markov_sentence[keys])

    # print(markov_sentence.random_sentence())
    # nested_histo = markov_sentence.create_markov_chain(words_list)

    # print(nested_histo['fish'].sample())