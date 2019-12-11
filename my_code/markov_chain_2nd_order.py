from dictogram import Dictogram
from clean_up_text import read_text, cleanup_text, start_token, stop_token
import random

class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(item)

    def deque(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


class MarkovChainSecond(Dictogram, Queue):

    def create_markov_chain(self):
        '''Creating the markov chain'''
        markov_chain_histogram = Dictogram()
        # markov_queue = []

        # for i in range(len(self.word_list)-1):
        #     first = self.word_list[i]
        #     second = self.word_list[i+1]
        #     markov_queue.enqueue(first)
        #     markov_queue.enqueue(second)

        for i in range(len(self.word_list)-1):
            first = self.word_list[i]
            second = self.word_list[i+1]

            if second != '#STOP#':
                third = self.word_list[i+2]

            key = (first, second)
            if key not in markov_chain_histogram.keys():
                markov_chain_histogram[key] = Dictogram()
            
            markov_chain_histogram.get(key).add_count(third)

        return markov_chain_histogram


    def random_sentence(self, steps):
        word = self.sample()
        sentence = [word]
        print (sentence)

        markov_histogram = self.create_markov_chain()

        i = 0
        while i != steps:
            i += 1
            next_word = markov_histogram[word].sample()
            sentence.append(next_word)
            word = next_word

            if next_word == "#STOP#":
                break

        return ' '.join(sentence)


if __name__ == "__main__":
    words_list = read_text('corpus.txt')
    # print(words_list)
    clean_text = cleanup_text(words_list)
    # print(clean_text)
    stop_token = stop_token(clean_text)
    start_token = start_token(clean_text)
    # print(clean_text)
    markov_sentence = MarkovChainSecond(stop_token)
    # print (markov_sentence)
    print(markov_sentence.random_sentence(5))
    nested_histo = markov_sentence.create_markov_chain()

    # print(nested_histo['fish'].sample())