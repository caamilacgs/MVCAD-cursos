import csv


def ler_arquivo():
    with open('curso-mvcad.csv', encoding="utf8") as file:
        leitor = csv.DictReader(file, delimiter=',')
        print(leitor)

        lista_pessoa = [item for item in leitor]
        print(lista_pessoa)
        for item in leitor:
            print(item)

ler_arquivo()