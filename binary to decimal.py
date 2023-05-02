a = '1010'
b = '1011'
sum = bin(int(a, 2) + int(b, 2)).replace("0b", "")
print(sum)