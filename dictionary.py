import os

import requests
import jsonpickle
from bs4 import BeautifulSoup
from random import Random

WORD_LIST_PATH = 'word_list.json'


class Dictionary:
    def __init__(self):
        if os.path.exists(WORD_LIST_PATH):
            # Abrir o arquivo salvo
            with open(WORD_LIST_PATH, 'r') as file:
                self.word_list = jsonpickle.decode(file.read())
        else:
            # Baixar da Internet
            self.download_word_list()

        # Fechar o jogo caso não existam palavras
        if len(self.word_list) == 0:
            print('Não foi possível obter a lista de palavras')
            exit()

    def get_random_word(self) -> str:
        '''Retorna uma palavra escolhida aleatoriamente da lista'''
        rand = Random()
        i = rand.randint(0, len(self.word_list) - 1)
        return self.word_list[i]

    def download_word_list(self):
        '''Baixa uma lista de palavras da Internet e salva como um JSON'''
        self.word_list = list()

        # Obter o conjunto de palavras da Internet
        try:
            response = requests.get('https://www.dicio.com.br/lista-de-palavras/')
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                for word_list_element in soup.find_all('p', class_='words-list--links'):
                    for word_element in word_list_element.find_all('a'):
                        if word_element.get_text() not in self.word_list:
                            self.word_list.append(word_element.get_text())

                # Salvar como JSON
                json_data = jsonpickle.encode(self.word_list)
                with open(WORD_LIST_PATH, 'w', encoding='UTF-8') as file:
                    file.write(json_data)
        except requests.exceptions.ConnectionError:
            print('ERRO de conexão ao baixar o dicionário!')
