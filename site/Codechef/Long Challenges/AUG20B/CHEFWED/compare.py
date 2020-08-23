f1 = open('ans_my.txt','r')
f2 = open('ans_sol.txt', 'r')
l1 = f1.readlines()
l2 = f2.readlines()
for i in range(len(l1)):
    if l1[i]!=l2[i]:
        print(l1[i],l2[i])
else:
    print("Same answers!")