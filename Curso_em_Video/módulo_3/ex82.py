#Trabalhando com listas
#Esse código cria uma lista de valores númericos e os separa entre duas outras listas, classificando-os entre valores pares e impares
general_list = []
even_list = []
odd_list = []
while True:
    try:
        number = int(input("Digite o valor a ser inserido na lista: "))
        general_list.append(number)
        question = input("Deseja inserir mais valores? Digite:\nS - para continuar\nou\nN - para encerrar\n").upper()
        while question not in ("S","N"):
            print("Escolha inválida!")
            question = input("Digite: \nS - para continuar\nou\nN - para encerrar\n").upper()
        if question == "N":
            break
    except ValueError:
        print("Digite um valor válido!")
for c in general_list:
    if c % 2 != 0:
        odd_list.append(c)
    else:
        even_list.append(c)
print(f"Lista completa de números inseridos {general_list}\nLista de números impares: {odd_list}\nLista de números pares: {even_list}")