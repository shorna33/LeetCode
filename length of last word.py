s = ' dbg'
s = list(s)
n = len(s)
count = 0
i = n-1
while 1:
    if ((s[i] >= 'a') and (s[i] <= 'z')) or ((s[i] >= 'A') and (s[i] <= 'Z')):
        break
    i -= 1
while 1:
    count += 1
    if i == 0:
        break
    elif s[i-1] == ' ':
        break
    i -= 1
print(count)
