def asteroidCollision(asteroids):
    length = len(asteroids)
    i = 0
    while asteroids[i] < 0:
        i += 1
    stack = []
    while i < length:
        while asteroids[i] > 0:
            stack.append(asteroids[i])
            i += 1
        prev = None
        while stack and abs(stack[-1]) <= abs(asteroids[i]):
            prev = stack[-1]
            stack.pop()
        if not stack and prev and prev != -asteroids[i]:
            stack.append(asteroids[i])
        i += 1
    return stack

asteroids = [8,-8, 2, 1, -5, 9, -4, -3, 6, -2]
res = asteroidCollision(asteroids)
print(res)