import os
import requests
import jsonpickle
from bs4 import BeautifulSoup

WORD_LIST_PATH = 'word_list.json'


class Dictionary:
    def __init__(self):
        if not os.path.exists(WORD_LIST_PATH):
            # Baixar da Internet
            self.download_word_list()
        else:
            # Abrir o arquivo salvo
            with open(WORD_LIST_PATH, 'r') as file:
                self.word_list = jsonpickle.decode(file.read())

    def get_random_word(self) -> str:
        pass

    def download_word_list(self):
        '''Baixa um conjunto de palavras da Internet e salva como um JSON'''
        self.word_list = set()

        # Obter o conjunto de palavras da Internet
        response = requests.get('https://www.dicio.com.br/lista-de-palavras/')
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            for word_list_element in soup.find_all('p', class_='words-list--links'):
                for word_element in word_list_element.find_all('a'):
                    self.word_list.add(word_element.get_text())

        # Salvar como JSON
        json_data = jsonpickle.encode(self.word_list)
        with open(WORD_LIST_PATH, 'w', encoding='UTF-8') as file:
            file.write(json_data)
