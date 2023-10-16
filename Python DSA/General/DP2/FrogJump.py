def kJumps(k, heights):
    length = len(heights)
    dp = [-1]*length
    dp[0] = 0
    for i in range(1, length):
        minEnergy = float("inf")
        for j in range(1, k+1):
            index = i-j
            if index >= 0:
                jump = dp[index]+abs(heights[i]-heights[index])
                minEnergy = min(minEnergy, jump)
        dp[i] = minEnergy
    return dp[-1]


heights = [10,20,35,40,20,10,25]
k = 5
res = kJumps(k, heights)
print(res)