def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def max_unique_primes(n):
    if n < 2:
        return 0
    prod = 2
    cnt = 1
    prim = 3
    while prod * prim <= n:
        if gcd(prod, prim) == 1:
            prod *= prim
            cnt += 1
        prim += 2
    return cnt
for i in range(int(input())):
    n = int(input())
    print(max_unique_primes(n))