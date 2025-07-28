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
print(f"{len(registros)} registro(s) feito(s) com sucesso")
maior = [0]
menor = [0]

for r in registros:
    if r[1] > maior[-1]:
        maior = [r[0],r[1]]
    elif r[1] < menor[-1] or menor[-1] == 0:
        menor = [r[0],r[1]]
        print({menor[-1]})
print(f"O individuo cadastrado com maior peso foi: {maior[0]}")
print(f"Os individuos cadastrados com o menor peso foir: {menor[0]}")