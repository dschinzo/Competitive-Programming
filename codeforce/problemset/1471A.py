# 1471A
import math
for _ in range(int(input())):
    n, x = map(int, input().split())
    A = list(map(int, input().split()))
    print(math.ceil(sum(A) / x), sum(math.ceil(el/x) for el in A))