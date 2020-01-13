#Challenge: verify if a string is an isogram (Ignore letter case)
#Solution 1:
def is_isogram(string):
    return len(string)==len(set(string.lower()))

print(is_isogram("aqqsdef"))

