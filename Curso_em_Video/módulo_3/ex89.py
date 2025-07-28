#Código que lê nomes e duas notas e os guarde em uma lista composta, após exiba um boletim da média considerando as notas inseridas
#e permitir exibir as notas de cada nome individualmente
lista = []
while True:
    nome = input("Digite o nome do aluno: ")
    lista.append([nome])
    for c in range(2):
        nota = float(input(f"Digite a {c+1}ª nota do aluno: "))
        lista[-1].append(nota)
    question = input("Deseja continuar?\nS\nN\n")
    while question.upper() not in ("S","N"):
        question = input("Tente novamente\nDeseja continuar?\nS\nN\n")
    if question.upper() == "N":
        break
for c in lista:
    notas = []
    for a in c:
        if type(a) == float:
            notas.append(a)
    media = sum(notas) / len(notas)
    print("-"*30)
    print(f"O aluno {c[0]} teve a média de {media}")
    
print(f"Deseja ver o boletim completo de um dos alunos?")
question = input("S\nN\n")
while question.upper() not in ("S","N"):
        question = input("Tente novamente\nDeseja continuar?\nS\nN\n")
if question.upper() == "S":
    print("Escolha o aluno: ")
    for i, a in enumerate(lista):
        print(f"id.{i+1}|{a[0]}")
    question = int(input("Digite o id do aluno desejado: "))
    while question > len(lista):
        question = int(input("id iválido!\nDigite o id do aluno desejado: "))
    print(f"Nome{'':<6}nota1{'':<6}nota2")
    escolhido = lista[question-1]
    print(f"{escolhido[0]:<6}{"":<6}{escolhido[1]}{"":<6}{escolhido[2]}")
