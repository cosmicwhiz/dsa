def climbingStairs(n):
    prev1, prev2 = 1, 0
    for i in range(1, n+1):
        temp = prev2
        prev2 = prev1
        prev1 = temp + prev2
    return prev1

#dp[n] = ways to reach from 0 to n

n = 6
res = climbingStairs(n)
print(res)