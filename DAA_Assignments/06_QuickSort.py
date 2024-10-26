import random


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# Deterministic Quicksort
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


# Randomized Quicksort
def randomized_partition(arr, low, high):
    rand_idx = random.randint(low, high)
    swap(arr, rand_idx, high)
    return partition(arr, low, high)

def rand_quicksort(arr, low, high):
    if low < high:
        q = randomized_partition(arr, low, high)
        rand_quicksort(arr, low, q-1)
        rand_quicksort(arr, q+1, high)


arr = [5, 4, 3, 2, 1]

rand_quicksort(arr, 0, len(arr)-1)
print(arr)