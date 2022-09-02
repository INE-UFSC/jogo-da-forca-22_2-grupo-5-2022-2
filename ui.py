import os
import unidecode

SCREEN_TEMPLATE = '''
  _____
  |   |    ERROS
  |   1    <misses>
  |  243 
  |  5 6 
  |        <word>
__|______
'''
BODY_PARTS = ['0', '/', '\\', '|', '/', '\\']


def clear_screen():
    """Executa o comando para limpar a tela"""
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def draw(word, correct_guesses, wrong_guesses) -> int:
    '''Desenha a forca na tela e retorna a quantidade de letras que o jogador ainda precisa acertar'''
    clear_screen()
    current_screen = SCREEN_TEMPLATE

    # Adicionar partes do corpo correspondente ao erro
    for miss in range(1, 7):
        current_screen = current_screen.replace(str(miss), BODY_PARTS[miss - 1] if len(wrong_guesses) >= miss else ' ')
    # Adicionar texto de erros
    misses_text = wrong_guesses.ljust(7, '_')
    current_screen = current_screen.replace('<misses>', ' '.join(misses_text))

    # Adicionar as letras que o jogador já acertou
    filtered_word = unidecode.unidecode(word)
    word_text = word
    for i, char in enumerate(filtered_word):
        if char.isalpha() and char not in correct_guesses:
            word_text = word_text[:i] + '_' + word_text[i + 1:]
    current_screen = current_screen.replace('<word>', '  '.join(word_text))

    print(current_screen)

    # Retornar a quantidade de letras que falta o jogador acertar
    return word_text.count('_')


def ask_for_char(guesses) -> str:
    pass


def ask_to_play_again() -> bool:
    while True:
        print("Deseja jogar novamente? (s/n)")
        r = input().casefold()

        if r == "s":
            return True
        elif r == "n":
            return False
