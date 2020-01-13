def all_the_same(elements) -> bool:
    elements=list(elements)
    print(elements)
    rr=len(elements)
    for i in range(0,rr-1):
        print(i)
        if elements[i]!=elements[i+1]:
            return False

    return True

print(all_the_same(['a','b','a']))