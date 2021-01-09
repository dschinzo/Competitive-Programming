def fib(n):
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(n-1):
        dp[i+1] += dp[i]
        dp[i+2] += dp[i]
    return dp[n-1]

print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))