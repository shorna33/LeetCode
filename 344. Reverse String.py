s = ["h","e","l","l","o"]
temp = 0
for i in range(round(len(s)/2)):
    temp = s[i]
    s[i] = s[len(s) - i - 1]
    s[len(s) - i - 1] = temp
print(s)

