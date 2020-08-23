arr = list(map(int, input().split()))
sub_list = [[]]
for i in range(len(arr)):
    for j in range(i+1,len(arr)+1):
        sub_list.append(arr[i:j])
print(sub_list)