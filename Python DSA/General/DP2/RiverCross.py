from collections import defaultdict

def canCross(stones):
    river = defaultdict(int)
    for n in stones:
        river[n] = 1
    memo = {}
    def f(i, prev, last):
        if i == last: return True
        if prev == 0 or river[i] == 0:
            return False
        if (i, prev) in memo: return memo[(i, prev)]
        canJump = False
        for j in range(prev-1, prev+2):
            canJump = f(i+j, j, last)
            if canJump: break

        memo[(i, prev)] = canJump
        return canJump

    return f(1, 1, max(stones))

stones = [0,1,2147483647]
res = canCross(stones)
print(res)