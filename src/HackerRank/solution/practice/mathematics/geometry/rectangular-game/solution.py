#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(steps):
    mi = [1000001 , 1000001]
    for i in steps:
        if i[0] < mi[0]:
            mi[0] = i[0]
        if i[1] < mi[1]:
            mi[1] = i[1]
    return mi[0] * mi[1]
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    steps = []

    for _ in range(n):
        steps.append(list(map(int, input().rstrip().split())))

    result = solve(steps)

    fptr.write(str(result) + '\n')

    fptr.close()
