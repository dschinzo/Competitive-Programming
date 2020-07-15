from collections import Counter
n = int(input())
numbers = list(map(int, input().split(" ")))
c = Counter(numbers)
mx = 0
for i in c:
    if c[i] + c[i-1] > mx:
        mx = c[i] + c[i-1]
print(mx)
