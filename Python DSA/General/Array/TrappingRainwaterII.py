from typing import List
from collections import defaultdict

def trapRainWater(heightMap: List[List[int]]) -> int:
    rows, cols = len(heightMap), len(heightMap[0])
    eastMax, westMax, northMax, southMax = defaultdict(list), defaultdict(list), defaultdict(list), defaultdict(list)
    
    # get max heights for indices towards all four directions
    def getWestMax():
        for i in range(1, rows-1):
            curMax = heightMap[i][0]
            for j in range(1, cols):
                westMax[i].append(curMax)
                if heightMap[i][j] > curMax: curMax = heightMap[i][j]
    
    def getEastMax():
        for i in range(1, rows-1):
            curMax = heightMap[i][-1]
            for j in range(cols-2, -1, -1):
                eastMax[i].append(curMax)
                if heightMap[i][j] > curMax: curMax = heightMap[i][j]
            eastMax[i] = eastMax[i][::-1]

    def getNorthMax():
        for j in range(1, cols-1):
            curMax = heightMap[0][j]
            for i in range(1, rows):
                northMax[j].append(curMax)
                if heightMap[i][j] > curMax: curMax = heightMap[i][j]
        
    def getSouthMax():
        for j in range(1, cols-1):
            curMax = heightMap[-1][j]
            for i in range(rows-2, -1, -1):
                southMax[j].append(curMax)
                if heightMap[i][j] > curMax: curMax = heightMap[i][j]
            southMax[j] = southMax[j][::-1]

    getWestMax()
    getEastMax()
    getNorthMax()
    getSouthMax()
    # print(eastMax, westMax, northMax, southMax)

    # start checking for the volume that can be collected
    vol = 0
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            curHeight = heightMap[i][j]

            minEW = min(eastMax[i][j], westMax[i][j-1])
            minNS = min(northMax[j][i-1], southMax[j][i])

            diffEW = minEW - curHeight
            diffNS = minNS - curHeight

            if diffEW > 0 and diffNS > 0:
                vol += min(diffEW, diffNS)
    return vol

heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
res = trapRainWater(heightMap)
print(res)
