s = "abcdefg"
k = 3

s = list(s)
slen = len(s)

temp = 0

for i in range(0, slen, (2 * k)):
    if (slen - i) < k:
        y = slen - i
    else:
        y = k
    for x in range(int(y/2)):
        m = i + x
        n = i + y - x - 1
        print(i, m, n, x, y)
        temp = s[m]
        s[m] = s[n]
        s[n] = temp

s = ''.join(map(str, s))
print(s)
