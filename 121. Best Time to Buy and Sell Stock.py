prices = [7,1,4,3,1]
p = len(prices)
maximum = 0
temp = 0
maxProfit = 0
j = p - 1
for i in range(p-2, -1, -1):
    temp = prices[j] - prices[i]
    if prices[j] > prices[i]:
        maximum = max(temp, maximum)
    else:
        j = i
print(maximum)
