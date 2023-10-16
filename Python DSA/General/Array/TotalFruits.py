def totalFruits(fruits):
    length = len(fruits)
    i = 0
    ans = 0
    while i < length:
        j = i
        if length - i <= ans:
            return ans
        fruitSet = set()
        while j < length:
            fruitSet.add(fruits[j])
            if len(fruitSet) >= 3:
                break
            j += 1
        ans = max(j-i, ans)
        i += 1
    return ans


fruits = [1,2,1]
res = totalFruits(fruits)
print(res)
