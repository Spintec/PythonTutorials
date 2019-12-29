basket={'apple':'mar','orange':'portocala','banana':'banana','kiwi':"kiwi"} #
tramp=set('You\'re a tramp')

print('orange' in basket) #returneaza True pentru ca se afla in lista
print('crabgrass' in basket)  #sets folosesc sa verifici daca ai abonament la sala, sa scoti date duplicate, etc

#Demonstrate set operations on unique letters from two words

a=set('abracadabra')
b=set('alacazam')
#print dintr-un set printeaza caracterele unice din acel set
print(a)
print(b)
print(a-b)  #compara a cu b si returneaza caracterele unice pentru a
print(b-a)  #invers: returneaza caracterele unice din b dupa compararea cu iteme din a
print(a|b)  #printeaza toate caracterele din ambele seturi
print(a&b)  #printeaza caracterele comune din a si b
print(a^b)  #printeaza toate caracterele care nu sunt comune seturilor

#Set comprehensions

print({x for x in 'abracadabra' if x not in 'abc'})  #printeaza caracterele din abracadabra in afara de 'abc'
print({x for x in 'abracadabra' if x in 'abz'})      #printeaza caracterele 'abc' daca se gasesc in set

