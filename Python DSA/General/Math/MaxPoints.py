from collections import defaultdict

def maxPoints(points):
    length = len(points)
    if length == 1:
        return 1
    i = 0
    ans = 0
    while i < length:
        slopes = defaultdict(int)
        curX, curY = points[i]
        for x, y in points[:i]+points[i+1:]:
            diffY = y - curY
            diffX = x - curX
            if diffX == 0:
                m = "inf"
            else:
                m = diffY/diffX
            slopes[m] += 1
        ans = max(ans, max(slopes.values()))
        i += 1
    return ans + 1


points = [[0, 0]]
res = maxPoints(points)
print(res)