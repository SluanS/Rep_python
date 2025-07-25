# programa que leia nome, sexo e idade de várias pessoas e guarde-os em um dicionário cada
# após isso, os dicionários deverão ser alocados dentro de uma lista
# Ao fim o programa deve exibir quantas pessaos foram cadastradas, a média de idade entre os cadastrados, listar todas as pessoas do sexo feminino e
# uma lista com todas as pessoas com idade acima da média

usuarios = []
idade = []

while True:
    question = input("Deseja cadastrar um novo usuário?\nS/N ").lower()
    while question not in ("s","n"):
        print("Resposta inválida!")
        question = input("Deseja cadastrar um novo usuário?\nS/N ").lower()
    if question == "n":
        break
    else:
        new_user = {"user_name":input("Digite o nome do usuário: "),
                    "user_age":int(input("Digite a idade do usuário: ")),
                    "user_gender": input("genero:\nM\nF\n").lower()}
        while new_user["user_gender"] not in ["m","f"]:
            print("Genero iválido!")
            new_user["user_gender"] = input("genero:\nM\nF\n")
        usuarios.append(new_user)
        idade.append(new_user["user_age"])

media_idade = int(sum(idade) / len(idade))
print(usuarios)
print(f"No total foram cadastrados {len(usuarios)} novos usuários")
print(f"A média de idade entre os usuários cadastrados foi de {media_idade}")

print("Usuários do sexo feminino: ")
for u in usuarios:
    if u["user_gender"] == "f":
        print(f"User name: {u["user_name"]}\n Age: {u["user_age"]}\n Gender: {u["user_gender"]}")

print(f"Os usuários cadastrados com idade acima da média {media_idade} foram: ")
for u in usuarios:
    if u["user_age"] > media_idade:
        print(f"User name: {u["user_name"]}\n Age: {u["user_age"]}\n Gender: {u["user_gender"]}")