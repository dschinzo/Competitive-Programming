# 1154A
arr = list(map(int, input().split()))
arr.sort()
print(" ".join([str(arr[-1] - el) for el in arr[:-1]]))