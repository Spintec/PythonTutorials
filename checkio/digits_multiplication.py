def checkio(number):
    snum=str(number)
    multi=1
    for i in snum:
        i=int(i)
        if i==0:
            continue
        multi = multi * int(i)
    return multi