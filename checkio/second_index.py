def second_index(text,symbol):
    """
        returns the second index of a symbol in a given text
    """
    # your code here
    if text.count(symbol)<2:
        return None
    pri=text.find(symbol)
    sec=text.find(symbol,pri+1)
    return sec
print(second_index("sims", "s"))