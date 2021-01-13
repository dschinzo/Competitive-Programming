with open("testcase1.txt") as f:
    #w_f = open("ans_sol.txt","w")
    for _ in range(int(f.readline())):
        N, K = map(int, f.readline().split())
        arr = list(map(int, f.readline().split()))
        #for K in range(2,5):
        no_dup = []
        for i in range(N):
            d = {}
            no_dup.append([0]*N)
            for j in range(i, N):
                no_dup[i][j] = no_dup[i][j-1]
                if arr[j] in d:
                    if d[arr[j]] == 1:
                        no_dup[i][j] += 1
                    no_dup[i][j] += 1
                    d[arr[j]] += 1
                else:
                    d[arr[j]] = 1
        #for r in no_dup:
        #    print(r)
        dp = []
        for i in range(N+1):
            dp.append([0]*(N+1))
        for i in range(1, N+1):
            dp[1][i] = no_dup[0][i-1]
        for i in range(2, N+1):
            dp[i][1] = 0
        for i in range(2, N+1):
            for j in range(2, N+1):
                opt = 1e6
                for p in range(1, j):
                    opt = min(opt, dp[i-1][p]+no_dup[p][j-1])
                dp[i][j] = opt
        ans = 1e6
        #for r in dp:
        #    print(r)
        for m in range(1,N):
            ans = min(ans,m*K+dp[m][N])
            #print(m*K+dp[m][N])
        print(ans)
        #w_f.writelines(" ".join(map(str, arr))+"\t"+str(K)+"\t"+str(ans)+"\n")