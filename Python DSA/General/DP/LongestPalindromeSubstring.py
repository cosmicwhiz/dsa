
def longestPalindrome(s):

    maxPalindromeLength = [0]
    maxPalindromeIndex = [(0,1)]
    palindromes = {}
    for i in range(len(s)):
        palindromes[(i, i+1)] = s[i]
    def checkPalindrome(startIndex, lastIndex):
        if lastIndex > len(s):
            if startIndex > len(s) - 2:
                return
            checkPalindrome(startIndex+1, startIndex+3)
            return
        
        for k in range(lastIndex, len(s)+1):
            if (startIndex, k) in palindromes:
                lastIndex = k+1
        j = lastIndex-1
        isPalindrome = True
        for i in range((lastIndex-startIndex)//2):
            if s[startIndex+i] != s[j-i]:
                isPalindrome = False
                break
        if isPalindrome:
            palindromes[(startIndex, lastIndex)] = s[startIndex:lastIndex]
            for i in range(startIndex+1, (lastIndex+startIndex)//2):
                print("Adding", (i, lastIndex-i+1))
                palindromes[(i, lastIndex-i+1)] = s[i:lastIndex-i+1]
            if lastIndex-startIndex > maxPalindromeLength[0]:
                maxPalindromeLength[0] = lastIndex-startIndex
                maxPalindromeIndex[0] =  (startIndex, lastIndex)
        checkPalindrome(startIndex, lastIndex+1)
        return

    checkPalindrome(0,2)
    print(palindromes)
    return palindromes[maxPalindromeIndex[0]]


s = "abdbaabdb"
print(longestPalindrome(s))