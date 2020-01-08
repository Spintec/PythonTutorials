#dictionary comprehension

RadioX={x:x**2 for x in (2,4,6)}
print(list(RadioX))
for i in RadioX:
    print(RadioX[i],end=" ")