def minimumTime(ranks, cars):
    memo = {}
    def dp(i, mech, c):
        if i == mech-1: return ranks[i]*c*c
        if (i, c) in memo: return memo[(i, c)]
        time = 1e9
        for n in range(c+1):
            time = min(time, max(ranks[i]*n*n, dp(i+1, mech, c-n)))
        memo[(i, c)] = time
        return memo[(i, c)]

    return dp(0, len(ranks), cars)


ranks = [4,2,3,1]
cars = 10
res = minimumTime(ranks, cars)
print(res)