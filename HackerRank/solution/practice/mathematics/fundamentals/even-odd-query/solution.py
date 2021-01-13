#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(A, queries):
    res = []
    for x, y in queries:
        if x < len(A) and x != y and A[x] == 0:
            res.append("Odd")
        else:
            res.append("Even" if A[x-1] % 2 == 0 else "Odd")
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = solve(arr, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
