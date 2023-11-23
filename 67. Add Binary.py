a = "11"
b = "1"

sum = bin(int(a, 2) + int(b, 2)).replace("0b", "")
print(sum)
