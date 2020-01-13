def checkio(str):
    return (any(x.isupper() for x in str) and any(x.islower() for x in str) and any(x.isdigit() for x in str) and len(str)>=10)

print(checkio("Asd3qwerty"))