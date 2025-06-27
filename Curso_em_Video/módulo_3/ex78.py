#Pertencente a aula #17 - listas (parte 1)
#Programa que lê 5 valores númericos e os guarde em uma lista, após isso, exibir qual foi o maior e o menor valore inserido.
values = []
for c in range(5):
    numero = int(input("Digite o valor a ser inserido: "))
    values.append(numero)
print(f"O maior valor inserido foi {max(values)}, na posição {values.index(max(values))}\nO menor valor inserido foi {min(values)} na posição {values.index(min(values))}")