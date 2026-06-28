# pip install lxml e html5lib para erros do html
#Bs4 modulo e BeautifulSoup é a classe
#pandas tabular formatar dados em tabelas.
import requests
from bs4 import BeautifulSoup
import pandas


response = requests.get('https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/#historico')
print(response.text[:600])

soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify()[:1000])


print('pandas: ') #pip install lxml e html5lib para erros do html
url_dados = pandas.read_html('https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/#historico')
print(url_dados[0].head(10))