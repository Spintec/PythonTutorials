#Dictionary operations
dick={"Car":"Ford",
      "Age":21,
      "Sex":"Male",
      }
#print(list(dick))
#for i in dick:
#    print(dick[i])
tel={'Jack':4098,'Sape':'4139'}
tel['New']=4127
del tel['Sape']
tel['irv']=4127
print(sorted(tel))
print('Jack' in tel)
print('jack' in tel)
print('Jack' not in tel)
#exista functia dic() cu care pot construi dictionar
newdick=dict([("Car","Ford"),("Age",21),("Sex","Male")])
