"""
>>> eh_par(5)
False
>>> eh_par(6)
True
>>> eh_par(0)
True
>>> eh_par(-2)
True
"""
def eh_par(a):
    if a % 2 == 0:
        return True
    else:
        return False
print(eh_par(5))
