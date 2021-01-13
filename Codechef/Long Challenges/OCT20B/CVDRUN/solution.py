# cook your dish here
for t in range(int(input())):
    n,k,x,y = map(int, input().split())
    first = x
    while x != y:
        x = (x+k)%n
        if x == first:
            print('NO')
            break
    else:
        print('YES')