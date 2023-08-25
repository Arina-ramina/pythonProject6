import random
import requests
from basic_word import BasicWord


def load_random_word() -> BasicWord:
    url = 'https://api.npoint.io/b668673dcdf6d94fdb8c'
    response = requests.get(url)
    data = response.json()
    random_word = random.choice(data)
    word = random_word['word']
    subwords = random_word['subwords']

    return BasicWord(word, subwords)