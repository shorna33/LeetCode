s = "axc"
t = "ahbgdc"
slen = len(s)
tlen = len(t)
s = list(s)
t = list(t)
k = 0
x = 0
count = 0
for i in range(slen):
    for j in range(x, tlen):
        if s[i] == t[j]:
            k = j
            count = count + 1
            break
    x = k + 1
if count == slen:
    print('true')
else:
    print('false')
