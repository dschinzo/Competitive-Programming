# WIPL
# 100 points

import sys
maxx = float('inf')

#------------------------INPUT FUNCTION----------------------------------#
I = lambda :int(sys.stdin.buffer.readline())
tup= lambda : map(int , sys.stdin.buffer.readline().split())
lint = lambda :[int(x) for x in sys.stdin.buffer.readline().split()]
S = lambda: sys.stdin.readline().strip('\n')
grid = lambda  r :[lint() for i in range(r)]
stpr = lambda x : sys.stdout.write(f'{x}' + '\n')
star = lambda x: print(' '.join(map(str, x)))

def rec(A ,B, a ,b ,k):
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] > B[j] and a - A[i] + B[j] >= k :
                x = A[i] - B[j]
                a-=x
                b+=x
                A[i] , B[j] = B[j] , A[i]
            elif A[i] < B[j] and b - B[j] +A[i] >= k :
                x= B[j] - A[i]
                b-=x
                a+=x
                A[i] , B[j] = B[j]  , A[i]
    return a ,b

def solve():
    n , k= tup()
    ls = lint()
    ls.sort(reverse=True)
    A ,B, a ,b =  [] , [] , 0 ,0 
    for i in range(n):
        if a + ls[i] <= k :
            A.append(ls[i])
            a+=ls[i]
        elif b + ls[i] <= k :
            B.append(ls[i])
            b+=ls[i]
        elif a < k:
            A.append(ls[i])
            a+=ls[i]
            a ,b= rec(A, B, a, b, k)
        elif b < k:
            B.append(ls[i])
            b+=ls[i]
            a ,b = rec(A, B, a, b, k)
        else:
            break
    if a>= k and b>=k :
        return len(A) + len(B)
    else:
        return -1

for _ in range(I()):
    print(solve())