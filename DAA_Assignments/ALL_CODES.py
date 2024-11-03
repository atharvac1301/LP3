'''
Assignment 1 - Fibonacci (Recursive + Iterative)
'''

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
# print(arr)


'''
Assignment 2 - Huffman Coding 
'''
from heapq import heappush, heappop

class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq 
        self.left = left
        self.right = right

        # Huffman code for Tree traversal direction (0/1 for left/right)
        self.huff = ''
    
    def __lt__(self, next):
        return self.freq < next.freq
        
char = ['a', 'b', 'c', 'd', 'e', 'f'] 
freq = [50, 10, 30, 5, 3, 2] 

def printNodes(node, val=''):
    new_val = val + str(node.huff)

    if node.left:
        printNodes(node.left, new_val)
    if node.right:
        printNodes(node.right, new_val)
    else:
        print(f"{node.char} -> {new_val}")

nodes = []

for i in range(len(char)):
    heappush(nodes, Node(char[i], freq[i]))

while len(nodes) > 1:
    left = heappop(nodes)
    right = heappop(nodes)
    
    left.huff = 0
    right.huff = 1

    newNode = Node(left.char + right.char, left.freq + right.freq, left, right)
    
    heappush(nodes, newNode)

# printNodes(nodes[0])


'''
Assignment 3 - 0-1 Knapsack using DP
'''
profit = [5, 4, 8, 6]
weight = [1, 2, 4, 5]
W = 5
n = len(profit)

# weight-item matrix
t = [[-1 for j in range(W+1)] for i in range(n+1)]

def knapsack(wt, val, W, n):
    if W==0 or n==0:
        return 0

    if t[n][W] != -1:
        return t[n][W]

    if wt[n-1] <= W:
        t[n][W] = max(val[n-1] + knapsack(wt, val, W-wt[n-1], n-1), knapsack(wt, val, W, n-1))
        return t[n][W]
    
    elif wt[n-1] > W:
        t[n][W] = knapsack(wt, val, W, n-1)
        return t[n][W]

# print(knapsack(weight, profit, W, n))


'''
Assignment 4 - NQueens with a Preplaced Queen
'''

n=4

def display(board):
    for row in board:
        print(row)
    print()


def isSafe(board, row, col):
    
    # Check entire column
    for i in range(n):
        if board[i][col] in (1, 2):
            return False
    
    # Check Top-right and Top-left diagonals
    for k in range(1, row+1):
        if row-k >=0 and col-k >= 0 and board[row-k][col-k] in (1, 2):
            return False
        if row-k >=0 and col+k < n and board[row-k][col+k] in (1, 2):
            return False
    
    # Check Bottom-right and Bottom-left diagonals
    for k in range(1, n-row):
        if row+k < n and col-k >= 0 and board[row+k][col-k] in (1, 2):
            return False
        if row+k < n and col+k < n and board[row+k][col+k] in (1, 2):
            return False
    
    return True


def n_queens(board, row, preplaced_row):
    if row==n:
        display(board)
        return

    if row == preplaced_row:
        n_queens(board, row+1, preplaced_row)


    for col in range(n):
        if isSafe(board, row, col):
            board[row][col] = 1
            n_queens(board, row+1, preplaced_row)
            board[row][col] = 0


board = [[0 for i in range(n)] for j in range(n)]
R, C = 2, 3
board[R][C] = 2

# n_queens(board, 0, R)


'''
Assignment 5 - QuickSort (Deterministic & Randomized)
'''

import random

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr, low, high):
    pivot = arr[high]
    i = low-1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            swap(arr, i, j)
    swap(arr, i+1, high)
    return i+1

def quicksort(arr, low, high):
    if low < high:
        q = partition(arr, low, high)
        quicksort(arr, low, q-1)
        quicksort(arr, q+1, high)


def rand_partition(arr, low, high):
    rand_idx = random.randint(low, high)
    swap(arr, rand_idx, high)
    return partition(arr, low, high)

def rand_quicksort(arr, low, high):
    if low < high:
        q = rand_partition(arr, low, high)
        rand_quicksort(arr, low, q-1)
        rand_quicksort(arr, q+1, high)

# arr = [3, 2, 1, 100, 11, 12]
# rand_quicksort(arr, 0, len(arr)-1)
# print(arr)



