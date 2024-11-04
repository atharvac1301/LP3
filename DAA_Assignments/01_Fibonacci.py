# fibonacci series
'''
1. Recursive Fibonacci - Time Complexity = O(2^n), Space Complexity = O(n)
2. Iterative Fibonacci - Time Complexity = O(n), Space Complexity = O(1)

The recursive algorithm has exponential time complexity because it repeatedly 
calculates the same subproblems. Each call to fib(n) requires two recursive calls, 
fib(n-1) and fib(n-2), resulting in a branching pattern similar to a binary tree.

The space complexity is O(n) due to the maximum depth of the call stack, which 
grows linearly with n. For each call to fib(n), the function holds a new frame 
in memory until reaching the base cases, creating a stack of up to n frames.


The iterative algorithm has linear time complexity since it computes each 
Fibonacci number from fib(0) up to fib(n) in a single pass, iterating n-1 times.

The space complexity is O(1) because the iterative algorithm only uses a 
fixed amount of memory to store a few variables (fib0, fib1, and i), 
regardless of n.
'''

import time

call_count = 0

def fib(n):
    global call_count
    call_count += 1

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

def analyze_fib(n):
    global call_count
    call_count = 0

    start_time = time.time()
    result = fib(n)
    end_time = time.time()

    time_taken = end_time - start_time

    print(f"Result: {result}")
    print(f"Time Taken: {time_taken}")
    print(f"Function call count : {call_count}")


def analyze_fib_iter(n):
    start_time = time.time()
    result = fib_iter(n)
    end_time = time.time()

    time_taken = end_time - start_time

    print(f"Result: {result}")
    print(f"Time Taken: {time_taken}")
    

analyze_fib_iter(1000)