num = 0
arr = str(num)
n = len(arr)
s = 0
while n > 1:
    for i in range(n):
        s = s + int(arr[i])
    arr = str(s)
    n = len(arr)
    s = 0
num = int(arr)
print(num)
