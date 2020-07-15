for t in range(int(input())):
    ts = int(input())
    if ts % 2 == 1:
        print(ts//2)
    else:
        n = ts // 2
        while n:
            if n % 2 == 1:
                print(n//2)
                break
            n //= 2
