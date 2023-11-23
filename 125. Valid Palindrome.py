s = "A man, a plan, a canal: Panama"
s = list(s)
n = len(s)
for i in range(n):
    if (s[i] >= 'A') and (s[i] <= 'Z'):
        s[i] = chr(ord(s[i]) + 32)
arr = [0 for i in range(n)]
i = 0
j = 0
index = 0
while i < n:
    if (s[i] >= 'a') and (s[i] <= 'z'):
        arr[j] = s[i]
        j += 1
        index += 1
    elif (s[i] <= '9') and (s[i] >= '0'):
        arr[j] = s[i]
        j += 1
        index += 1
    i += 1
flag = 0
for i in range(index):
    if arr[i] != arr[index-i-1]:
        flag = 1
if flag == 1:
    print('false')
else:
    print('true')


