from collections import Counter
with open("testcase3.txt") as f:
    for _ in range(int(f.readline())):
        N, K = map(int, f.readline().split())
        F = list(map(int, f.readline().split()))    
        arr = [[]]
        for el in F:
            if el not in arr[-1]:
                arr[-1].append(el)
            else:
                arr.append([el])
        if K == 1:
            print(len(arr))
        else:
            n = len(arr)
            no_dup = []
            for i in range(n):
                d = Counter(arr[i])
                no_dup.append([0]*n)
                for j in range(i+1, n):
                    no_dup[i][j] = no_dup[i][j-1]
                    for k in arr[j]:
                        if k in d:
                            if d[k] == 1:
                                no_dup[i][j] += 1
                            no_dup[i][j] += 1
                            d[k] += 1
                        else:
                            d[k] = 1
            dp = []
            for i in range(n+1):
                dp.append([0]*(n+1))
            for i in range(1, n+1):
                dp[1][i] = no_dup[0][i-1]
            for i in range(2, n+1):
                dp[i][1] = 0
            for i in range(2, n+1):
                for j in range(2, n+1):
                    opt = 1e18
                    for p in range(1, j):
                        opt = min(opt, dp[i-1][p]+no_dup[p][j-1])
                    dp[i][j] = opt
            for r in dp:
                print(r)
            ans = 1e18
            for m in range(1,n):
                ans = min(ans,m*K+dp[m][n])
            print(ans)