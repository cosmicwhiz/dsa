def AltkthPalindrome(queries, intLength):
    # Time Limit Exceeded
    nums1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    nums2 = ['00', '11', '22', '33', '44', '55', '66', '77', '88', '99']

    total = 9 * 10**(intLength // 2)

    temp = sorted(queries, reverse=True)
    limit = temp[0]
    for t in temp:
        if t <= total:
            limit = t
            break

    def formNum(arr, i, length):
        if i == intLength:
            nums1.pop(0)
        elif i > intLength:
            return arr
        newarr = []
        for n in nums1:
            for s in arr:
                newarr.append(n+s+n)
                length += 1
        return formNum(newarr, i+2, length)


    if intLength % 2 == 0:
        p = formNum(nums2, 4, 0)
    else:
        p = formNum(nums1[:], 3, 0)
    if intLength == 2 or intLength == 1:
        total = 9
        p.pop(0)

    return [(p[n-1]) if n <= total else -1 for n in queries]


def kthPalindrome(queries, intLength):
    palindromes = []
    for i in range(10**(intLength//2 - 1), 10**(intLength//2)):
        n = str(i)
        rev = n[::-1]
        p = n + rev
        palindromes.append(p)
    

queries = [1,2,3,5,10,34]
intLength = 14
res = AltkthPalindrome(queries, intLength)
print(res)