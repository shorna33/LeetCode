from functools import reduce

s = 'aaa'
t = 'aa aa aa aa'
slen = len(s)
s = list(s)
sList = reduce(lambda re, x: re+[x] if x not in re else re, s, [])
t = t.split()
tlen = len(t)

flag = 0

if slen != tlen:
    print('false')
    exit(0)

tList = reduce(lambda re, x: re+[x] if x not in re else re, t, [])
n = len(sList)

if len(sList) != len(tList):
    print('false')
    exit(0)

arr = [[0 for i in range(2)] for j in range(n)]
for i in range(n):
    arr[i][0] = sList[i]
    arr[i][1] = tList[i]

print(arr)

for i in range(slen):
    for j in range(n):
        if (s[i] == arr[j][0]) and (t[i] != arr[j][1]):
            print(s[i], arr[j][0])
            print(t[i], arr[j][1])
            flag = 1
if flag == 1:
    print('false')
else:
    print('true')


