def escrever_cabecalho(lista_cabecalho):
    with open(nome_arquivo, 'a') as file:
        escritor = csv.DictWriter(file, fieldnames=lista_cabecalho)
        escritor.writeheader()


def escrever_linhas(lista_cabecalho, lista_linhas):
    with open(nome_arquivo, 'a') as file:
        escritor = csv.DictWriter(file, fieldnames=lista_cabecalho)
        escritor.writerows(lista_linhas)
