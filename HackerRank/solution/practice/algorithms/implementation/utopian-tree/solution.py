for i in range(int(input())):
    period = int(input())
    height = 0
    for i in range(period+1):
        if i % 2 == 0:
            height += 1
        else:
            height = height * 2
    print(height)
