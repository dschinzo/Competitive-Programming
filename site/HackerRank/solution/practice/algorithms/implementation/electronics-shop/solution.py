def getMoneySpent (b, k, d):
    if len(k) == 0 or len(d) == 0 or min(k) + min(d) > b:
        return -1
    k.sort(reverse = True)
    d.sort(reverse = True)
    lst = []
    for i in k:
        for j in d:
            if i + j <= b:
                lst.append(i + j)
                break
    return max(lst)
budget, n, m = map(int, input().split(" "))
keyboards = list(filter(lambda x: x < budget, map(int,input().split(" "))))
drives = list(filter(lambda x: x < budget, map(int,input().split(" "))))
print(getMoneySpent(budget, keyboards, drives))