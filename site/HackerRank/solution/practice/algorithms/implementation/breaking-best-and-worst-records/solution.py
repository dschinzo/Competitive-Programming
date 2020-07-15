#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    min1 = scores[0]
    max1 = scores[0]
    record = [0, 0]
    for i in scores:
        if i < min1:
            record[1] += 1
            min1 = i
        elif i > max1:
            record[0] += 1
            max1 = i
    return record
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
