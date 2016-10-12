#!/usr/bin/python

"""
Pascal's triangle

     1
    1  1
   1  2  1
  1  3  3  1
 1  4  6  4  1

 A function that takes integer n as an argument 
 and returns the nth row of Pascal's triangle
 """

def pascal(n):
    nth_row = []
    for j in range(1, n+1):
        if j == 1:
            nth_row.append(1)
        elif j == n:
            nth_row.append(1)
        else:
            nth_row.append(pascal(n-1)[j-2] + pascal(n-1)[j-1])
    return nth_row

# Next steps: memoisation
