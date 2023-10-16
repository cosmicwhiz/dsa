def tribonacci(n):
    tribo = [-1]*37
    tribo[0] = 0
    tribo[1] = tribo[2] = 1
    def nthTri(num):
        if tribo[num] != -1:
            return tribo[num]
        tribo[num] = nthTri(num-1) + nthTri(num-2) + nthTri(num-3)
        return tribo[num]
    return nthTri(n)


for i in range(100):
    print(tribonacci(int(i)))