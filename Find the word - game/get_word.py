from uzwords import words
import random

def get_word(): # returns a <word> as <object>
    word = random.choice(words)
    while "-" in word or ' ' in word:
        word = random.choice(words)
    return word.upper()