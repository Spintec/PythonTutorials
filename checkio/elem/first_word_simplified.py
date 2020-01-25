def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    list = []
    for x in text:
        if x != '\u0020':
            list.append(x)
        else:
            break
    return "".join(list)

    """
        Best solution:
        return text.split(' ')[0]
    """


print(first_word("Hello world"))
