# fibonacci series

def fib(n):
    if n==0 or n==1:
        return n
    if n > 1:
        return fib(n-1) + fib(n-2)

def fib_iter(n):
    fib0 = 0
    fib1 = 1

    if n==0 or n==1:
        return n
    
    for i in range(n-1):
        fib1 = fib1 + fib0
        fib0 = fib1 - fib0
        
    return fib1

arr=[]
for i in range(10):
    arr.append(fib(i))
print(arr)
