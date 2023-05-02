s = "3[a]2[bc]"
sLen = len(s)
s = list(s)
print(s)
for i in range(len(s)):
    if int(s[i]):
        print(s[i])
