"""
>>> e_par(5)
False
>>> e_par(6)
True
>>> e_par(0)
True
>>> e_par(-2)
True
"""
def e_par(a):
    if a % 2 == 0:
        return True
    else:
        return False
print(e_par(5))
