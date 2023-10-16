def minMutation(start, end, bank):
    mutations = [20]
    def dp(m, gene, arr):
        if gene == end:
            mutations[0] = min(mutations[0], m)
            return
        for g in range(len(arr)):
            count = 0
            for i in range(8):
                if arr[g][i] != gene[i]:
                    count += 1
                if count > 1:
                    break
            if count == 1:
                dp(m+1, arr[g], arr[:g]+arr[g+1:])
            
    dp(0, start, bank)
    return mutations[0]

start = "AACCGGTT"
end = "AAACGGTA"
bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
res = minMutation(start, end, bank)
print(res)
