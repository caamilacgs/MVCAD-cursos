quantidade = int(input("Quantos números você quer escolher? "))

index = 0
lista = []
while (index < quantidade):
    proximo = int(input("Digite o proximo número: "))
    index += 1
    lista.append(proximo)
lista.sort()
n = len(lista)
ultimo = n - 1
print(lista)
print(f"Menor: {lista[0]} , Maior: {lista[ultimo]} ")