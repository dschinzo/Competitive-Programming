#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    sealevel = 0
    flag = 0
    for i in list(s):
        if i == 'U':
            sealevel += 1
        else:
            sealevel -= 1
        if sealevel == 0 and down == True:
            flag += 1
        elif sealevel < 0:
            down = True
        else:
            down = False

        print(i, sealevel, flag) 
    return flag

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
