def histogram():
    ''' A function that return a histogram data structure that stores each unique 
    word along with the number of times the word appears in the source text'''

    file = 'Grim-tales.txt'

    with open(file, 'r') as f:
        text = f.read().split()

    dictionary = {}
    for word in text:

        if word in dictionary.keys():
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    return dictionary

def list_histogram():
    ''' A function that return a histogram data structure that stores each unique 
    word along with the number of times the word appears in the source text, but 
    instead of using a dictionary, it uses a list'''

    file = 'Grim-tales.txt'

    with open(file, 'r') as f:
        text = f.read().split()

    histogram_list = []
    for word in text:
        list_word = [word, 0]
        for word2 in text:
            if word == word2:
                list_word[1] += 1
        if list_word not in histogram_list:
            histogram_list.append(list_word)

    return histogram_list

def unique_words(histogram):
    '''A function that takes a histogram argument and returns the total count 
    of unique words in the histogram'''
    count = 0
    for word in histogram.keys():
        if histogram.get(word) == 1:
            count += 1

def frequency (word, histogram):
    '''A function that takes a given word and histogram argument and returns the 
    number of times that word appears in a text'''

    return histogram.get(word)

if __name__ == "__main__":
    histo = list_histogram()
    #This code checks the frequency of the word 'I' within the text provided
    print (frequency ('I', histo))

