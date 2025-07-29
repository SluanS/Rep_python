players = []
player = {}

while True:
    question = input("Deseja cadastrar um novo jogador? \nS/N\n")
    while question.lower() not in ("s","n"):
        print("Opção inválida!")
        question = input("Deseja cadastrar um novo jogador? \nS/N")
    if question == "n":
        break
    else:
        player["nome"] = input("Qual o nome do jogador? ")
        player["partidas"] = int(input("Quantas partidas o jogador participou? "))
        player["gols"] = []
        for p in range(player["partidas"]):
            player["gols"].append(int(input(f"Gols feitos na {p+1}ª partida : ")))
            print(player)
        players.append(player)
        player = {}

print(player,"\n", players)
while True:
    question = input("Deseja vizualizar o aproveitamento dos jogadores?\nS/N\n")
    while question.lower() not in ("s","n"):
        print("Opção inválida!")
        question = input("Deseja vizualizar o aproveitamento dos jogadores?\nS/N\n")
    if question == "n":
        break
    elif question == "s":
        for j in range(len(players)):
            for k, v in players[j].items():
                if k == "name":
                    print(f"N.{j+1} - {v}")