x,y,z,q=1,2,3,4


list=[("y",y),("z",z)]
list.append(("x",x))
list[3:]=[("q",q)] #or list[len(list):]=[("q",q)]

#for i in list:
#    print(i)

list2=[]
list2.extend(list) #or list2[len(list2):]=list
#print(list2)
list2.sort(key=lambda list:list[1])
#print(list2)
list2.insert(3,("breaker",0))
list2[len(list2):]=[("re-value",2)]
list2[len(list2):]=[("re-value",1)]
#print(list2)
list2.remove(("x",1)) #or del list2[0]
#print(list2)
#print(list2.pop(0)) #pot sa dau print din cauza ca .pop scoate din lista si returneaza ce a scos
print(list2)
list.clear() # or del list[:]
#for i in list:
#    print(i)
print("Index of value 4 from the list is: ",list2.index(("q",4)))

#for rott in list2:
#    print("Count for values",rott,"is: ",list2.count(rott))
list2.reverse()
print("Reversed list: ",list2)
print("Returned copy of list2: ",list2[:])
print("Same as list2.copy(): ",list2.copy())