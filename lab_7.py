import requests
from bs4 import BeautifulSoup
import pandas as pd
requests.packages.urllib3.disable_warnings()

url = 'https://books.toscrape.com/'
requisicao = requests.get(url)

# Criação da extração do conteúdo HTML com BeautifulSoup
extracao = BeautifulSoup(requisicao.text, 'html.parser')

# Imprime os primeiros 2000 caracteres do HTML bruto
print(requisicao.text[:2000])

# Imprime o HTML formatado com prettify()
print(extracao.prettify())