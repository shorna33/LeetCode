s = "a"
n = len(s)

sub = []

i = 0
flag = 0
temp = s
sub.append(s[0])
temp_sub = ''.join(sub)
while i < (n/2):
    for j in range(int(n/(i+1))):
        temps = temp.split(temp_sub, 1)
        if (len(temps) > 1) and (len(temps[0]) == 0):
            temp = temps[1]
            if len(temp) == 0:
                flag = 1
        else:
            i += 1
            sub.append(s[i])
            temp_sub = ''.join(sub)
            temp = s
            break
    if flag == 1:
        break

if flag == 1:
    print('true')
else:
    print('false')

