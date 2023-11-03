left = 47
right = 85

output = []

for i in range(left, right+1):
    if '0' in str(i):
        continue
    if len(str(i)) < 2:
        output.append(i)
        continue
    if len(str(i)) > 1:
        temp = list(str(i))
        flag = 0
        for j in range(len(str(i))):
            if i % int(temp[j]) != 0:
                flag = 1
        if flag == 0:
            output.append(i)
        else:
            continue
print(output)



