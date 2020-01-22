def best_stock(a):
    return list(a.keys())[list(a.values()).index(max(a.values()))]

print(best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}))
print(best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}))