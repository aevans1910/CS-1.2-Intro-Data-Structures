from dictogram import Dictogram
import random

class MarkovChain(Dictogram):

    def create_markov_chain(self):
        '''Creating the markov chain'''
        previous = None
        markov_chain_histogram = Dictogram()

        i = 0
        for word in self.word_list:
            i += 1
            if i <= len(self.word_list)-1:
                next_word = self.word_list[i]
                if word not in markov_chain_histogram.keys():
                    markov_chain_histogram[word] = Dictogram()
                markov_chain_histogram[word].add_count(next_word)
            
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

    #     random_word = random.choice(list(self.keys))
    #     first_word = random_word.capitalize()
    #     words = [first_word]
    #     other_random_words = random.choice(list(self.keys))

    #     for _ in range(len - 1):
            
    #         other_random_words = self.sample(other_random_words)[0]
    #         words.append(other_random_words)

    #     return ' '.join(words) + '.'

    #     i = 0
    #     while 1 <= 10:
    #         sentence.append(word)


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
    markov_sentence = MarkovChain(words_list)
    print(markov_sentence.random_sentence())
    # print(markov_sentence.random_sentence())
    # nested_histo = markov_sentence.create_markov_chain(words_list)

    # print(nested_histo['fish'].sample())