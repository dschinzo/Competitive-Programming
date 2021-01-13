#DIVTHREE
for i in range(int(input())):
    N, K, D = map(int, input().split())
    print(min(sum(map(int, input().split())) // K, D))
