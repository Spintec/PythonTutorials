#Challenge: Revert a given string
#def spin_words(sentence):
#    sentence=input("Enter String: ")
#    sentence="".join(list(reversed(sentence)))
#    return sentence

#print(spin_words(""))

def spin_words(sentence):
    # Your code goes here
    sentence="".join(list(reversed(sentence)))
    return sentence
print(spin_words("ot"))