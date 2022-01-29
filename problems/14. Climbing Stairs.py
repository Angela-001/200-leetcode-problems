def climbStairs(n):
    if n < 3:
        return n

    x, y = 1, 2

    for i in range(1, n - 1):
        x, y = y, x + y

    return y

print(climbStairs(7))

# https://leetcode.com/problems/climbing-stairs/
