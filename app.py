import json
from difflib import get_close_matches


data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    close_matches = get_close_matches(word, data.keys())
    if word in data:
        return data[word]
    elif len(close_matches) > 0:
        return f'Did you mean {close_matches[0]}'
        
    else:
        return "The word doesn't exist. Please double check it"

word = input("Enter a word: ")

print(translate(word))