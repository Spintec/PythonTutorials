#reversed() function

for i in reversed(range(0,12,2)):
    print(i)

#sorted() function looping
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(basket):
    print(f)
#sau pot folosi set() ca sa nu se repete itemele
for f in sorted(set(basket)):
    print(f,end=" ")