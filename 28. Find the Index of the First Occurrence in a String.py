haystack = "leetcode"
needle = "leeto"
slen = len(haystack)
tlen = len(needle)
s = list(haystack)
t = list(needle)
flag, index = 0, 0
i, j = 0, 0
while i < slen and j < tlen:
    if s[i] == t[j]:
        if j == 0:
            index = i
        flag += 1
        i += 1
        j += 1
    else:
        i = i - flag
        index = 0
        flag = 0
        j = 0
        i += 1
if flag == tlen:
    print(index)
else:
    print('-1')
