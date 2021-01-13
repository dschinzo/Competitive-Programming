#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matrixRotation function below.
def matrixRotation(matrix, r, m, n):
    cycle = min(m,n) // 2
    for i in range(cycle):
        lst = []
        for j0 in range(i, m-i):
            lst.append(matrix[j0][i])
        for j1 in range(i+1, n-i):
            lst.append(matrix[m-i-1][j1])
        for j2 in range(m-i-2, i-1, -1):
            lst.append(matrix[j2][n-i-1])
        for j3 in range(n-i-2, i, -1):
            lst.append(matrix[i][j3])
        elm = len(lst)
        s = 0
        for j0 in range(i, m-i):
            matrix[j0][i] = lst[(s - r) % elm]
            s += 1
        for j1 in range(i+1, n-i):
            matrix[m-i-1][j1] = lst[(s - r) % elm]
            s += 1
        for j2 in range(m-i-2, i-1, -1):
            matrix[j2][n-i-1] = lst[(s - r)% elm]
            s += 1
        for j3 in range(n-i-2, i, -1):
            matrix[i][j3] = lst[(s - r) % elm]
            s += 1
    for i in range(m):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print()

        
         

if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r, m, n)
