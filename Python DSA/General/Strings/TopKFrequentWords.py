from collections import OrderedDict

def topKFrequent(words, k):
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    res = []
    freq = sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
    i = 0
    while i < k:
        res.append(freq[i][0])
        i += 1
    return res

words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
k = 4
res = topKFrequent(words, k)
print(res)