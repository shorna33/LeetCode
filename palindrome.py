x = int('-121')
x = str(x)
x = list(x)
n = len(x)
y = [0 for i in range(n)]
s = ''
for i in range(n):
    s = x[i]
    y[n-i-1] = s
flag = 0
for i in range(n):
    if y[i] != x[i]:
        flag = 1
if flag == 1:
    print('false')
else:
    print('true')
