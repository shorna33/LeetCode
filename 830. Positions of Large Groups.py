s = "abcdddeeeeaabbbcd"
s = list(s)

n = len(s)
interval = []
array = []
count = 0

if n < 3:
    print(interval)
    exit()

i = 0
j = 1

temp = s[0]
while j<n:
    if s[i] == s[j]:
        temp = temp + s[j]
        j += 1
        if j == n:
            array.append(temp)
    else:
        i = j
        j += 1
        if j == n:
            array.append(temp)
            array.append(s[j-1])
        else:
            array.append(temp)
        temp = s[i]


for i in range(len(array)):
    if len(array[i]) >= 3:
        interval.append([count, count+len(array[i])-1])
        count = count + len(array[i])
    else:
        count = count + len(array[i])

print(interval)
