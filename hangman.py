from dictionary import Dictionary
import unidecode
import ui


class Hangman:
    def __init__(self):
        self.dictionary = Dictionary()

    def run(self):
        while True:
            self.word = self.dictionary.get_random_word().upper()
            self.correct_guesses = ''
            self.wrong_guesses = ''

            while True:
                # Desenho e determina a vitória
                if ui.draw(self.word, self.correct_guesses, self.wrong_guesses) == 0:
                    print("Você Venceu!")
                    break
                print(self.word)

                # Verifica se a letra está correta
                guess = ui.ask_for_char(self.correct_guesses)
                for i,letra in enumerate(self.word):
                    if guess == unidecode.unidecode(letra):
                        self.correct_guesses = self.correct_guesses + guess
                        break
                    if i == len(self.word)-1:
                        self.wrong_guesses = self.wrong_guesses + guess

                if len(self.wrong_guesses) >= 7:
                    print("Você perdeu! A palavra era " + self.word.upper())
                    break

            # Pergunta se o jogo reiniciará
            play = ui.ask_to_play_again()
            if not play:
                break
            