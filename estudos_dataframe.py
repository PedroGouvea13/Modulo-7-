import pandas as pd

#Lista: Uma colecao ordenada de elementos que podem ser qualquer tipo
lista_nomes = ['Ana', 'Joao', 'Pedro', 'Paulo']
print('Lista de Nomes: \n', lista_nomes)
print('Primeiro elemento da lista \n', lista_nomes[0])

#Dicionario: Estrutura composta de pares chave-valor
# noinspection PyUnresolvedReferences
dicionario_pessoa = {
    'nome': 'Ana',
    'idade': 20,
    'cidade': 'Sao Paulo'
}
#Lista de dicionario: estrutura de dados que combinam listas e dicionarios
dados = [
    {'nome': 'Ana', 'idade': 20, 'cidade': 'Sao Paulo'},
    {'nome': 'Marcos', 'idade': 25, 'cidade': 'Rio de Janeiro'},
    {'nome': 'Mauro', 'idade': 63, 'cidade': 'Petropolis'}
]

#Dataframe: estruturas de dados bidimencional

df = pd.DataFrame(dados)

print('DataFrame \n', df)
