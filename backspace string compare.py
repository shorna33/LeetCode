def pop(str, pos, n):
    if pos < n:
        for j in range(pos, n):
            str[j - 2] = str[j]
    return str


def onePop(str, n):
    for x in range(1, n):
        str[x - 1] = str[x]
    return str


def countHash(str):
    n = len(str)
    count = 0
    for i in range(n):
        if str[i] == '#':
            count += 1
    return count


s = 'a##c'
t = '#a#c'
slen = len(s)
tlen = len(t)
slength = slen
tlength = tlen
s = list(s)
t = list(t)
sHash = countHash(s)
tHash = countHash(t)
for k in range(sHash):
    for i in range(slength):
        if s[i] == '#' and i == 0:
            onePop(s, slength)
            slength -= 1
            break
        if s[i] == '#':
            pop(s, i + 1, slength)
            slength -= 2
            break
for k in range(tHash):
    for i in range(tlength):
        if t[i] == '#' and i == 0:
            onePop(t, tlength)
            tlength -= 1
            break
        if t[i] == '#':
            pop(t, i + 1, tlength)
            tlength -= 2
            break

if slength != tlength:
    print('false')
flag = 0
for i in range(slength):
    if s[i] != t[i]:
        flag = 1
if flag == 1:
    print('false')
else:
    print('true')
