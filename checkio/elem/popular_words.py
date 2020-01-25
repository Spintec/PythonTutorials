def popular_words(text: str, words: list) -> dict:
    dictz = {x: 0 for x in words}
    text = text.lower()
    for word in text.split():
        if word in dictz:
            dictz[word] = dictz[word] + 1
    return dictz


print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))