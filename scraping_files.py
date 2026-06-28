import requests
from bs4 import BeautifulSoup
import pandas as pd

requests.packages.urllib3.disable_warnings()

url = 'https://books.toscrape.com/'
requisicao = requests.get(url)

# Criação da extração do conteúdo HTML com BeautifulSoup
extracao = BeautifulSoup(requisicao.text, 'html.parser')

catalogo = []

# --- Parte 1 ---

# Encontra todos os artigos de produtos (livros) na página
artigos = extracao.find_all('article', class_='product_pod')

for artigo in artigos:
    # Dicionário padrão para o livro atual
    livro = {'Título': '', 'Preço': ''}

    # 1. Cria um for para encontrar a tag <h3> dentro da tag <article>
    tags_h3 = artigo.find_all('h3')
    for h3 in tags_h3:
        # Extrai o texto da tag <h3> (com os "...")
        titulo = h3.get_text(strip=True)
        # Atualiza o valor de livro['Título']
        livro['Título'] = titulo

    # 2. Cria outro for para encontrar a tag <p class='price_color'> com find_all
    tags_preco = artigo.find_all('p', class_='price_color')
    for p in tags_preco:
        # Extrai o texto e remove o caractere 'Â' caso ele apareça por problemas de encoding
        preco = p.get_text(strip=True).replace('Â', '')
        # Atualiza o valor de livro['Preço']
        livro['Preço'] = preco

    # Os livros devem ser adicionados na lista catalogo
    catalogo.append(livro)

# --- Parte 2 ---

# Armazene a quantidade de livros na variável contar_livros
contar_livros = len(catalogo)

# Formata as saídas exatamente como o corretor espera ler no terminal
lista_titulos = [l['Título'] for l in catalogo]
lista_precos = [l['Preço'] for l in catalogo]

print(lista_titulos)
print(lista_precos)
print(f"contar_livros = {contar_livros}")