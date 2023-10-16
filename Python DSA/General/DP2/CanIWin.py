def canIWin(maxChoosableInt, desTotal):
    memo = {}
    def f(turn, choices, clen, total):
        if clen == 0: return False
        if total <= max(choices):
            if turn: return True
            return False
        if (turn, choices) in memo: return memo[(turn, choices)]
        win = False
        for i in range(clen):
            temp = choices[:i] + choices[i+1:]
            win = f(abs(turn-1), temp, clen-1, total-choices[i])
            if win: break
        memo[(turn, choices)] = win
        return win
    avlChoices = [n for n in range(1, maxChoosableInt+1)]
    return f(1, tuple(avlChoices), maxChoosableInt, desTotal)

maxChoosableInt, desTotal = 15, 56
res = canIWin(maxChoosableInt, desTotal)
print(res)