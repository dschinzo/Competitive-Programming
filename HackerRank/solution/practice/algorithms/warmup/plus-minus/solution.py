#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    cnt = [0, 0, 0]
    for i in arr:
        if i > 0:
            cnt[0] += 1
        elif i < 0:
            cnt[1] += 1
        elif i == 0:
            cnt[2] += 1
    for i in cnt:
        print('{:.6f}'.format(i / len(arr)))
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
