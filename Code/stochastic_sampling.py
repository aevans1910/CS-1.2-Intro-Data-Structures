import random

def get_text():
    file = 'random.txt'

    with open(file, 'r') as f:
        text = f.read().split()
    
    return text

def histogram(get_text):
    ''' A function that return a histogram data structure that stores each unique 
    word along with the number of times the word appears in the source text'''

    dictionary = {}
    for word in get_text:

        if word in dictionary.keys():
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    return dictionary

def sample_frequency(histogram):
    '''A function that takes a histogram and returns a single word, at random'''
    
    words_list = []

    for key in histogram:
        for _ in range(histogram[key]):
            words_list.append(key)

    random_word = random.choice(words_list)
    return (random_word)

if __name__ == '__main__':
    histo = histogram(get_text())

    results = []

    for counter in range(100):
        random_word = sample_frequency(histo)
        results.append(random_word)

    print (results)