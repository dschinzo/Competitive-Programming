# cook your dish here
for t in range(int(input())):
    n = int(input())
    x_cor = {}
    y_cor = {}
    for _ in range(4*n - 1):
        x, y = map(int, input().split())
        if x in x_cor:
            x_cor.pop(x)
        else:
            x_cor[x] = 1
        if y in y_cor:
            y_cor.pop(y)
        else:
            y_cor[y] = 1
        
    print(list(x_cor)[0], list(y_cor)[0])
