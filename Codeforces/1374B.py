# 1374B
import sys

I = lambda :int(sys.stdin.buffer.readline())
stpr = lambda x : sys.stdout.write(f'{x}' + '\n')

for t in range(I()):
    n = I()
    two, three = 0, 0
    while n % 2 == 0:
        two += 1
        n //= 2
    while n % 3 == 0:
        three += 1
        n //= 3
    if n == 1:
        if two > three:
            stpr(-1)
        else:
            stpr(2*three-two)
    else:
        stpr(-1)