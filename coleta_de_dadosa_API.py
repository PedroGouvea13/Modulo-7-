import pprint

def enviar_arquivos():
    #escolher o caminho de upload

    caminho = r'C:\Users\Pedro\Downloads\produtos_informatica.xlsx'

    #Eviar o arquivo
    requisicao = requests.post('https://upload.gofile.io/uploadfile', files={'file': open(caminho, 'rb')})
    saida_requisicao = requisicao.json()

    print(saida_requisicao)
    url = saida_requisicao['data']['downloadPage']
    print("Arquivo enviado. link para acesso.", url)

import requests

def receber_arquivo(file_url):
    #Receber_aquivos
    requisicao = requests.get(file_url)

    #Salvar o Arquivo
    if requisicao.ok:
        with open('arquivo_baixado.xlsx', "wb") as file:
            file.write(requesicao.content)
        print('Arquivo Baixado com sucesso. ' )
    else:
        print("Erro ao baixar o arquivo:",requisicao.json())