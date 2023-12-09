jewels = "z"
stones = "ZZ"

jewels = list(jewels)
stones = list(stones)

count = 0

for i in range(len(stones)):
    if stones[i] in jewels:
        count += 1

print(count)
