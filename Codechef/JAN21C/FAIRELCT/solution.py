#FAIRELCT

for t in range(int(input())):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    sA, sB = sum(A), sum(B)
    if sA > sB:
        print(0)
    else:
        cost = sB - sA
        k = min(n, m)
        A.sort()
        B.sort(reverse=True)
        for i in range(k):
            if A[i] < B[i]:
                cost -= 2*(B[i]-A[i])
                if cost < 0:
                    print(i+1)
                    break
            else:
                print(-1)
                break
        else:
            print(-1)