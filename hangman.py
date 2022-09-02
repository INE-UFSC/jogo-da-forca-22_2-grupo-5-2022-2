from dictionary import Dictionary
import ui


class Hangman:
    def __init__(self):
        self.dictionary = Dictionary()

    def run(self):
        while True:
            word = self.dictionary.get_random_word().upper()
            correct_guesses = ''
            wrong_guesses = ''

            while True:
                # Desenho e determina a vitória
                if ui.draw(word, correct_guesses, wrong_guesses) == 0:
                    print("Você Venceu!")
                    break

                # Verifica se a letra está correta
                guess = ui.ask_for_char(correct_guesses + wrong_guesses)
                if guess in word:
                    correct_guesses = correct_guesses + guess
                else:
                    wrong_guesses = wrong_guesses + guess

                if len(wrong_guesses) >= 7:
                    ui.draw(word, correct_guesses, wrong_guesses)
                    print("Você perdeu! A palavra era " + word.upper())
                    break

            # Pergunta se o jogo reiniciará
            play = ui.ask_to_play_again()
            if not play:
                break
