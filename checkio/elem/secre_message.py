def find_message(text):
    upper_string =""
    for i,j in enumerate(text):
        if j.isupper()==True:
            upper_string=upper_string+text[i]
    return upper_string