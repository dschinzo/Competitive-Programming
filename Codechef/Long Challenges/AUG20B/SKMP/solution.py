for i in range(int(input())):
    S = list(input())
    P = input()
    for c in P:
        S.remove(c)
    S.sort()
    for i in range(len(S)):
        if S[i] > P[0]:
            break
    else:
        i = len(S)
    opt = "".join(S[:i])+P+"".join(S[i:])
    if P[0] in S:
        k = S.index(P[0])
        print(min(opt, "".join(S[:k])+P+"".join(S[k:])))
    else:
        print(opt)