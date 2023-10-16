# nums = [2,7,9,3,1,6,10,8]
nums = [1,2,4,6,8]
totalHouses = len(nums)

money = {}

def stealTheMoney(i):
    if i >= totalHouses - 3:
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

money2 = {}

def stealTheMoney2(i):
    if i >= totalHouses - 2:
        money2[i] = nums[i]
        return nums[i]
    if i in money2:
        return money2[i]
    maxMoney = 0
    for j in range(i+2, totalHouses-1):
        m = nums[i] + stealTheMoney2(j)
        if m > maxMoney:
            maxMoney = m
    money2[i] = maxMoney
    return money2[i]
if totalHouses <= 3:
    print(max(nums))
else:
    stealTheMoney(1)
    stealTheMoney(2)
    stealTheMoney2(0)
    print(max(money2[0], money[1], money[2]))
