def maxProfit(prices):
    buy = 0
    sell = 1
    curr_max = 0
    while sell < len(prices):
        if prices[buy] < prices[sell]:
            curr_max = max(curr_max, prices[sell]-prices[buy])
        else:
            buy = sell
        sell += 1
    return curr_max


prices = [10,20,25,15.40]
result = maxProfit(prices)
print(result)
