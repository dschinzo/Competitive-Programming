for _ in range(int(input())):
    n = int(input())
    if n % 2:
        for i in range(1, n**2+1, n):
            print(*range(i, i+n))
    else:
        for i in range(1, n**2+1, 2*n):
            print(*range(i, i+n))
            print(*[str(el[0])+' '+str(el[1]) for el in zip(range(i+n+1, i+2*n, 2), range(i+n, i+2*n, 2))])
