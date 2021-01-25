import math
for c in range(1,10001):
    if math.gcd(c+1, 2*c+1) > 1:
        print(c)
    