nums = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]

newQuery = {}
for i,j in queries:
    if j in newQuery:
        newQuery[j].append(i)
    else:
        newQuery[j] = [i]
print(newQuery)

queryExeOrder = []
for i,j in queries:
    queryExeOrder.append(j)
print(queryExeOrder)

evenSum = 0
for n in nums:
    if n%2 == 0:
        evenSum += n
res = []
for i in queryExeOrder:
    num = newQuery[i].pop(0)
    if nums[i] % 2 == 0:
        evenSum -= nums[i]
    nums[i] += num
    if nums[i] % 2 == 0:
        evenSum += nums[i]
    res.append(evenSum)
print(res)