# cook your dish here
for t in range(int(input())):
    q = int(input())
    points = [0, 0]
    for _ in range(q):
        A, B = input().split()
        ap = sum(map(int, A))
        bp = sum(map(int, B))
        if ap > bp:
            points[0] += 1
        elif ap < bp:
            points[1] += 1
        else:
            points[0] += 1
            points[1] += 1
    if points[0] > points[1]:
        print(0, points[0])
    elif points[0] < points[1]:
        print(1, points[1])
    else:
        print(2, points[0])