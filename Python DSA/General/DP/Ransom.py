def canContruct(ransomNote, magazine):
    letters = {}
    for c in magazine:
        if c in letters:
            letters[c] += 1
        else:
            letters[c] = 1
    print(letters)
    
    for c in ransomNote:
        if c in letters:
            letters[c] -=1
        else:
            return False
        
    for c in letters:
        if letters[c] < 0:
            return False
    return True

print(canContruct("aba", "aab"))