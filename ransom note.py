ransomNote = "aa"
magazine = "aba"

s = list(ransomNote)
t = list(magazine)
slen = len(s)
tlen = len(t)

i = 0
j = 0

while (i < slen) and (j < tlen):
    if s[i] == t[j]:
        s[i] = 0
        t[j] = 0
        i += 1
        j = 0
    else:
        j += 1
flag = 0
for i in range(slen):
    if s[i] != 0:
        flag = 1

if flag == 1:
    print('false')
else:
    print('true')