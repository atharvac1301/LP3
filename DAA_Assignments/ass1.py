# fibonacci series

def fibonacci_rec(n):
    f0 = 0
    f1 = 1
    if n < 0:
        return "Invalid"
    elif n==0:
        return 0
    elif n==1:
        return 1
    return fibonacci_rec(n-1) + fibonacci_rec(n-2)

def fibonacci_iter(n):
    f0 = 0
    f1 = 1
    if n < 0:
        return "Invalid"
    elif n==0:
        return 0
    elif n==1:
        return 1
    
    temp = None
    for i in range(2, n+1):
        temp = f0 + f1
        f0 = f1
        f1 = temp
    return temp

n=7
print("Fibonacci Recursive:", fibonacci_rec(n))
print("Fibonacci Iterative:", fibonacci_iter(n))
