def minStickers(stickers, target):
    
    subSeq = {}
    def dp(sticks, target):
        print("Recursion...")
        if target in subSeq:
            if subSeq[target] != -1:
                return subSeq[target] + 1
            return -1
        if not target:
            return 1
        t = target
        arr = sticks.copy()
        stickersCount = set()
        for word in sticks:
            print(word, target, arr)
            found = False
            for c in word:
                if c in t:
                    i = t.index(c)
                    t = t[:i] + t[i+1:]
                    found = True
            if found:
                print(word)
                res = dp(arr, t)
                if res != -1:
                    stickersCount.add(res)
            else:
                arr.pop(arr.index(word))
            t = target
        if not stickersCount:
            subSeq[target] = -1
            return -1
        else:
            subSeq[target] = min(stickersCount)
        print(subSeq)
        return subSeq[target] + 1

    dp(stickers, target)
    return subSeq[target]

stickers = ["notice", "possible"]
target = "basicbasic"
res = minStickers(stickers, target)
if res:
    print(res)
