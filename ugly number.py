
#
#                     NOT SOLVED
#


def exist(num):
    l = len(num)
    flag = 0
    for i in range(l):
        if (num[i] != 2) and (num[i] != 3) and (num[i] != 5):
            flag = 1
    if flag == 1:
        return 1
    else:
        return 0


def isPrime(d):
    arr = []
    if (d == 1) or (d == 2) or (d == 3):
        return 1
    mid = int(d / 2)
    for i in range(2, mid + 1):
        if (d % i) == 0:
            arr.append(i)
    if (len(arr)) == 0:
        return 1
    else:
        return 0


n = 32
num = []

if n == 1:
    print('true')
    exit()
if n <= 0 or isPrime(n) and ((n != 2) and (n != 3) and (n != 5)):
    print('false')
    exit()
mid = round(n / 2)
for i in range(2, mid + 1):
    if (n % i) == 0 and isPrime(i):
        print(i)
        num.append(i)
print(num)
if exist(num):
    print('false')
else:
    print('true')
