def checkio(*args):
    if args:
        result=max(args)-min(args)
        result=round(result,3)
        return result
    else:
        return 0

print(checkio(1, 2, 3))
print(checkio(5, -5))
print(checkio(10.2, -2.2, 0, 1.1, 0.5))
print(checkio())