def correct_sentence(text):
    for i in range(0,len(text)):
        if text[i]==".":
            text=text[0:i]
            break
    return text[0].upper() + text[1:]+"."

print(correct_sentence("greetings, friends"))
print(correct_sentence("Greetings, friends"))
print(correct_sentence("Greetings, friends."))
print(correct_sentence("hi"))
print(correct_sentence("welcome to New York"))
