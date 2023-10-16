from collections import defaultdict

def isScramble(s1, s2):
    length = len(s2)
    pos = defaultdict(int)
    for i, c in enumerate(s2): pos[c] = i
    print(pos)
    def scramble(s):
        curLen = len(s)
        if curLen > 1:
            for i in range(1, curLen):
                left, right = s[:i], s[i:]
                scramble(left)
                scramble(right)
                if pos[left[0]] > pos[right[0]]:
                    s = right + left
                print(s)
                if curLen == length and s == s2: return True
    if scramble(s1): return True
    return False


s1 = "great"
s2 = "rgeat"
res = isScramble(s1, s2)
print(res)