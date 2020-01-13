'''
You are given an array (which will have a length of at least 3, but could be very large) containing integers.
The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N.
Write a method that takes the array as an argument and returns this "outlier" N.
'''

def find_outlier(integers):
    odd=0
    even=0
    for i,j in enumerate(integers):
        while even==odd:
            if (integers[i]%2==0):
                even=even+1
            else:
                odd=odd+1
        if




find_outlier([1,2,10,4,3])
