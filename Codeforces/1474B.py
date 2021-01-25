def isPrime(n) : 
    if (n <= 3) : 
        return True

    if (n % 2 == 0 or n % 3 == 0) : 
        return False
 
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
 
    return True

for t in range(int(input())):
    d = int(input())
    i = d + 1
    check = 0

    while True:
        if isPrime(i):
            if check == 1:
                if i - res >= d:
                    print(res * i)
                    break
            else:
                res = i
                check = 1
        i += 1
        
    