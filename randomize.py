import random

#Fisher-Yates function that generates a random order for the words in script
def random_script_order(script, length):
    #This code randomly selects one word from the script, then randomly selects another
    #word from the script, and then switches the two. It does this for every word in
    #the script
    for selected_word1 in range(length):
        selected_word2 = random.randint(0, selected_word1)

        script[selected_word1],script[selected_word2] = script[selected_word2],script[selected_word1]
    return script

script = ['hello', 'earthlings', 'I', 'have', 'come', 'to', 'dominate', 'your', 'planet']
length = len(script)
print(random_script_order(script,length))
    
        
