import requests
import json
from app import add_word


def add_words_in_bd():
    '''
    Fill the database with nouns in the table "Words"
    '''
    # TODO when connect to non local db use Try-Except

    db = requests.get('https://raw.githubusercontent.com/Harrix/Russian-Nouns/main/src/data.json')
    db_dict = json.loads(db.text)
    for word in db_dict:
        add_word(word)
        print(f'Add word: {word}')
    print("END")
