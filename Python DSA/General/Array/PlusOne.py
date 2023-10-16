def plusOne(digits, numSys):
    if numSys == 2:
        limit = 1
    elif numSys == 10:
        limit = 9
    digits[-1] += 1
    i = len(digits)-1
    while i > 0:
        if digits[i] > limit:
            digits[i] = 0
            digits[i-1] += 1
        i -= 1
    if digits[i] > limit:
        digits[i] = 0
        digits = [1] + digits
    return digits

digits = [1, 0, 1]
numSys = {'binary': 2, 'decimal': 10}
res = plusOne(digits, numSys['binary'])
print(res)