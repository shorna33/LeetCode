s = "Hello"

s = list(s)

for i in range(len(s)):
    if (ord(s[i]) > 64) and (ord(s[i]) < 91):
        s[i] = chr(ord(s[i]) + 32)

s = ''.join(s)

print(s)
