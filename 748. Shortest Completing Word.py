licensePlate = "1s3 456"
words = ["looks", "pest", "stew", "show"]

licensePlate = list(licensePlate)
n = len(licensePlate)

target = []
contains = []
minimum = 9999
index = 0

for i in range(n):
    if (licensePlate[i] >= 'a') and (licensePlate[i] <= 'z'):
        target.append(licensePlate[i])
        continue
    if (licensePlate[i] >= 'A') and (licensePlate[i] <= 'Z'):
        target.append(chr(ord(licensePlate[i]) + 32))
        continue

target = sorted(target)

for i in range(len(words)):
    x = sorted(words[i])

    count = 0
    for j in range(len(target)):
        for k in range(len(x)):
            if target[j] == x[k]:
                x[k] = 0
                count += 1
                break
    if count == len(target):
        contains.append(words[i])

if len(contains) == 0:
    print('')
    exit()

if len(contains) == 1:
    print(contains[0])
else:
    for i in range(len(contains)):
        if minimum > len(contains[i]):
            minimum = len(contains[i])
            index = i
    print(contains[index])
