lst = [[],[]]
n = int(input())
for i in range(n):
    x, y = input().split(' ')
    lst[0].append(int(x))
    lst[1].append(int(y))
def isTrue(a, b):
    for i in range(1,len(a)):
        if a[0] != a[i] and b[0] != b[i]:
            return 'NO'
    return 'YES'

print(isTrue(lst[0], lst[1]))
