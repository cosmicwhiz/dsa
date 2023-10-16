def findKthBit(n, k):
    def invert(s):
        bits = {"1": "0", "0": "1"}
        return "".join(bits[c] for c in s)
    
    binary = {1: "0"}
    for i in range(2, n+1):
        prev = binary[i-1]
        binary[i] = prev + "1" + invert(prev)[::-1]
    return binary[n][k-1]

n = 20
k = 1
res = findKthBit(n, k)
print(res)