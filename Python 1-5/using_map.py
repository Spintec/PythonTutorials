#map()

def patrat(s):
    return s**2

rezultat=map(patrat,range(10))
print(list(rezultat))

#using map with lambda

culambda=list(map(lambda x:x**2,range(10)))

print("Cu lambda: ",culambda)

culambdaset=set(map(lambda x:x**2,range(10)))
print("Lambda cu set: ",culambdaset)

print("Nice!")