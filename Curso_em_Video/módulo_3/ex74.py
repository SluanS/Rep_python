#Ex 74 pertencente a aula 16
#Finalidade: Sortear cinco valores, exibir a lista dos valores sorteados e o menor e maior valor.

import random
n1 = random.randint(0,100)
n2 = random.randint(0,100)
n3 = random.randint(0,100)
n4 = random.randint(0,100)
n5 = random.randint(0,100)



t = (n1,n2,n3,n4,n5)

print(f"Lista de números aleatorios {t}, sendo o {sorted(t)[-1]} o maior e {sorted(t)[0]} o menor")