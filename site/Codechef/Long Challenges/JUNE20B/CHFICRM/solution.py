for t in range(int(input())):
    n = input()
    lst = map(int, input().split())
    dct = {5:0, 10:0, 15:0}
    for i in lst:
        dct[i] += 1
        if i == 15:
            if dct[10] == 0:
                if dct[5] < 2:
                    print("NO")
                    break
                else:
                    dct[5] -= 2
            else:
                dct[10] -= 1
        elif i == 10:
            if dct[5] == 0:
                print("NO")
                break
            else:
                dct[5] -= 1
    else:
        print("YES")
