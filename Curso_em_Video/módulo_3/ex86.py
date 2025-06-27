#Cria uma matriz de dimensão 3X3 e insira valores nessa matriz
matriz = [[],[],[]]
for c in range(9):
    numeros = int(input("Digite um número: "))
    
    for index, line in enumerate(matriz):
         if len(line) < 3:
            matriz[index].append(numeros)
            break

print("Matriz: ")
for lista in matriz:
    for index, valores in enumerate(lista):
        if index < 2:
            print(f'{valores:<6}',end="|")
        elif index == 2:
            print(valores,"\n")
            print('-'*16)