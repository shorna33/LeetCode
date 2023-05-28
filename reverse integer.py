x = 120

s = x
if x < 0:
    s = s * (-1)
s = str(s)
s = list(s)
n = len(s)
temp = 0

for i in range(int(n/2)):
    temp = s[n - 1 - i]
    s[n - 1 - i] = s[i]
    s[i] = temp

# print(s)
output = ''.join(map(str, s))
output = int(output)

if output > 2147483647:
    print(0)
    exit()

if x < 0:
    output *= (-1)
print(output)
