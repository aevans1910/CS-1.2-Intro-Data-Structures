def histogram():
    ''' A function that return a histogram data structure that stores each unique 
    word along with the number of times the word appears in the source text'''

    file = 'random.txt'

    with open(file, 'r') as f:
        text = f.read().split()

    dictionary = {}
    for word in text:

        if word in dictionary.keys():
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    return dictionary

def unique_words(histogram):
    '''A function that takes a histogram argument and returns the total count 
    of unique words in the histogram'''
    count = 0
    for word in histogram.keys():
        if histogram.get(word) == 1:
            count += 1

def frequency (word, histogram):
    '''A function that takes a word and histogram argument and returns the 
    number of times that word appears in a text'''

    for word in histogram:
        print (word)

histo = histogram()
print(unique_words(histo))
