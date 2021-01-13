from itertools import combinations_with_replacement
with open("testcase3.txt", 'w') as f:
    f.writelines('220\n')
    for r in com(range(1,4),20):
        f.writelines('20 2\n')
        f.writelines(" ".join(map(str,r))+'\n')