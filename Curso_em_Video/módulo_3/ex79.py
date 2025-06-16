#Pertencente a aula #17 - listas (parte 1)
#Programa que receba inúmeros valores e os adicione a uma lista sem reptição. Após isso, a lista será exibida em ordem crescente
lista = []
while True:
    number = int(input("Digite o valor a ser inserido: "))
    if number not in lista:
        lista.append(number)
    question = input("Deseja continuar?\nS\nOu\nN\n").upper()
    while question not in ("N","S"):
        print("Escolha inválida!")
        question = input("Deseja continuar?\nS\nOu\nN\n").upper()
    if question == "N":
        break
print(f"Segue lista com valores únicos em ordem crescente: {lista}")