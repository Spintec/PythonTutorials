#list comprehensions in TUPLES
vec=[-4,-2,0,2,4]
print([x*2 for x in vec])

asd=[x for x in vec if x >=0]
print(asd)

print([abs(x) for x in vec])

freshfruit=['banana',' loganberry','passion fruit  ']
fruitz=[zed.strip() for zed in freshfruit]
print(fruitz)

print([(x,x**2) for x in range(6)])

vec=[[1,2,3],[4,5,6],[7,8,9]]
print([num for elem in vec for num in elem])


