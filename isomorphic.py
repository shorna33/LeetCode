s = "bbbaaaba"
t = "aaabbbba"
slen = len(s)
tlen = len(t)
s = list(s)
t = list(t)
scol = len(set(s))
tcol = len(set(t))
f = 0
match = [[0 for i in range(2)] for j in range(scol)]
match[0][0] = s[0]
match[0][1] = t[0]
temp = 0
if (slen != tlen) or (scol != tcol):
    print("false")
    exit()
else:
    a = 1
    for i in range(1, slen):
        k = 0
        for j in range(scol):
            if s[i] == match[j][0]:
                k = 1
        if k == 0:
            match[a][0] = s[i]
            match[a][1] = t[i]
            a = a + 1
    print(match)
    r = 0
    for i in range(slen):
        for j in range(scol):
            if s[i] != match[j][0]:
                continue
            else:
                r = j
                break
        if t[i] != match[r][1]:
            f = 1
    if f == 1:
        print('false')
    else:
        print('true')
