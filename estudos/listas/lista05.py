presentes = int(input("Quantas pessoas são presentes? "))
pessoas = []
for i in range(presentes):
    pessoas.append(input("Digite o nome do participante: "))
pessoas.sort()
print("Partipantes por ondem alfabetica: ")
print("\n".join(pessoas))
