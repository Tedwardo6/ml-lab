def factorial(n):
    x = 0
    y = n 
    for i in range(1, n):
        x = y * (n-i)
        y = x
    return y

print(factorial(3))