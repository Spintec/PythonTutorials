def incrementor(n):
    return lambda x: x+n

print(incrementor(0))
f=incrementor(1)
print(f(0))
print(f(1))

#Use lambda to pass a small function as an argument

thelist=[(1,'one'),(2,'two'),(3,'three'),(4,'four')]
#sort it by it's second argument
thelist.sort(key=lambda e:e[1])
print(thelist)