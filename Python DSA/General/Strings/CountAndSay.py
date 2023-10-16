def countAndSay(n: int) -> str:
    if n == 1:
        return "1"
    numstr = countAndSay(n-1)
    prev = numstr[0]
    res = ""
    count = 1
    for s in numstr[1:]:
        if s != prev:
            res += str(count)+prev
            prev = s
            count = 1
        else:
            count += 1
    res += str(count)+prev
    return res