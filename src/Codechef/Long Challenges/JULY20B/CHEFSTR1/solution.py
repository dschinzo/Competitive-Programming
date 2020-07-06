# cook your dish here
for t in range(int(input())):
    n = input()
    arr = list(map(int, input().split()))
    s = 0
    for i in range(int(n)-1):
        s += abs(arr[i] - arr[i+1])-1
    print(s)