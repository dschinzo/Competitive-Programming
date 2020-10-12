for t in range(int(input())):
    n, k = map(int, input().split())
    Q = map(int, input().split())
    d = 0
    res = 0
    for el in Q:
        d += 1   
        el += res
        if el < k:
            break
        else:
            res = el - k
    print(d+el//k)