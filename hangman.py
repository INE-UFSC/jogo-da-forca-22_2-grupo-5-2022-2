from dictionary import Dictionary
import ui


class Hangman:
    def __init__(self):
        self.dictionary = Dictionary()
        self.word = self.dictionary.get_random_word()
        self.guesses = ' ' + '-'

    def run(self) -> bool:
        ui.clear_screen()
        ui.draw(self.word, self.guesses)

        guess = ui.ask_for_char(self.guesses)
        self.guesses = self.guesses + guess

        ui.clear_screen()
        play = ui.ask_to_play_again()
        return play