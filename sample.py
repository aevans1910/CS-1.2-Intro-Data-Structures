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
    #This function randomly selects a word in the list
    random_word = random.randint(0,7)
    start_search_range = 0

    for word, count in histogram.items():
        end_search_range = start_search_range + count
        #Function goes through each range of possible frequencies in the list, and tries to 
        #match where the word selected is within the range
        if start_search_range <= random_word < end_search_range:
            return word
            # If the word is indeed within the range, then the word is returned
        start_search_range = end_search_range
        #If word not found,the search continues

if __name__ == '__main__':
    histo = histogram(get_text())

    results = []

    for counter in range(10):
        random_word = sample_frequency(histo)
        results.append(random_word)

    print (results)