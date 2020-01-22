def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    There can be dots and commas in a string.
    A string can start with a letter or, for example, a dot or space.
    A word can contain an apostrophe and it's a part of a word.
    The whole text can be represented with one word and that's it.

    Just saw some magic... not mine though...:
    import re
    return re.findall(r'[a-zA-Z]+', text)

    Finding my own solution...Loading...
    """
    return text.strip(".\ \'\"").translate({ord("."):"\u0020",ord(","):"\u0020"}).split()[0]


print(first_word("Hello world"))
print(first_word(" a word "))
print(first_word("don't touch it"))
print(first_word("greetings, friends"))
print(first_word("... and so on ..."))
print(first_word("hi"))
print(first_word("Hello.World"))