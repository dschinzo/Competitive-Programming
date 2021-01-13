# 1468N
for _ in range(int(input())):
    c = list(map(int, input().split()))
    a = list(map(int, input().split()))
    if c[0] >= a[0] and c[1] >= a[1] and c[2] >= a[2]:
        c = [c[i] - a[i] for i in range(3)]
        a[3] -= c[0]
        a[4] -= c[1]
        if max(0,a[3]) + max(0,a[4]) <= c[2]:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
        