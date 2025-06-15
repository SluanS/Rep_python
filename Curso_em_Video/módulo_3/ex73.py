#Ex 73 (adaptado) pertencente a aula 16 
#Dedicado a interação com tuplas extensas
#Finalidade: Exibir os primeiros 5 colocados de uma classificação de campeonato, os ultimos 4 colocados, a listagem do
#campeonato em ordem alfabética e exibir o em que posição um elememento especifíco se encontra.

Pokemon = ("Pikachu", "Squirtle", "Popplio", "Fomantis", "Lapras", "Ampharos", "Sylveon",
    "Fennekin", "Mr. Mime", "Froakie", "Dragonite", "Snivy", "Vaporeon", "Bulbasaur",
    "Geodude", "Charmander", "Chimchar", "Piplup", "Turtwig", "Torchic", "Ralts"
)
print("Os primeiro cinco pokemon classificados foram: ")
print(Pokemon[:5])

print("Os ultimos 4 colocados foram: ")
print(Pokemon[-4:])

print("Lista completa em ordem alfabética: ")
for a in sorted(Pokemon):
    print(a)

# Informa a posição de um Pokémon específico
print(f"O favorito do publico Lapras está na posição {Pokemon.index('Lapras')+1}")