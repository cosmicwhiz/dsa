def sellingWoodAlt(m, n, prices):
    dimension = {}
    [dimension.setdefault(i, n) for i in range(m)]
    board = []
    
    def dp(d):
        pset = {0}
        for h, w, p in prices:
            canCut = False
            tempd = d.copy()
            for i in range(m):
                if tempd[i] >= w:
                    skip = False
                    # check if sufficient height available
                    for k in range(i, i+h):
                        if k not in tempd or tempd[k] < w:
                            skip = True
                            break
                    if skip:
                        break
                    # cut out that piece
                    for j in range(i, i+h):
                        tempd[j] -= w
                        canCut = True
                    break
            if canCut:
                # save the profit of
                earning = dp(tempd) + p
                board.append((d, earning))
                pset.add(earning)
            else:
                board.append((tempd, 0))
        
        return max(pset)
    return dp(dimension)

def sellingWood(m, n, prices):
    dimension = [n] * m
    board = {}
    
    def dp(d):
        dTuple = tuple(d)
        if dTuple in board:
            return board[dTuple]
        pset = {0}
        for h, w, p in prices:
            canCut = False
            tempd = d.copy()
            for i in range(m):
                if tempd[i] >= w:
                    skip = False
                    # check if sufficient height available
                    for k in range(i, i+h):
                        if k >= m or tempd[k] < w:
                            skip = True
                            break
                    if skip:
                        break
                    # cut out that piece
                    for j in range(i, i+h):
                        tempd[j] -= w
                        canCut = True
                    break
            if canCut:
                # save the profit of
                earning = dp(tempd) + p
                pset.add(earning)
        
        mp = max(pset)
        board[dTuple] = mp
        return max(pset)

    return dp(dimension)
    

m = 4
n = 6
prices = [[3,2,10],[1,4,2],[4,1,3]]
res = sellingWood(m, n, prices)
print(res)