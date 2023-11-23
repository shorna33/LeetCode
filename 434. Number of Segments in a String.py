s = "Hello"

temp = []
i = 0
output = []
while i < len(s):
    if s[i] == ' ':
        i += 1
        temp = ''.join(map(str, temp))
        output.append(temp)
        temp = []
        continue
    elif i == (len(s) - 1):
        temp.append(s[i])
        i += 1
        temp = ''.join(map(str, temp))
        output.append(temp)
        temp = []
    else:
        temp.append(s[i])
        i += 1
count = 0
for i in range(len(output)):
    if output[i] != '':
        count += 1
print(count)
