# cook your dish here
def solve(H, k, n):
    s = sum(H)
    if n == 1 or s < 2*k:
        return -1
    H.sort(reverse=True)
    
    if H[0] >= k:
        for i in range(1, len(H)):
            k -= H[i]
            if k <= 0:
                return i+1
        return -1
    
    A = H.pop(0)
    B = H.pop(0)
    
    print(A, B, H)
    while True:
        if not H: break
        if A < B:
            for i in range(len(H)):
                if A + H[i] < k:
                    A += H.pop(0)
                    break
                if i > 0:
                    A += H.pop(i-1)
                    break
            else:
                A += H.pop(0)
        else:
            for i in range(len(H)):
                if B + H[i] < k:
                    B += H.pop(0)
                    break
                if i > 0:
                    B += H.pop(i-1)
                    break
            else:
                B += H.pop(0)
        print(A, B, H)
        if A >= k and B >= k:
            return n - len(H)
    return -1
                
for t in range(int(input())):
    n, k = map(int, input().split())
    H = list(map(int, input().split()))
    print(solve(H, k, n))