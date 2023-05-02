n = 30
flag = 0
div = n
if n == 1:
    print('true')
    exit()
while div >= 1:
    print(div)
    div = div / 2
    if div == 1:
        flag = 1
        break
if flag == 1:
    print('true')
else:
    print('false')
