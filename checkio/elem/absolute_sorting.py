def checkio(numbers_array):
    numbers_array = sorted(numbers_array, key=lambda x: abs(x))
    return numbers_array


print(checkio((-20, -5, 10, 15)))
