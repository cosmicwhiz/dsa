def maxProfit(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit

prices = [5,1,2,3,0,2]
res = maxProfit(prices)
print(res)