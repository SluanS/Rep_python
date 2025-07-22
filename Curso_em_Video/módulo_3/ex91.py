# Programa onde 4 jogadores joguem um dado e guarde os resultados em um dicionário e no fim organize os valores em ordem e exiba o vencedor
from random import randint
from time import sleep

jogadas = {}

print("-="*10,"JOGANDO DADOS","-="*10)
for c in range(4):
    print("...")
    sleep(1)
    jogadas[f"jogador{c+1}"] = randint(1,6)
    print(f"Jogador{c+1} jogou o dado -> {jogadas[f"jogador{c+1}"]}")

maior = [[0],0]
for k, v in jogadas.items():
    if v > maior[1]:
        maior[0] = [k]
        maior[1] = v
    elif v == maior[1]:
        maior[0].append(k)
ranking = []
dados = sorted(jogadas.values(),reverse=True)

for k, v in jogadas.items():
    ranking.insert(dados.index(jogadas[k]),k)

print("-="*10,"RANKING","-="*10)

for c in range(len(ranking)):
    print(f"{c+1}º-{ranking[c]}")

if len(maior[0]) > 1:
    print("-="*10,"TEMOS UM EMPATE","-="*10)
    print(f"Os jogadores {maior[0]} empataram com o número {maior[1]}")
else:
    print("-="*10,"TEMOS UM VENCEDOR","-="*10)
    print(f"O jogador {maior[0]} venceu com o número {maior[1]}")