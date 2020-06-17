#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bigSorting function below.
def bigSorting(unsorted):
    d = {}
    for i in unsorted:
        d.setdefault(len(i), []).append(i)
    lst = list(d.keys())
    lst.sort()
    
    sorted_lst = []

    for i in lst:
        temp_lst = d[i]
        temp_lst.sort()
        for val in temp_lst:
            sorted_lst.append(val)

    print(d, lst, sorted_lst, sep = '\n')

    return sorted_lst

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
