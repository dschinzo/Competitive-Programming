#BILLRD
for t in range(int(input())):
    N, k, x, y = map(int, input().split())
    case_1 = [(N,N-x+y),(N-x+y,N),(0,x-y),(x-y,0)]
    case_2 = [(N-y+x,N),(N,N-y+x),(y-x,0),(0,y-x)]
    if x == 0:
        if y == 0 or y == N:
            print(x, y)
        else:
            print(*case_2[(k-1)%4])
    elif x == N:
        if y == 0 or y == N:
            print(x, y)
        else:
            print(*case_1[k%4])
    elif x == y:
        print(N, N)
    elif x > y:
        print(*case_1[(k-1)%4])
    else:
        print(*case_2[(k-1)%4])