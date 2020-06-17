#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    lst = p.copy()
    
    for i in range(len(p)):
        lst[p[i]-1] = i + 1
    ret = []
    for val in lst:
        for j in range(len(p)):
            if val == p[j]:
                ret.append(j + 1)
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
