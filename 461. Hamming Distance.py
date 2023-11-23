x = 4
y = 5

a = str(bin(x).replace("0b", ""))
b = str(bin(y).replace("0b", ""))

l1 = len(a)
l2 = len(b)
n = abs(l1 - l2)

distance = 0
temp = ''
zero = '0'
for i in range(n):
    temp = temp + zero

if l1 < l2:
    a = temp + a
if l2 < l1:
    b = temp + b

for i in range(len(a)):
    if a[i] != b[i]:
        distance += 1

print(distance)

