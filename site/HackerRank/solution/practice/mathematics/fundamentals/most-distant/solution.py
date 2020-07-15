alist = []
blist = []
for i in range(int(input())):
    a, b = input().split(' ')
    alist.append(int(a))
    blist.append(int(b))
x1 = min(alist)
x2 = max(alist)
y1 = min(blist)
y2 = max(blist)
print(max(x2 - x1, y2 - y1, (x1**2 + y2**2)**0.5, (x2**2 + y2**2)**0.5,(x2**2 + y1**2)**0.5,(x1**2 + y1**2)**0.5))