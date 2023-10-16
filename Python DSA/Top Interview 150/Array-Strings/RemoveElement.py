'''
    Time Complextiy: O(n)
    Space Complexity: O(1)
'''
def removeElement(nums, val):
    l, r = 0, len(nums) - 1
    count = 0
    while l <= r:
        if nums[l] == val:
            while l <= r and nums[r] == val:
                r -= 1
            if l > r: return count
            nums[l], nums[r] = nums[r], nums[l]
            r -= 1
        count += 1
        l += 1
    print(nums)
    return count

'''
    Time Complextiy: O(n)
    Space Complexity: O(1)
'''
def removeElement_alt1(nums, val):
    index = 0
    for n in nums:
        if n != val:
            nums[index] = n
            index += 1
    print(nums)
    return index

'''
    Time Complextiy: O(n)
    Space Complexity: O(n)
'''
def removeElement_alt2(nums, val):
    nums[:] = [num for num in nums if num != val]
    return len(nums)

nums = [0,1,2,2,3,0,4,2]
val = 2
res = removeElement(nums, val) == removeElement_alt1(nums, val)
print(res)