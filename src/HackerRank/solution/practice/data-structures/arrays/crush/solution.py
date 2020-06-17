#!/bin/python3

import os
from itertools import accumulate

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    res = [0]*(n+1)
    for a, b, k in queries:
        res[a] += k
        if b+1 <= n:
            res[b+1] -= k
    return max(accumulate(res)) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
