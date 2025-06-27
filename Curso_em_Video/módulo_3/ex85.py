#programa que receba 7 valores númericos e os divida os valores pares e impares em sublistas
#Exercício pertencenten a aula 17 parte 2
lista = [[],[]]
for c in range(7):
    valor = int(input("Digite um número: "))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
    

print(f"Valores pares inseridos {sorted(lista[0])}, valores impares {sorted(lista[1])}")