from math import log2
f = lambda n: 1 if n%2 else 1 + f(n/2)
 
for _ in range(int(input())):
    w, h, n = map(int, input().split())
    print(['NO', 'YES'][2**(f(w)-1) * 2**(f(h)-1) >= n])