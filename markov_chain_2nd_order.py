from dictogram import Dictogram
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

        # i = 0
        # for word in self.word_list:
        #     i += 1
        #     if i <= len(self.word_list)-1:
        #         next_word = self.word_list[i]
        #         if word not in markov_chain_histogram.keys():
        #             markov_chain_histogram[word] = Dictogram()
        #         markov_chain_histogram[word].add_count(next_word)
            
        # return markov_chain_histogram

        for i in range(len(self.word_list)-1):
            first = self.word_list[i]
            second = self.word_list[i+1]

            key = (first, second)
            if key not in markov_chain_histogram.keys():
                markov_chain_histogram[key] = Dictogram()
            
            markov_chain_histogram.get(key).add_count()

        return markov_chain_histogram


    def random_sentence(self, length=8):
        word = self.sample()
        sentence = [word]

        markov_histogram = self.create_markov_chain()
        for _ in range(length-1):
            next_word = markov_histogram[word].sample()
            word = next_word
            sentence.append(next_word)
        return ' '.join(sentence)


def clean_up_words(file_name):
    '''Cleans up words so we can use them anywhere
    in the sentence'''
    with open(file_name, 'r') as f:
        words = f.read().split()

    word_list = []
    for word in words:
        word = word.strip("_")
        word_list.append(word)

    return word_list

if __name__ == "__main__":
    words_list = clean_up_words('random_sentence.txt')
    markov_sentence = MarkovChainSecond()
    print(markov_sentence.random_sentence())
    print(markov_sentence.random_sentence())
    nested_histo = markov_sentence.create_markov_chain()

    print(nested_histo['fish'].sample())