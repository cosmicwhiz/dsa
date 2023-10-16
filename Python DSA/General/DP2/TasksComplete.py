def minimumTime(tasks):
    timeOn = [False]*2001
    tasks = sorted(tasks, key=lambda t:t[1])

    for st,end,dur in tasks:
        for t in range(st, end+1):
            if timeOn[t]: dur -= 1
        i = end
        while dur > 0:
            if timeOn[i]:
                i -= 1
                continue
            timeOn[i] = True
            dur -= 1
            i -= 1
    return sum(timeOn)