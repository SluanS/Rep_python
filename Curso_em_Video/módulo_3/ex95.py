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
        players.append(player)
        player = {}


while True:
    question = input("Deseja vizualizar o aproveitamento dos jogadores?\nS/N\n")
    while question.lower() not in ("s","n"):
        print("Opção inválida!")
        question = input("Deseja vizualizar o aproveitamento dos jogadores?\nS/N\n")
    if question.lower() == "s":
            for j in range(len(players)):
                    for k, v in players[j].items():
                        if k == "nome":
                            print(f"N.{j+1} - {v}")
            question = int(input("Digite o ID do jogador desejado: "))
            while question > len(players) or question < 0:
                print("Opção inválida!")
                question = int(input("Digite o ID do jogador desejado: "))
            print(f"Segue aproveitamento do jogador {players[question-1]['nome']}: ")
            for g in range(players[question-1]['partidas']):
                print(f"jogo {g+1}º - {players[question-1]["gols"][g]}")
                                 
                                
                                

                                
    elif question.lower() == "n":
        break