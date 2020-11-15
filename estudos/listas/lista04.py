n = int(input("Digite a quantidade de números que deseja processar: "))
maior = -100000
menor = 100000
entrada =map(int, input(f"Digite {n} numeros, separado por virgula: ").split(","))

for atual in entrada:
    menor = min(menor, atual)
    maior = max(maior, atual)

print(f"Maior: {maior}")
print(f"Menor: {menor}")