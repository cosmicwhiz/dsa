from math import ceil

def minEatingSpeed(piles, h):
    l, r = 1, max(piles)
    time = 0
    while l <= r:
        time = 0
        mid = (l+r) // 2
        print(l, r, mid)
        for n in piles:
            time += ceil(n/mid)
        print(time)
        if time > h:
            l = mid + 1
        else:
            r = mid - 1
    if time <= h: 
        return mid
    return mid + 1
        

piles = [1234570]
h = 1234569
res = minEatingSpeed(piles, h)
print(res)