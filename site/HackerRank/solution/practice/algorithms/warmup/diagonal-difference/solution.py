#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    n = len(arr)
    s = 0
    for i in range(n//2):
        s += arr[i][i] + arr[n-i-1][n-i-1] - arr[i][n-i-1]-arr[n-i-1][i]
    return abs(s)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
