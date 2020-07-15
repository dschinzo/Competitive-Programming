#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    n = len(arr)
    s1, s2 = 0, 0
    for i in range(n):
        for j in range(n):
            if i == j:
                s1 += arr[i][j]
            if i == n - j - 1:
                s2 += arr[i][j]
    return abs(s1 - s2)
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
