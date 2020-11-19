def factorial(x, ans = 1):
    if x == 0:
        return ans
    x = ans * x
    x -= 1
    factorial(x, ans)