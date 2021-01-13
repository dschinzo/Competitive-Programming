#!/bin/python3

import os
import sys
from math import gcd

# Complete the solve function below.
def solve(a, b, c):
    if a + b <= c:
        return '1/1'
    s = 2*a*b
    if max(a,b) <= c:
        n = s-(a-c+b)**2
        d = gcd(n, s)
        return f'{n//d}/{s//d}'
    if min(a,b) >= c:
        n = c ** 2
        d = gcd(n, s)
        return f'{n//d}/{s//d}'
    if a < b:
        a, b = b, a 
    n = c**2-(c-b)**2
    d = gcd(n, s)
    return f'{n//d}/{s//d}'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    for n_itr in range(n):
        abc = input().split()

        a = int(abc[0])

        b = int(abc[1])

        c = int(abc[2])

        result = solve(a, b, c)

        fptr.write(result + '\n')

    fptr.close()
