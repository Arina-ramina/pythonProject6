class BasicWord:
    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

    def __repr__(self):
        return f'Word:{self.word}, Subwords:{self.subwords}'

    def check_subwords(self, subword):
        return subword in self.subwords

    def count_subwords(self):
        return len(self.subwords)