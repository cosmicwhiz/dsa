def trap(height):
    maxLeft = {}
    maxRight = {}

    def getMaxLefts(i, maxleft):
        if i < len(height):
            maxLeft[i] = maxleft
            if height[i] > maxleft:
                maxleft = height[i]
            getMaxLefts(i+1, maxleft)
        
    def getMaxRights(i, maxright):
        if i >= 0:
            maxRight[i] = maxright
            if height[i] > maxright:
                maxright = height[i]
            getMaxRights(i-1, maxright)

    getMaxLefts(0, 0)
    getMaxRights(len(height)-1, 0)
    
    print(maxLeft)
    print(maxRight)

    totalVol = 0
    for i in range(len(height)):
        if min(maxLeft[i], maxRight[i]) - height[i] > 0:
            totalVol += min(maxLeft[i], maxRight[i]) - height[i]
    return totalVol

height = [4,2,6,3]
print("Total volume stored:",trap(height))
