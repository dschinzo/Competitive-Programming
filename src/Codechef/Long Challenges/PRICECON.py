for t in range(int(input())):
    n, k = input().split()
    k = int(k)
    arr = map(int, input().split())
    print(sum([max(0, el-k) for el in arr]))