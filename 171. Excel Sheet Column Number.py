columnTitle = 'XGPD'
n = len(columnTitle)
count = 0
add, div = 0, 0
letters = [[0 for i in range(2)] for j in range(26)]
for i in range(26):
    letters[i][0] = chr(i + 65)
    letters[i][1] = i + 1
num = 0
for i in range(n):
    for j in range(26):
        if letters[j][0] == columnTitle[n-1-i]:
            print(letters[j][0], letters[j][1])
            num = num + ((26 ** i) * letters[j][1])
print(num)
