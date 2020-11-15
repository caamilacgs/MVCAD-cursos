#referneciei o arquivo para abrir, Pega as posicoes da planilha separadas por vircula

import csv


def ler_arquivo():
    with open('curso-mvcad.csv', encoding="utf8") as file:
        leitor = csv.DictReader(file, delimiter=',')

        for item in leitor:
            print(item)

        lista_pessoa = [item for item in leitor]
        print(lista_pessoa)



ler_arquivo()