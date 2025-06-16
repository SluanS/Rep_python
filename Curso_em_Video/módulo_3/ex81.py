#Pertencente a aula #17 - listas (parte 1)
#Programa que cria uma lista que terá inúmeros valores, então deverá ser exibido quantos valores foram inseridos, a lista em ordem decrescente e se o valor 5 foi digitado.
lista = []
while True:
    numero = int(input("Digite o valor a ser isnerido: "))
    lista.append(numero)
    pergunta = input("Deseja continuar?\nN\nOu\nS\n").upper()
    while pergunta not in ("N","S"):
        print("Valor inválido")
        pergunta = input("Deseja continuar?\nN\nOu\nS\n").upper()
    if pergunta == "N":
        break
print(f"Foram inseridos {len(lista)} elementos na lista")
if 5 in lista:
    print("O número 5 está na lista")
else:
    print("O número 5 não aparece na lista")
print(f"Lista em ordem decrescente: {sorted(lista,reverse=True)}")