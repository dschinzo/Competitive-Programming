#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic):
    lst = []
    for i in range(len(topic)):
        for j in range(i+1, len(topic)):
            lst.append(str(bin(int(topic[i],2)|int(topic[j],2)))[2:])
    cnt = []
    for i in lst:
        cnt.append(i.count('1'))
    m = max(cnt)
    return [m, cnt.count(m)]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
