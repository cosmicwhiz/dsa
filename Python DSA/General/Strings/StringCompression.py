

def compress(chars):
    prev = chars[0]
    count, encoded = 1, [prev]
    def addCount(cnt):
        if cnt > 1:
            for nc in str(cnt):
                encoded.append(nc)
    for c in chars[1:]:
        if c != prev:
            addCount(count)            
            encoded.append(c)
            count = 1
        else:
            count += 1
        prev = c
    addCount(count)
    return len(encoded)


chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
res = compress(chars)
print(res)