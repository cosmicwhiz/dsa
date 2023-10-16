def minimumTime(time, totalTrips):
    l, r = 1, max(time)*totalTrips
    trips = 0
    while l <= r:
        trips = 0
        mid = (l+r) // 2
        print(l, r, mid)
        for t in time:
            trips += (mid // t)
        print(trips)
        if trips < totalTrips:
            l = mid + 1
        else:
            r = mid - 1
    if trips >= totalTrips: return mid
    return mid + 1

time = [1,2,3]
totalTrips = 5
res = minimumTime(time, totalTrips)
print(res)