#Cadastro de pesos
#Código que registre pesos de várias pessoas em uma lista e exiba quantas pessoas foram cadastradas, quem são as pessoas mais pesadas e
# quem são as pessoas mais leves

registros = []
media = []
while True:
    novo_registro = [input("Digite o nome da pessoa: "), float(input("Agora digite seu peso: "))]
    registros.append(novo_registro)
    media.append(novo_registro[-1])
    question = input("Deseja continuar a cadastrar?\nS\nN\n")
    while question.upper() not in ["N","S"]:
        question = input(f"Inválido!\nDeseja continuar a cadastrar?\nS\nN\n")
    if question.upper() == "N":
        break
print(f"{len(registros)} registro(wfeito(s) com sucesso")
maior = 0
menor = 0
for r in registros:
    if r[1] > maior:
        maior = r[1]
    elif r[1] < menor - 10:
        menor = r[1]
print(f"O individuo cadastrado com maior peso foi: {maior}")
print(f"Os individuos cadastrados com o menor peso foir: {menor}")