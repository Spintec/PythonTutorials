def checkio(str):
    result={}
    for letter in str:
        letter=letter.lower()
        if letter not in result and (letter.isdigit() or letter.isalpha()):
            result[letter]=1
        elif letter in result and (letter.isdigit() or letter.isalpha()):
            result[letter]=result[letter]+1
    keyz=(list(result.keys()))
    keyz.sort()
    print(keyz)
    n=max(list(result.values()))

    return (list(result.keys())[list(result.values()).index(n)])

# MAI RAMANE SA SORTEZ ALFABETIC!!!!!!!! pentru ca strine 'One' sa returneze 'e' in loc de 'o'

#same as:
#    key_list=list(result.keys())
#    print(result)
#    value_list=list(result.values())
#    print(key_list[value_list.index(2)])
print(checkio("One"))