def checkio(words):
    count = 0
    for w in words.split():
        if w.isalpha():
            count += 1
        elif w.isdigit():
            count = 0
        if count >= 3:
            return True

    return False

print(checkio("bla bla bla bla"))
print(checkio("He is 123 man"))
print(checkio("one two 3 four five six 7 eight 9 ten eleven 12"))
