#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    if s[-2:] == 'AM':
        if s[:2] == '12':
            return '00' + s[2:len(s)-2]
        else:
            return s[:len(s)-2]
    elif s[-2:] == 'PM':
        if s[:2] == '12':
            return s[:len(s)-2]
        else:
            k = int(s[:2])+12
            return str(k) + s[2:len(s)-2]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
