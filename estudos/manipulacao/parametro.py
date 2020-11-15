#consultar parametros do arquivo
arquivo = open('../curso-utf8.csv')
print(arquivo)

#Você pode passar o encoding na hora de abrir o arquivo também
arquivo = open('../curso-mvcad.csv', 'r', encoding='utf-8')
