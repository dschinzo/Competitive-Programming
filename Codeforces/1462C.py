# 1462C

import sys
I = lambda :int(sys.stdin.buffer.readline())
stpr = lambda x : sys.stdout.write(f'{x}' + '\n')

for t in range(I()):
    n = I()
    if n > 45:
        stpr(-1)
    else:
        res = ''
        i = 9
        while n > 0:
            if n < i:
                res = str(n) + res
            else:
                res = str(i) + res  
            n -= i
            i -= 1
        stpr(res)