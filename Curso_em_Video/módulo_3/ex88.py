#Programa que ajuda um jogador com palpites para a mega sena
#Pede o número de jogos e sorteará 6 números

import random
import time
print("-"*30)
print("     JOGO DA MEGA SENA")

quantidade_jogos = int(input("Quantos jogos deseja gerar? "))
jogos = []
for c in range(quantidade_jogos):
    grupo = []
    for n in range(6):
        numero = random.randint(1,60)
        while numero in grupo:
            numero = random.randint(1,60)
        grupo.append(numero)
    jogos.append(grupo)
print('-='*3,f"SORTEANDO {quantidade_jogos} jogo(s)",'-='*3)
for c in range(len(jogos)):
    time.sleep(2)
    print(f"jogo {c+1}:",jogos[c])