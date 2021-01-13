#DECODEIT

encode = 'abcdefghijklmnop'
def decode(S):
    return encode[sum(2**(3-i) for i in range(4) if S[i] == '1')]
        
    
for t in range(int(input())):
    n = int(input())
    s = input()
    res = ''
    for i in range(0, n, 4):
        res += decode(s[i:i+4])
    print(res)