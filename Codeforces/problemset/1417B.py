# 1417B
for _ in range(int(input())):
    n = input()
    lst = list(map(int, input().split()))
    odd = lst.count(1)
    even = lst.count(2)

    if n == 1 or odd % 2 == 1:
        print("NO")
    elif even % 2 == 0 or odd > 1:
        print("YES")
    else:
        print("NO")