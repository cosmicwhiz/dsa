def decodeString(s):
    length = len(s)
    i = 0
    while i < length:
        if s[i] == ']':
            w = ""
            k, wlen = i-1, 0
            while s[k] != '[':
                wlen += 1
                w += s[k]
                k -= 1
            w = w[::-1]
            num, nlen = 0, 0
            try:
                num = int(s[k-1])
                nlen = 1
                num = int(s[k-2:k])
                nlen = 2
                num = int(s[k-3:k])
                nlen = 3
            except:
                pass
            s = s[:k-nlen] + (w * num) + s[i+1:]
            lengthFactor = (num-1) * wlen - (2+nlen)
            i += lengthFactor
            length += lengthFactor
            continue
        i += 1
    return s

def decodeStringAlt(s):
    stack = []; curNum = 0; curString = ''
    for c in s:
        if c == '[':
            stack.append(curString)
            stack.append(curNum)
            print(stack)
            curString = ''
            curNum = 0
        elif c == ']':
            num = stack.pop()
            prevString = stack.pop()
            print(stack)
            curString = prevString + num*curString
        elif c.isdigit():
            curNum = curNum*10 + int(c)
        else:
            curString += c
    return curString

s = "3[3[c]]"
res = decodeStringAlt(s)
print(res)
