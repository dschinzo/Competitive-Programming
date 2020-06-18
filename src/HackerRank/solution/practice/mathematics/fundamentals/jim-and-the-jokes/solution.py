#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(dates):
    cnt = {}
    for d in dates:
        if d[0] == 1:
            continue
        for n in str(d[1]):
            if int(n) >= d[0]:
                break
        else:
            num = int(str(d[1]),d[0])
            if num in cnt:
                cnt[num] += 1
            else:
                cnt[num] = 1

    return sum([v*(v-1)//2 for v in cnt.values()])
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    dates = []

    for _ in range(n):
        dates.append(list(map(int, input().rstrip().split())))
    
    result = solve(dates)

    fptr.write(str(result) + '\n')

    fptr.close()
