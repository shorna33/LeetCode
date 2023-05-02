
#
#                     NOT SOLVED
#


columnNumber = 701
count = 0
add, div = 0, 0
letters = [[0 for i in range(2)] for j in range(26)]
for i in range(26):
    letters[i][0] = chr(i + 65)
    letters[i][1] = i + 1
add = columnNumber % 26
div = round(columnNumber / 26)
output = [0 for i in range(div + 1)]
print(add, div)
if div > 0:
    for i in range(div):
        output[i] = 'A'
        count = i
    output[count+1] = letters[add-1][0]
else:
    output[0] = letters[columnNumber - 1][0]
print(output)
