s = 'anagram'
t = 'nagaram'
slen = len(s)
tlen = len(t)
s = list(s)
t = list(t)
flag = 0

if slen != tlen:
    print('false')
    exit(0)

s.sort()
t.sort()
for i in range(slen):
    if s[i] != t[i]:
        flag = 1

if flag == 1:
    print('false')
else:
    print('true')

