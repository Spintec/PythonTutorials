'''
It is sometimes tempting to change a list while iterating over it,
however it is much safer and simpler to create a new one instead
'''
#math.isnan() method
import math
raw_data=[56.2,float('NaN'),51.7,55.3,52.5,float('NaN'),47.8]
filtered_data=[]
for v in raw_data:
    if not math.isnan(v):
        filtered_data.append(v)

print(filtered_data)