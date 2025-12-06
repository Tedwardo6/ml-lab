
FIB_TERMS = 10

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    x = fibonacci(n-1) + fibonacci(n-2)
    return x

for i in range(1, FIB_TERMS+1):
    print(fibonacci(i))