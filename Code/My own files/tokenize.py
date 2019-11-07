import random

#Fisher-Yates function that generates a random order for the words in script
def random_script_order(script, n):
    for i in range(n):
        j = random.randint(0, i)

        script[i],script[j] = script[j],script[i]
    return script

script = ['hello', 'earthlings', 'I', 'have', 'come', 'to', 'dominate', 'your', 'planet']
n = len(script)
print(random_script_order(script,n))
    
        
