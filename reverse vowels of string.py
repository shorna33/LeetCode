s = "Egad! Loretta has Adams as mad as a hatter. Old age!"
s = list(s)
temp = 0
n = len(s)
count = 0
vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for i in range(n):
    if s[i] in vowel:
        count += 1
print(count)

i = 0
j = len(s) - 1
while (count > 0) and (i < n) and (j > 0):
    print(count)
    if (s[i] in vowel) and (s[j] in vowel):
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        i += 1
        j -= 1
        count -= 2
        continue
    if (s[i] in vowel) and (s[j] not in vowel):
        j -= 1
        continue
    if (s[i] not in vowel) and (s[j] in vowel):
        i += 1
        continue
    i += 1
    j -= 1

s = ''.join(s)
print(s)

