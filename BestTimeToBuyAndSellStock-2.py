prices = [7, 6, 4, 3, 1]
profit = 0
decreasing = False
increasing = False
inStock = False
buy = None
for i in range(0, len(prices)):
    print("stocks", prices[i])
    if i+1 < len(prices) and prices[i] < prices[i+1]:
        decreasing = False
        increasing = True
    if i+1 < len(prices) and prices[i] > prices[i+1]:
        increasing = False
        decreasing = True
    if decreasing or i == len(prices)-1:
        if inStock:
            deal = prices[i]-buy
            if deal > profit:
                profit = deal
                print("profit", profit)

    if increasing:
        if buy == None or prices[i] < buy:
            buy = prices[i]
            inStock = True
        print(buy)

print(profit)
