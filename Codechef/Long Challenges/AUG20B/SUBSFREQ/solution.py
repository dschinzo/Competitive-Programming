from collections import Counter
for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    res = [0]*(N+1)
    frq = Counter(A)
    for k in frq:
        res[k] = frq[k]
    #res[min(frq)] += 1
    nums = list(frq.keys())
    nums.sort()
    s = N - 1
    for k in nums:
        print(s, nums, k, ((2*s-frq[k]+1)/2)*frq[k])
        res[k] += int(((2*s-frq[k]+1)/2)*frq[k])
        s -= frq[k]
    for k in nums:
        if frq[k] == 1:
            cnt = 0
            for o in nums:
                if o > k:
                    cnt += 1
            res[k] = int((cnt*(cnt+1))/2)
        else:
            i = 1
            cum = 0
            while i < frq[k]:
                cum += i * (N - 1 - i)
                i += 1
            res[k] += cum
    print(" ".join(map(str, res[1:])))
