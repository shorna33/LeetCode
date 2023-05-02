s = "abccccdd"
slen = len(s)
s = list(s)
scol = len(set(s))
count = [[0 for i in range(2)] for j in range(scol)]
sList = set(s)
k = 0
for i in sList:
    count[k][0] = i
    for j in range(slen):
        if count[k][0] == s[j]:
            count[k][1] += 1
    k += 1

odd = 0
pal = 0
for i in range(scol):
    if (count[i][1] % 2) == 1 and count[i][1] > odd:
        odd = count[i][1]
    elif (count[i][1] % 2) == 0:
        pal = pal + count[i][1]
pal = pal + odd
print(pal)
