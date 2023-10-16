from collections import Counter
import random

def awesomeStringAlt(s):
    # Time Limit Exceeded
    maxLen = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            temp = s[i:j+1]
            c = Counter(temp)
            oddVal = 0
            for v in c.values():
                if v % 2 != 0:
                    oddVal += 1
                if oddVal > 1:
                    break
            if oddVal == 1:
                maxLen = max(maxLen, sum(c.values()))
    return maxLen

def awesomeString(s):
    # Time Complexity = O(An) where A = 10
    n = len(s)
    ans, mask = 0, 0
    
    memo = [n] * 1024
    memo[0] = -1
    
    for i in range(n):
        mask ^= 1 << int(s[i])
        
        # Case 1. Check if we have seen similar mask
        ans = max(ans, i - memo[mask])
        
        # Case 2. Check for masks that differ by one bit
        for j in range(10):
            test_mask = mask ^ (1 << j)
            ans = max(ans, i - memo[test_mask])
            
        # save the earliest position
        memo[mask] = min(memo[mask], i)    
    
    return ans