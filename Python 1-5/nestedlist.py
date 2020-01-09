#nested list comprehensions
matrix=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]
x=0
print([row for row in matrix])

#f1
print([[row[i] for row in matrix] for i in range(4)])

#f1 echivalent cu:

transposed=[]
for i in range(4):
    transposed.append([row[i] for row in matrix])

#care este echivalent cu:

for i in range(4):
    #urmatoarele 3 linii implementeaza nested listcomprehension
    transposed_row=[]
    for row in matrix:
        transposed_row.append(row[i])
    transposedz.append(transposed_row)
print(transposedz)

print(transposed)
