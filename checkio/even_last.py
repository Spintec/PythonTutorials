def checkio(array):
    multi=0
    for i,j in enumerate(array):
        if i%2==0:
            multi=multi+j
    if array==[]:
        return 0
    else:
        return multi*array[-1]