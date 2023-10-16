from collections import defaultdict

def printVertically(s):
    words = defaultdict(str)
    count, wc = 0, 0
    prev = ""
    for c in s:
        if c == " ":
            count = 0
            if prev != " ":
                wc += 1
            prev = c
            continue
        i = len(words[count])
        if i < wc:
            for j in range(i, wc):
                words[count] += " "
        words[count] += c
        count += 1
        prev = c
    return list(words.values())