from dictogram import Dictogram
import random

class MarkovChain(Dictogram):

    def create_markov_chain(self):
        '''Creating the markov chain'''
        # Create a markov chain from histogram
        markov_chain_histogram = Dictogram()

        # Start counter
        i = 0
        # For all the words in the list of words we have
        for word in self.word_list:
            # Add 1 to counter
            i += 1
            # As long as i is less then or equal to the length of words
            if i <= len(self.word_list)-1:
                # The next word will be the one with the next index in the list of words
                next_word = self.word_list[i]
                # If the word in not yet in the histogram
                if word not in markov_chain_histogram.keys():
                    # Add an entry of that word in the histogram
                    markov_chain_histogram[word] = Dictogram()
                # If word already exsists, increase its token count by 1
                markov_chain_histogram[word].add_count(next_word)
            
        return markov_chain_histogram

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