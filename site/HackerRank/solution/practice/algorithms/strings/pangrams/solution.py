#!/bin/python3

import math
import os
import random
import re
import sys
from string import ascii_letters
# Complete the pangrams function below.
def pangrams(s):
    d = dict()
    s = s.lower()
    cnt = 0
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] = 1
            cnt += 1
    if cnt == 27:
        return 'pangram'
    else:
        return 'not pangram'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
