def getRomanDict(data):
    checkRoman = True
    decimalCheck = False
    roman = ""
    decimal = ""
    romanDict = {}
    for c in data:
        if c != ",":
            if checkRoman:
                if c != " ":
                    roman += c
                else:
                    checkRoman = False
            if decimalCheck:
                decimal += c
            if c == "(":
                decimalCheck = True
            if c == ")":
                decimal = decimal[:-1]
                decimalCheck = False
                num = int(decimal)
                if num not in romanDict:
                    romanDict[num] = roman
                decimal = ""
                roman = ""
                checkRoman = True
    return romanDict

def intToRoman(num):
    roman = {
        0: "", 1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX",
        10: "X", 20: "XX", 30: "XXX", 40: "XL", 50: "L", 60: "LX", 70: "LXX", 80: "LXXX", 90: "XC",
        100: "C", 200: "CC", 300: "CCC", 400: "CD", 500: "D", 600: "DC", 700: "DCC", 800: "DCCC", 900: "CM",
        1000: "M", 2000: "MM", 3000: "MMM"
    }

    resArr = []
    tenPow = 1
    while num != 0:
        rem = num % pow(10, tenPow)
        resArr.append(roman[rem])
        tenPow += 1
        num -= rem
    if not resArr:
        resArr.append(roman[num])

    res = ""
    for s in resArr[::-1]:
        res += s
    return res


romanDict = getRomanDict(data)
totalTests = len(romanDict)
testsPassed = 0

for num in romanDict.keys():
    if intToRoman(num) == romanDict[num]:
        testsPassed += 1
    else:
        break

print("Tests Passed:",testsPassed,"/",totalTests)

    
