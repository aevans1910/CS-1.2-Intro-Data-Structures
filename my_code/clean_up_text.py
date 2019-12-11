import sys
from re import split, sub, IGNORECASE

def read_text(filename):
    '''Opens and reads a text file'''
    with open(filename, 'r') as f:
        read_text_file = f.read().split()
    read_text_file = [item.lower() for item in read_text_file]
    return read_text_file

def start_token(text):
    '''Add a start token'''
    text.insert(0, '#START#')
    return text

def stop_token(text):
    '''Add a stop token'''
    text.append('#STOP#')
    return text

# def create_sentence(text):
#     '''Makes first work capitalized'''
#     capitalization = " ".join(text).capitalize()
#     sentence = f"{capitalization}."
#     return sentence

if __name__ == "__main__":
    string = "he$l@ hbnjm .jnkm."
    print(read_text('corpus.txt'))