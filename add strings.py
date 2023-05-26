num1 = "9"
num2 = "99"

num1 = list(num1)
num2 = list(num2)
l1 = len(num1)
l2 = len(num2)
sum = []
rem = 0
ren = abs(l2 - l1)

if l1 <= l2:
    for i in range(l1 - 1, -1, -1):
        temp = (ord(num1[i]) - 48) + (ord(num2[i + ren]) - 48) + rem
        rem = 0
        print(i, temp)
        if temp > 9:
            rem = 1
            sum.append(temp - 10)
        else:
            sum.append(temp)
    for j in range(ren - 1, -1, -1):
        if rem == 1:
            temp = (ord(num2[j]) - 48) + rem
            rem = 0
            if temp > 9:
                rem = 1
                sum.append(temp - 10)
            else:
                sum.append(temp)
        else:
            sum.append(num2[j])
else:
    for i in range(l2-1, -1, -1):
        temp = (ord(num2[i])-48) + (ord(num1[i+ren])-48) + rem
        rem = 0
        print(i, temp)
        if temp > 9:
            rem = 1
            sum.append(temp - 10)
        else:
            sum.append(temp)
    print(sum)
    for j in range(ren-1, -1, -1):
        if rem == 1:
            temp = (ord(num1[j]) - 48) + rem
            rem = 0
            if temp > 9:
                rem = 1
                sum.append(temp - 10)
            else:
                sum.append(temp)
        else:
            sum.append(num1[j])

if rem == 1:
    sum.append('1')

output = ''.join(map(str, sum))
output = output[::-1]
print(output)

