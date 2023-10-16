import sys

sys.setrecursionlimit(10000)

def largestRectangleArea(heights):
    totalBars = len(heights)
    minimums = set()
    def dp(i, curMin, length, area):
        if i == totalBars:
            minimums.add(curMin)
            return area
        h = heights[i]
        if h in minimums:
            return area
        if h == 0:
            return area
        curMin = min(curMin, h)
        area = max(area, curMin*length)
        return dp(i+1, curMin, length+1, area)
    
    areas = set()
    for i in range(len(heights)):
        a = dp(i, 1e+6, 1, 0)
        areas.add(a)
    return max(areas)

heights = [2,1,4,5,1,3,3]
res = largestRectangleArea(heights)
print(res)