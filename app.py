import json
from difflib import get_close_matches


data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    close_matches = get_close_matches(word, data.keys())
    if word in data:
        return data[word]
    elif len(close_matches) > 0:
        yon = input(f'Did you mean {close_matches[0]}? Enter Y if yes, or N if no: ')
        if  yon == "Y":
            return data[close_matches[0]]
        elif yon == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."
        
    else:
        return "The word doesn't exist. Please double check it"

word = input("Enter a word: ")

print(translate(word))