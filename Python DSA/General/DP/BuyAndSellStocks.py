def maxProfit(prices):
    maxProfit = [0]
    def dp(profit, i):
        if i >= len(prices) - 1:
            maxProfit[0] = max(maxProfit[0], profit)
        while i < len(prices)-1:
            ind = i
            profitsSet = set()
            for p in prices[i+1:]:
                ind += 1
                newProfit = p - prices[i]
                if newProfit > 0:
                    profitsSet.add(dp(profit+newProfit ,ind+1)-profit)
            i += 1
        maxProfit[0] = max(maxProfit[0], profit)
    dp(0, 0)
    return maxProfit[0]

prices = [3,2,6,5,0,3]
res = maxProfit(prices)
print(res)
