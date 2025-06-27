#Programa que recebe um dado e exibe na tela seu tipo primitivo
#aula 6
inserir = input("Digite o dado: ")
print(f"O tipo do dado inserido é {type(inserir)}")
print(f"Foram inseridas letras: {inserir.isalpha()}")
print(f"É um número: {inserir.isnumeric()}")
print(f"É consistido apenas por espaços: {inserir.isspace()}")