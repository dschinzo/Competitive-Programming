import sys
I = lambda :int(sys.stdin.buffer.readline())
stpr = lambda x : sys.stdout.write(f'{x}' + '\n')
tup= lambda : map(int , sys.stdin.buffer.readline().split())
lint = lambda :[int(x) for x in sys.stdin.buffer.readline().split()]
S = lambda: sys.stdin.readline().strip('\n')
grid = lambda  r :[lint() for i in range(r)]
star = lambda x: print(' '.join(map(str, x)))