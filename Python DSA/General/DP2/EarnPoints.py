def waysToReachTarget(target, types):
    length = len(types)
    memo = {}
    def dp(i, t, n):
        if t == 0: return 1
        if i >= n: return 0
        if (i, t) in memo: return memo[(i, t)]
        mx = min(types[i][0], t // types[i][1])
        ways = 0
        for q in range(mx+1):
            ways += dp(i+1, t-q*types[i][1], n)
        memo[(i, t)] = ways
        return ways
    return dp(0, target, length)


target = 18
types = [[6,1],[3,2],[2,3]]
res = waysToReachTarget(target, types)
print(res)