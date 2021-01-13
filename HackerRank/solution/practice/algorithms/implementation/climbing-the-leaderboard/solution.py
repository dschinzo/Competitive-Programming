n = input()
lst = map(int, input().split())
ranked = [-1]
for el in lst:
    if el != ranked[-1]:
        ranked.append(el)
ranked.pop(0)
m = input()
lst = map(int, input().split())
i = len(ranked)
for score in lst:
    while (i > 0) and (score >= ranked[i-1]):
        i -= 1
    print(i+1)