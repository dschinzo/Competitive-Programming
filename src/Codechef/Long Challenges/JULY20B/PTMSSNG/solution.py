# cook your dish here
for t in range(int(input())):
    n = int(input())
    x_cor = []
    y_cor = []
    for _ in range(4*n - 1):
        x, y = map(int, input().split())
        if x in x_cor:
            x_cor.remove(x)
        else:
            x_cor.append(x)
        if y in y_cor:
            y_cor.remove(y)
        else:
            y_cor.append(y)
    print(x_cor.pop(), y_cor.pop())
