def checkio(str):
    result={}
    for letter in str:
        letter=letter.lower()
        if letter not in result and  letter.isalpha():
            result[letter]=1
        elif letter in result and letter.isalpha():
            result[letter]=result[letter]+1
    n=max(list(result.values()))
    result={k:v for k,v in sorted(result.items(),key=lambda item:item)}
    return (list(result.keys())[list(result.values()).index(n)])


#same as:
#    key_list=list(result.keys())
#    print(result)
#    value_list=list(result.values())
#    print(key_list[value_list.index(2)])
print(checkio("One"))