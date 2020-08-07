if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        line = input().split()
        student_marks[line[0]] = sum(map(float,line[1:]))/3.0
    print('%.2f' % student_marks[input()])