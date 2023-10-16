nums = [2,7,9,3,1,6,10,8]
# nums = [1,2]
totalHouses = len(nums)

money = {}

def stealTheMoney(i):
    if i >= totalHouses - 2:
        money[i] = nums[i]
        return nums[i]
    if i in money:
        return money[i]
    maxMoney = 0
    for j in range(i+2, totalHouses):
        m = nums[i] + stealTheMoney(j)
        if m > maxMoney:
            maxMoney = m
    money[i] = maxMoney
    return money[i]

if totalHouses <= 2:
    print(max(nums))
else:
    stealTheMoney(0)
    stealTheMoney(1)
    print(max(money[0], money[1]))
