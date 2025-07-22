#Programa que leia o nome, data de nascimento e carteira de trabalho e cadastre (com a idade) em um dicionário
#verifique se há ou não carteira e com base nisso pedir a data de contratação e o salário e a idade de aposentadoria
from datetime import datetime
import random
data_atual = datetime.now()
cadastro = {"nome":input("Digite o nome: "), "Ano_nasc":int(input("Digite o ano de nascimento: "))}
print(datetime.now())
idade = data_atual.year - cadastro["Ano_nasc"] 
ctps = ""
for c in range(9):
    n = str(random.randint(1,9)) 
    ctps = n + ctps
if idade < 18:
    cadastro["ctps"] = 0
else:
    cadastro["ctps"] = ctps
if cadastro["ctps"] != 0:
    cadastro["Ano_contratacao"] = int(input("Digite o ano da contratação: "))
    while cadastro["Ano_contratacao"] < cadastro["Ano_nasc"] + 18:
        print(f"Periodo de contratação invállido\nO indivíduo era menor de idade, tendo {cadastro["Ano_contratacao"]-cadastro["Ano_nasc"]} anos")
        cadastro["Ano_contratacao"] = int(input("Digite o ano de contratação: "))
    cadastro["salario"] = int(input("Digite salário do funcionário: "))
    cadastro["Aposentadoria"] = cadastro["Ano_contratacao"] - cadastro["Ano_nasc"] + 35

print(cadastro)