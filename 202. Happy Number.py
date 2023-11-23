def exists(arr, m):
    f = 0
    for i in range(len(arr)):
        if arr[i] == m:
            f = 1
    if f == 1:
        return 1
    else:
        return 0


n = 7
sum, flag, temp = n, 0, n
arr = []
arr.append(n)
length = len(str(temp))
while sum != 1:
    num = str(temp)
    length = len(num)
    sum = 0
    for i in range(length):
        sum = sum + int(num[i]) ** 2
    temp = sum
    print(arr)
    if exists(arr, sum):
        break
    else:
        arr.append(sum)
if sum == 1:
    flag = 1
if flag == 1:
    print('yes')
else:
    print('no')
