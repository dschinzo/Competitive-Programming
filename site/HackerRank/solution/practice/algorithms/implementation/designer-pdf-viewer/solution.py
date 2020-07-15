import string
alphabet = string.ascii_lowercase
lst = list(map(int,input().split(' ')))
word = input()
d = {}
for i in range(26):
    d[alphabet[i]] = lst[i]
mx = 0
for i in range(len(word)):
    if d[word[i]] > mx:
        mx = d[word[i]]
print(mx*len(word))
