def search(temp, t):
    for j in range(len(t)):
        if temp == t[j]:
            t[j] = 0
            return t


s = 'abcd'
t = 'abcde'
slen = len(s)
tlen = len(t)

s = list(s)
t = list(t)
output = 0

if (slen == 0) and (tlen == 1):
    print(t)
    exit()


for i in range(slen):
    search(s[i], t)

for i in range(tlen):
    if t[i] != 0:
        output = t[i]

print(output)
