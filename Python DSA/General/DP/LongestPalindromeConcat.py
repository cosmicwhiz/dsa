import collections

def longestPalindrome(words):
    c = collections.Counter(words)
    length = 0
    oddFound = False
    visited = set()
    for w in c:
        count = c[w]
        rev = w[::-1]
        if w not in visited:
            if w == rev:
                if count % 2 == 0:
                    length += count * 2
                else:
                    if oddFound:
                        length += (count-1)*2
                    else:
                        length += count * 2
                        oddFound = True
            else:
                length += min(count, c[rev]) * 4
                visited.add(rev)
    return length

words = ["ab","ty","yt","lc","cl","ab",]
res = longestPalindrome(words)
print(res)