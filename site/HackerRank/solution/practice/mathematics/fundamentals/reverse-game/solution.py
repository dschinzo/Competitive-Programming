for _ in range(int(input())):
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])

    i = 0
    guess = n - 1
    while i < n:
        if guess == k:
            print(i)
            break
        if i % 2 == 0:
            guess += 1 + i - n
        else:
            guess += n - 1 - i
        i += 1
