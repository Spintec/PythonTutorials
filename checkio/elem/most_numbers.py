from decimal import *
getcontext().prec=3
def checkio(*args):
    if args:
        result = Decimal(max(*args)) - Decimal(min(*args))
    else:
        return 0

    return result

print(checkio(1, 2, 3))
print(checkio(5, -5))
print(checkio(10.2, -2.2, 0, 1.1, 0.5))
print(checkio())