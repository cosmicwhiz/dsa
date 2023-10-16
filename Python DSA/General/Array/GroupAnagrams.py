def groupAnagrams(strs):
    group = defaultdict(list)
    for w in strs:
        letter = defaultdict(int)
        for c in sorted(w):
            letter[c] += 1
        group[tuple(list(letter.items()))].append(w)
    return group.values()

strs = ["eat","teea","tan","ate","nat","bat"]
res = groupAnagrams(strs)
print(res)