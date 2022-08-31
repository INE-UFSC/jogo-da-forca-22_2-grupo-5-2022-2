import os


def clear_screen():
    """Executa o comando para limpar a tela"""
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def draw(word, guesses):
    pass


def ask_for_char(guesses) -> str:
    pass


def ask_to_play_again() -> bool:
    pass
