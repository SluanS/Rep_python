def divisao(a,b):
    if b == 0:
        try:
            a / b
        except ZeroDivisionError:
            return "Dividendo não pode ser igual a zero"

    else:
        return a / b
    
print(divisao(1,0))