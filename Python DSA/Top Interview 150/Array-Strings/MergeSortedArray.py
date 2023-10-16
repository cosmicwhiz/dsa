"""
    Time Complexity: O(m+n)
    Space Complexity: O(1)
"""
def merge(nums1, n, nums2, m):
    i, j, k = n-1, m-1, n+m-1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

"""
    Time Complexity: O(m+n)
    Space Complexity: O(m+n)
"""
def merge_alt1(nums1, n, nums2, m):
    temp = []
    i, j = 0, 0
    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            temp.append(nums1[i])
            i += 1
        else: 
            temp.append(nums2[j])
            j += 1
    while i < m:
        temp.append(nums1[i])
    while j < n:
        temp.append(nums2[j])
    for i in range(m+n):
        nums1[i] = temp[i]


"""
    Time Complexity: O((m+n)log(m+n))
    Space Complexity: O(1)
"""
def merge_alt2(nums1, n, nums2, m):
    for i in range(n):
        nums1[i+m] = nums2[i]
    nums1.sort()

nums1 = [1,2,3,8,0,0,0]
n = 4
nums2 = [2,5,6]
m = 3
merge(nums1, n, nums2, m)
print(nums1)