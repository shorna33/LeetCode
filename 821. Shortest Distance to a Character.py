s = "aaab"
c = "b"

s = list(s)
index = []

for i in range(len(s)):
    if s[i] == c:
        s[i] = 0
        index.append(i)

j = 0
for i in range(len(s)):
    if (i == index[j]) and (j < len(index)-1):
        j += 1
    if s[i] == 0:
        continue
    else:
        if j > 0:
            s[i] = min((abs(index[j-1] - i)), (abs(index[j] - i)))
        else:
            s[i] = abs(index[j] - i)

print(s)
