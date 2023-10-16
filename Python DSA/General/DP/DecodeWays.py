import time

start = time.time()
def numDecodings(s):
    encodings = {}
    letters = "JKLMNOPQRSTUVWXYZ"
    for i,c in enumerate(letters):
        encodings[str(i+10)] = c
    validPath = {}

    def findWays(i):
        if i >= len(s):
            return 1
        p1, p2 = 0, 0
        if s[i] != "0":
            if i in validPath:
                p1 = validPath[i]
            else:
                p1 = findWays(i+1)
                validPath[i] = p1
        if i < len(s)-1 and s[i]+s[i+1] in encodings:
            if (i, i+1) in validPath:
                p2 = validPath[(i, i+1)]
            else:
                p2 = findWays(i+2)
                validPath[(i, i+1)] = p2
        return p1+p2

    totalWays = findWays(0)
    return totalWays

s = "06"
res = numDecodings(s)
end = time.time()

print(res)
print("Time Elapsed:",end-start,"seconds")
