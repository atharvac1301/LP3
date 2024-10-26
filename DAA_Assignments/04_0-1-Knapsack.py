profit = [60, 100, 120]
weight = [100, 20, 30]
W = 50
n = len(profit)

# t is weight-item matrix
t = [[-1 for i in range(W+1)] for j in range(n+1)]

# Dynamic Programming = Recursion + Memoization
def knapsack(wt, val, W, n):
    if n==0 or W==0:
        return 0
   
    if t[n][W] != -1:
        return t[n][W]
    
    if wt[n-1] <= W:
        t[n][W] = max(val[n-1]+knapsack(wt, val, W-wt[n-1], n-1), knapsack(wt, val, W, n-1))
        return t[n][W]
    elif wt[n-1] > W:
        t[n][W] = knapsack(wt, val, W, n-1)
        return t[n][W]

print(knapsack(weight, profit, W, n))


