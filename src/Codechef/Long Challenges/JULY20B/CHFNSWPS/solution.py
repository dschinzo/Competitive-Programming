from collections import Counter
def solve(A, B):
    aShare = []
    bShare = []
    for k in set(A.keys()).union(set(B.keys())):
        if k in A:
            if k not in B:
                if A[k] % 2 == 0:
                    for _ in range(A[k]//2):
                        aShare.append(k)
                else:
                    return -1
            else:
                if (A[k]+B[k])%2==0:
                    if A[k] > B[k]:
                        for _ in range((A[k]-B[k])//2):
                            aShare.append(k)
                    elif B[k] > A[k]:
                        for _ in range((B[k]-A[k])//2):
                            bShare.append(k)
                else:
                    return -1
        else:
            if B[k] % 2 == 0:
                for _ in range(B[k]//2):
                    bShare.append(k)
            else:
                return -1
    guess = min(min(A), min(B))
    aShare.sort()
    bShare.sort(reverse=True)
    cost = 0
    m = len(aShare)
    for i in range(m):
        cost += min(min(aShare[i], bShare[i]), 2 * guess)
    return cost
    
for t in range(int(input())):
    n = input()
    d1 = Counter(map(int, input().split()))
    d2 = Counter(map(int, input().split()))
    print(solve(d1, d2))
