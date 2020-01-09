#items() function
knights= {'Jesus':'The Saviour','Mary':"The Alleged Virgin"}

for k,v in knights.items():
    print(k,v)
#enumerate() function
seq=[('tic'),('tac'),('toe')]

for i,n in enumerate(seq):
    print(i,n)

#zip() function
questions=['problem','favourite color','middle name']
answers=['You!','Black intertwined with Red','Dell']

for k,v in zip(questions,answers):
    print("What is your",k,"?",v)

#Cu format() function iese mai elegant
for q,a in zip(questions,answers):
    print("What is your {0}? {1}".format(q,a))