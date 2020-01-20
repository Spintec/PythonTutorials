def best_stock(a):
    return list(a.keys())[list(a.values()).index(max(a.values()))]