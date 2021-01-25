for t in range(int(input())):
    n = int(input())
    a = input()
    b = ['1']*n
    for i in range(1,n):
        if b[i-1] == '1':
            if a[i] == '1' and a[i-1] == '1':
                b[i] = '0'
            elif a[i] == '0' and a[i-1] == '0':
                b[i] = '0'
        else:
            if a[i] == '0' and a[i-1] == '1':
                b[i] = '0'
    print("".join(b))