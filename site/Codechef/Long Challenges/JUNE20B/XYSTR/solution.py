# cook your dish here
for t in range(int(input())):
    s = input()
    n = len(s)
    if n < 2:
        print(0)
    else:
        i = 1
        last = s[0]
        cnt = 0
        while i < n:
            if s[i] == last:
                i += 1
            else:
                cnt += 1
                if i+1 < n:
                    last = s[i+1]
                i += 2
        print(cnt)                