#!/bin/python3

import os
import sys

#
# Complete the strangeGrid function below.
#
def strangeGrid(r, c):
    #
    # Write your code here.
    #
    if r % 2 == 0:
        return (r - 2) * 5 + 2 * c - 1
    else:
        return (r - 1) * 5 + 2 * (c - 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rc = input().split()

    r = int(rc[0])

    c = int(rc[1])

    result = strangeGrid(r, c)

    fptr.write(str(result) + '\n')

    fptr.close()
