s = 'LVIII'
s = list(s)
n = len(s)
sum = 0
assign = [['I', 1], ['V', 5], ['X', 10], ['L', 50], ['C', 100], ['D', 500], ['M', 1000]]
pos = 10
for i in range(n):
    for j in range(7):
        if s[i] == assign[j][0] and pos < j:
            sum = sum + (assign[j][1] - assign[pos][1] - assign[pos][1])
            break
        elif s[i] == assign[j][0]:
            sum = sum + assign[j][1]
            pos = j
print(sum)
