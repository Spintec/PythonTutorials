def checkio(data):
    data_dict={}
    for i in data:
        if i not in data_dict:
            data_dict[i]=1
        else:
            data_dict[i]=data_dict[i]+1
    for j in data_dict:
        if data_dict[j]==1:
            data.remove(j)
    return data

print(checkio([1, 2, 3, 1, 3]))
print(list(checkio([1, 2, 3, 4, 5])))
print(list(checkio([5, 5, 5, 5, 5])))
print(list(checkio([10, 9, 10, 10, 9, 8])))