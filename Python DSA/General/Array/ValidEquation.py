import random

def equationsPossible(equations):
    variables = {}
    val1, val2 = 1, 1
    letters = "abcdefghijklmnopqrstuvwxyz"
    value = {}
    for i,c in enumerate(letters):
        value[c] = i+1

    for eq in equations:
        a, b = eq[0], eq[3]
        condition = eq[1:3]

        if a not in variables and b in variables:
            if condition == "==":
                variables[a] = variables[b]
            else:
                variables[a] = value[a]
        elif b not in variables and a in variables:
            if condition == "==":
                variables[b] = variables[a]
            else:
                variables[b] = value[b]
        elif a not in variables and b not in variables:
            if condition == "==":
                variables[a] = variables[b] = value[a]
            else:
                variables[a] = value[a]
                variables[b] = value[b]            
        print(variables)
        if condition == "==":
            if variables[a] != variables[b]:
                return False
        else:
            if variables[a] == variables[b]:
                return False
    return True

equations = []
variables = "abcde"
conditions = ["==", "!="]

for i in range(4):
    var1 = variables[random.randint(0, len(variables)-1)]
    ind = variables.index(var1)
    newarr = variables[:ind] + variables[ind+1:]
    var2 = newarr[random.randint(0, len(newarr)-1)]
    condition = conditions[random.randint(0, 1)]
    eq = var1 + condition + var2
    equations.append(eq)
print(equations)
res = equationsPossible(equations)
print(res)