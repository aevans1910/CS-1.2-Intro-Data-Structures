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

    print(dictionary)

histogram()