import heapq
import random

def minTimeToRemoveSol(colors, neededTime):
    ans = 0
    heapq.heapify(neededTime)
    for i in range(1, len(colors)):
        # if the i-th balloon has the same color as (i - 1)th one
        # e.g. aba[a]c and i = 3 (0-based)
        if colors[i] == colors[i - 1]:
            # then we remove the one with less time
            # e.g. in above example, we remove the balloon at index 2 
            # with neededTime[2] since neededTime[2] < neededTime[3] 
            ans += min(neededTime[i], neededTime[i - 1])
            # update the max neededTime inplace 
            # or alternatively you can store it in a variable
            neededTime[i] = max(neededTime[i], neededTime[i - 1])
    return ans

def minTimeToRemove(colors, times):
    prev = colors[0]
    sameIndices = []
    heapq.heappush(sameIndices, times[0])
    balloonArr = []

    for i in range(1, len(colors)):
        if colors[i] != prev:
            if len(sameIndices) > 1:
                balloonArr.append(sameIndices)
            sameIndices = []
        heapq.heappush(sameIndices, times[i])
        prev = colors[i]
    if len(sameIndices) > 1:
        balloonArr.append(sameIndices)
    minTime = 0
    for times in balloonArr:
        while len(times) > 1:
            t = heapq.heappop(times)
            minTime += t

    return minTime

startTesting = True

letters = "a"
totalTests = 5000
testsPassed = 0

if startTesting:
    for test in range(totalTests):
        colors = ""
        times = []
        size = random.randint(30, 50)
        for i in range(size):
            colors += random.choice(letters)
            times.append(random.randint(1, 9))
        print("Generated Data...")
        print(colors, " ", times)
        print("Answer:",minTimeToRemoveSol(colors, times))
        if minTimeToRemoveSol(colors, times) == minTimeToRemove(colors, times):
            testsPassed += 1
            print("✅ Test Passed\n")
        else:
            break
    print("Tests Passed:",testsPassed,"/",totalTests)
