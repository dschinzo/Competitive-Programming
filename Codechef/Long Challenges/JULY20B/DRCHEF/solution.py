# cook your dish here
for t in range(int(input())):
    n, x = map(int, input().split())
    A = map(int, input().split())
    B = []
    C = []
    for el in A:
        if el > x:
            B.append(el)
        else:
            C.append(el)
    cnt = len(C)    
    if len(B) == 0:
        print(cnt)
    else:
        if len(C) != 0:
            x = max((max(C)*2), x)
        B.sort()
        for el in B:
            if x >= el:
                cnt += 1
            else:
                while el > x:
                    x += x
                    cnt += 1
                cnt += 1
            x = min(x, el) * 2
        print(cnt)
