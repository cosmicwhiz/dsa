def findLongestChain(pairs):
    pairs = sorted(pairs, key=lambda p:p[0])
    length = len(pairs)
    memo = {}
    def dp(i, length):
        if i in memo:
            return memo[i]
        ans = 1
        a, b = pairs[i]
        for j in range(i+1, length):
            c, d = pairs[j]
            if c > b:
                ans = max(ans, 1+dp(j, length))
        memo[i] = ans
        return ans
    
    res = 0
    for i in range(length):
        res = max(res, dp(i, length))
    return res

pairs = [[7,9],[4,5],[7,9],[-7,-1],[0,10],[3,10],[3,6],[2,3]]
res = findLongestChain(pairs)
print(res)