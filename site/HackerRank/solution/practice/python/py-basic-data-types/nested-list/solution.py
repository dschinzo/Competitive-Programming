if __name__ == '__main__':
    min1 = 101
    min2 = 102
    students = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score < min1:
            min2, min1 = min1, score
        elif score > min1 and score < min2:
            min2 = score
        students[name] = score
    sel = [name for name in students if students[name] == min2]
    sel.sort()
    for s in sel:
        print(s)