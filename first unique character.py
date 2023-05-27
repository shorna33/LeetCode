s = ""

s = list(s)
l = len(s)

temp = []
i = 0
output = -1

while i < l:
    temp = s.copy()
    temp[i] = 0
    if s[i] not in temp:
        output = i
        break
    i += 1

print(output)
