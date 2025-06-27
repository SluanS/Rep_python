#Pertencente a aula #17 - listas (parte 1)
#Programa que receba 5 valores númericos e os insira na lista já na ordem correta
lista = []
numero = int(input("Digite o número a ser inserido: "))
lista.append(numero)
for c in range(4):
    numero = int(input("Digite o número a ser inserido: "))
    if numero > max(lista):
        lista.append(numero)
        print(f"Após o maximo {lista}")
    elif numero < min(lista):
        lista.insert(0,numero)
        print(f"Após o minimo {lista}")
    elif numero in lista:
        lista.insert(lista.index(numero),numero)
        print(f"Após um igual {lista}")
    else:
        indice = []
        valor = []
        for c in range(len(lista)):
            if numero > lista[c]:
                valor.append(lista[c])
        lista.insert(lista.index(max(valor))+1,numero)
        print("Após o else de valores no meio", lista)
print(lista)