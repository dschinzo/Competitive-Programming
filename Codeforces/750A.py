# 750A
n, k = map(int, input().split())
pos = 240 - k
solved = 0
while pos >= 5 and solved < n:
    solved += 1
    pos -= solved*5
    if pos < 0:
        solved -= 1
        break
print(solved)
    