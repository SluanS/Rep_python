#Cria uma matriz de dimensão 3X3 e insira valores nessa matriz
#exibir a soma de todos os valores pares digitados
#exibir a soma dos valores da terceira coluna
#o valor da segunda linha
matriz = [[],[],[]]
for c in range(9):
    numeros = int(input("Digite um número: "))
    
    for index, line in enumerate(matriz):
         if len(line) < 3:
            matriz[index].append(numeros)
            break
soma_pares = 0
soma_ter_col = 0
print("Matriz: ")
for lista in matriz:
    for index, valores in enumerate(lista):
        if valores % 2 == 0:
            soma_pares += valores
        if index < 2:
            print(f'{valores:<6}',end="|")
        elif index == 2:
            print(valores,"\n")
            print('-'*16)
        if index == 2:
            soma_ter_col += valores
print(f"A soma de todos os números pares foi {soma_pares}")
print(f"A soma dos valores da terceira coluna foi {soma_ter_col}")
print(f"O maior valor da segunda linha é {max(matriz[1])}")
