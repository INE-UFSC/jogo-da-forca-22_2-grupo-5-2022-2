from dictionary import Dictionary


class Hangman:
    def __init__(self):
        self.dictionary = Dictionary()
        self.word = self.dictionary.get_random_word()
        self.guesses = ''

    def run(self):
        pass
