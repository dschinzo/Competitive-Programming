# 263A

import sys
lint = lambda :[int(x) for x in sys.stdin.buffer.readline().split()]
mat = [lint() for i in range(5)]
flag = 0
for i in range(5):
    for j in range(5):
        if mat[i][j] == 1:
            print(abs(2 - j) + abs(2-i))
            flag = 1
            break
    if flag:
        break