#List comprehensions

squares=[]
for s in range(10):
    squares.append(s**2)

print(squares)

lelist=[(x,y) for x in [1,2,3] for y in [1,2,3]]
print(lelist)

lelist2=[(x,y) for x in [1,2,3] for y in [1,2,3] if x!=y] #if x!=y daca x diferit de y, combina listele
print(lelist2)

#echivalent cu:
combs=[]
for x in [1,2,3]:
    for y in [1,2,3]:
        if x!=y:
            combs.append((x,y))  #daca nu pun 2 paranteze, combs.append crede ca ii dau 2 argumente.
print(combs)

