image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]

x = len(image)
y = len(image[0])
temp = 0

for i in range(x):
    for j in range(y):
        if j > y - j - 1:
            break
        temp = image[i][y - j - 1]
        image[i][y - j - 1] = image[i][j]
        image[i][j] = temp
        if image[i][j] == 1:
            image[i][j] = 0
        elif image[i][j] == 0:
            image[i][j] = 1
        if (image[i][y - j - 1] == 1) and (j < y - j - 1):
            image[i][y - j - 1] = 0
        elif (image[i][y - j - 1] == 0) and (j < y - j - 1):
            image[i][y - j - 1] = 1

print(image)