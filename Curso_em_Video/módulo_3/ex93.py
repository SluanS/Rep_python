# Programa que gerencia o aproveitamento de um jogador de futeboll
# O programa lerá o nome do jogador, o número de partidas jogadas por ele, o número de gols em cada partida e guardar os valores fornecidos em um diconário

jogador = {"nome": input("Digite o nome do jogador: "), "n_partidas": int(input("Número de partidas jogadas: "))}

for c in range(jogador["n_partidas"]):
    jogador[f"jogo{c+1}"] = int(input(f"Gols feitos no {c+1}º jogo:"))


for k, v in jogador.items():
    if k == "nome":
        print(f"O aproveitamento do jogador {jogador['nome']}", end=" ")
    if k == "n_partidas":
        print(f"em {jogador['n_partidas']} partidas foi:")
    else:
        print(f"jogo {k[-1]}: {v}")