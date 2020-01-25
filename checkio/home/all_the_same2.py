def all_the_same2(elements):
 #   elements=list(elements)
    return len(set(elements)) <=1

print(all_the_same2(['a','a','a','b','b']))
