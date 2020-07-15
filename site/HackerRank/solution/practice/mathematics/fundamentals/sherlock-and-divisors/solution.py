#!/bin/python3

import os
import sys

#
# Complete the divisors function below.
#
def divisors(n):
    #
    # Write your code here.
    #
    cnt = 0
    i = 2
    while i <= int(n**0.5):
        if n%i==0 and i%2==0: cnt+=1
        if n%(n/i)==0 and (n/i)!=i and (n/i)%2==0: cnt+=1
        i+=1
    if n%2==0: cnt+=1
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = divisors(n)

        fptr.write(str(result) + '\n')

    fptr.close()
