i, j, k = map(int, input().split(" "))
cnt = 0
for q in range(i,j+1):
    if (q - int(str(q)[::-1])) % k == 0:
        cnt += 1
print(cnt)