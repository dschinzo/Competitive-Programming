#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    d = {}
    for i in range(1,n+1):
        if n % i == 0:
            if i not in d:
                d[i] = sum(map(int,list(str(i))))
    mx = max(d.values())
    mn = 10 ** 5
    for i in d:
        if d[i] == mx: 
            if mn > i:
                mn = i
    print(d[mx] if mn == 10 ** 5 else mn)
