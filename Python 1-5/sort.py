#Need to sort out "sort" to understand lambda expression.py


def sortFunc(arg):
    return arg[1]

thelist=[(1,'one'),(2,'two'),(3,'three'),(4,'four')]

thelist.sort(key=sortFunc)
print(thelist)