# WIPL
# 30 points

MAX = 10**5 + 1

for t in range(int(input())):
    n, k = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort()
    i = n-1
    suffix = [0]
    while i >= 0:
        suffix.append(suffix[-1]+H[i])
        i -= 1
    suffix.reverse()
    
    dp = []
    for i in range(n+1):
        dp.append([MAX]*(k+1))
    
    dp[n][0] = 0
    for i in range(n-1, -1, -1):
        for j in range(k, -1, -1):
            if j <= H[i]:
                dp[i][j] = H[i]
                continue
            if dp[i+1][j-H[i]] == MAX:
                dp[i][j] = MAX
            else:
                dp[i][j] = min(dp[i+1][j], dp[i+1][j-H[i]]+H[i])
    flag = 0
    for i in range(n-1,-1,-1):
        if suffix[i] - dp[i][k] >= k:
            print(n-i)
            flag = 1
            break
    if flag == 1:
        continue
    print(-1)