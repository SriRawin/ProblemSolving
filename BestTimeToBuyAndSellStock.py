prices = [7, 1, 5, 3, 6, 4]
profit = 0
decreasing = False
increasing = False
inStock = False
for i in range(0, len(prices)):
    if i+1 < len(prices) and prices[i] < prices[i+1]:
        decreasing = False
        increasing = True
    if i+1 < len(prices) and prices[i] > prices[i+1]:
        increasing = False
        decreasing = True
    if decreasing or i == len(prices)-1:
        if inStock:
            profit += prices[i]-buy
            inStock = False
    if increasing:
        if not inStock:
            buy = prices[i]
            inStock = True

print(profit)
