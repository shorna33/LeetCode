bills = [5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]

n = len(bills)
flag = 0

notes = [[5, 0], [10, 0], [20, 0]]

for i in range(n):
    if (notes[0][1] < 0) or (notes[1][1] < 0) or (notes[2][1] < 0):
        flag = 1
        break
    if bills[i] == 5:
        notes[0][1] += 1
    if bills[i] == 10:
        notes[1][1] += 1
        notes[0][1] -= 1
    if bills[i] == 20:
        notes[2][1] += 1
        if notes[1][1] < 1:
            notes[0][1] -= 3
        else:
            notes[0][1] -= 1
            notes[1][1] -= 1

if (notes[0][1] < 0) or (notes[1][1] < 0) or (notes[2][1] < 0):
    flag = 1

if flag == 1:
    print('false')
else:
    print('true')
