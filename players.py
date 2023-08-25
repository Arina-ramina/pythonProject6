class Player:
    def __init__(self, name_user):
        self.name_user = name_user
        self.word_user = []

    def __repr__(self):
        return f'Name:{self.name_user}, Used Words: {self.word_user}'

    def count_words_user(self):
        return len(self.word_user)

    def plus_used_words(self, word):
        self.word_user.append(word)

    def word_usage_check(self, word):
        return word in self.word_user
