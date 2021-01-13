#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dynamicArray function below.
def dynamicArray(n, queries):
    seqList = []
    result = []
    for i in range(n):
        seqList.append([])
    lastAns = 0
    for i in queries:
        q_type = i[0]
        q_x = i[1]
        q_y = i[2]
        if q_type == 1:
            seqList[(q_x ^ lastAns) % n].append(q_y)
        else:
            seq = seqList[(q_x ^ lastAns) % n]
            lastAns = seq[q_y % len(seq)]
            result.append(lastAns)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().rstrip().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
