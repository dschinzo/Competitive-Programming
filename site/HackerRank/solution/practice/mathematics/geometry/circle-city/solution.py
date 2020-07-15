#!/bin/python3
import os
import sys
import math

# Complete the solve function below.
def solve(d, k):
    while d % 2 == 0:
        d = d//2
    
    i = 3
    p = 4
    while d > 1:
        q = 1
        w = 0
        while d % i == 0:
            if i % 4 == 1:
                q += 1  
            if i % 4 == 3:
                w += 1
            d = d // i

        if w % 2 == 1:
            return "possible"
        if i > 10 ** 5:
            if d % 4 == 1:
                p *= 2
                break
            else:
                return "possible"
        p *= q
        i += 2
    if p <= k:
        return "possible"
    else:
        return "impossible" 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        dk = input().split()

        d = int(dk[0])

        k = int(dk[1])

        result = solve(d, k)

        fptr.write(result + '\n')

    fptr.close()
