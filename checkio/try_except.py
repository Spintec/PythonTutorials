
def index_power(array, n):

    try: return array[n] ** n

    except IndexError: return -1

print(index_power([1,2,3,4,5,6],2))