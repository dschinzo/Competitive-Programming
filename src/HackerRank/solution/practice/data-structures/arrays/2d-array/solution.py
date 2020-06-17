#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    n = len(arr)
    lst = []
    for i in range(1,n-1):
        for j in range(1,n-1):
            lst.append(arr[i][j] + sum(arr[i-1][j-1:j+2]) + sum(arr[i+1][j-1:j+2]))
    return max(lst)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
