word = "mL"

s = list(word)
slen = len(s)
flag = 0
flag1 = 0
flag2 = 0

if (ord(s[0]) < 91) and (ord(s[0]) > 64):
    print('no', ord(s[0]))
    for i in range(1, slen):
        if ord(s[i]) > 122 or ord(s[i]) < 97:
            flag1 = 1
            break
    if flag1 == 0:
        print('true')
        exit()
    for i in range(1, slen):
        if ord(s[i]) > 91 or ord(s[i]) < 65:
            flag2 = 1
            break
    if flag2 == 0:
        print('true')
        exit()
else:
    print('yes')
    for i in range(slen):
        if ord(s[i]) > 122 or ord(s[i]) < 97:
            flag = 1
            break
    if flag == 0:
        print('true')
        exit()
    for i in range(slen):
        if ord(s[i]) > 91 or ord(s[i]) < 65:
            flag = 1
            break
    if flag == 0:
        print('true')
        exit()


if ((flag1 == 1) and (flag2 == 1)) or (flag == 1):
    print('false')
else:
    print('true')

