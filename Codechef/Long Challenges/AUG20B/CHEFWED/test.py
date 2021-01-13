def solve(main, lst, pre=[]):
    m = len(lst)
    for i in range(m):
        for w in range(2,m-i+1):
            print(pre, lst[i:i+w], list(map(lambda x: [x],main-set(pre)-set(lst[i:i+w]))))
            solve(main, lst[i+w:],lst[i:i+w])
l = list(range(5))
l = "ABCDE"
solve(set(l), l)