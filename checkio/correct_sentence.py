def correct_sentence(text):
    for i in range(0,len(text)):
        if text[i]==".":
            text=text[0:i]
            break
    return text[0].upper() + text[1:]+"."