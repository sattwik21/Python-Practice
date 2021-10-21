def romanToInt(romanNum):
    roman_numberals = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
    intNum = 0 # Result variable
    i = 0

    while i < len(romanNum):
        currRomanNum = roman_numberals[romanNum[i]]
        nextRomanNum = roman_numberals[romanNum[min(i+1,len(romanNum) - 1)]]
        # nextRomanNum is romanNum[i+1] in number and if i equals to len(romanNum-1) then it will be romanNum[i]

        if nextRomanNum > currRomanNum:
            intNum += nextRomanNum - currRomanNum
            i += 2
        else:
            intNum += currRomanNum
            i += 1

    return intNum

print(romanToInt('L'))
