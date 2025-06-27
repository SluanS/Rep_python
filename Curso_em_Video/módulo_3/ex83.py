testes = ["(a+b)",
    "((a+b)*c)",
    "a+(b*(c-d))",
    "((x+y)+(z+w))",
    "(1+2)+(3+(4-5))",
    "()",
    ")",
    "((a+b)",
    "(a+b))",
    "a+b)",
    "((a+b)+(c-d)",
    ")a+(b+c)",
    "((a+b)*(c-d)))",
    "((a+(b-c)) + ((d+e)",
    "(()",
    "(((a+b)"
]

for expressao in testes:
    abrir = 0
    fechar = 0
    print("testando: ",expressao)
    for c in expressao:
                if c == ")" and abrir == 0:
                    fechar += 1
                    break
                if c == "(":
                    abrir += 1
                elif c == ")":
                        fechar+= 1
                if fechar > abrir:
                    break
    if fechar == abrir:
        print("Expressão correta")
    else:
        print("Expressão incorreta!")