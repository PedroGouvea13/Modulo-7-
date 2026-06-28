import requests
from bs4 import BeautifulSoup

url = 'https://python.org.br/web/'
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text, 'html.parser')

#Exibir Texto
print(extracao.text.strip())

Filtrar a exibicao pela tag
for linha_texto in extracao.find_all('h2'):
    titulo = linha_texto.text.strip()
    print('Titulo: ', titulo )

#Quantidade de titulos e paragrafos
contar_titulos = 0
contar_paragrafos = 0

for linha_texto in extracao.find_all(['h2', 'p']):
    if linha_texto.name == 'h2':
        contar_titulos += 1 #Contar_titulos_maior_igual_a_1
    elif linha_texto.name == 'p':
        contar_paragrafos += 1

print('Total de titulos ' , contar_titulos)
print('total de paragrafos ', contar_paragrafos)

#Exibir somente os textos das tags h2 e p
for linha_texto in extracao.find.all(['h2', 'p']):
    if linha_texto.name == 'h2':
        titulo == linha_texto.text.strip()
        print('Titulo: \n', titulo)
    elif linha_texto.name == 'p':
        paragrafo = linha_texto.text.strip()
        print('Paragrafo: \n', paragrafo)

#