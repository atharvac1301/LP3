'''
Time and Space Complexity = O(n*W), n*W = dimensions of the Table, 
n = no. of items, W = capacity of Knapsack 
'''

profit = [5, 4, 8, 6]
weight = [1, 2, 4, 5]
W = 5
n = len(profit)

# t is weight-item matrix
t = [[-1 for j in range(W+1)] for i in range(n+1)]

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


