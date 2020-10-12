for t in range(int(input())):
    n = int(input())
    if n == 1:
        print(1)
    elif n & (n-1) == 0:
        print('-1')
    else:
        lst = ['2', '3', '1']
        if n < 4:
            print(" ".join(lst))
        else:
            m = 4
            while m < n:
                lst.append(str(m+1))
                lst.append(str(m))
                for i in range(m+2, min(m*2,n+1)):
                    lst.append(str(i))
                m *= 2
            print(" ".join(lst))