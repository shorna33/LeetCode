s = "Test1ng-Leet=code-Q!"
s = list(s)

n = len(s)
temp = 0
alphabets = ['0' for i in range(52)]

for i in range(26):
    alphabets[i] = chr(i + ord('a'))
for i in range(26):
    alphabets[i + 26] = chr(i + ord('A'))

i = 0
j = n - 1

while i < j:
    print(s[i], s[j])
    if (s[i] in alphabets) and (s[j] in alphabets):
        temp = s[j]
        s[j] = s[i]
        s[i] = temp
        i += 1
        j -= 1
    elif (s[i] in alphabets) and (s[j] not in alphabets):
        j -= 1
    elif (s[i] not in alphabets) and (s[j] in alphabets):
        i += 1
    elif (s[i] not in alphabets) and (s[j] not in alphabets):
        i += 1
        j -= 1


s = ''.join(s)
print(s)

