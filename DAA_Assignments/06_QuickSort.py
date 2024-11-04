import random
import time

'''
All elements to the left of pivot are less than it and all elements to the
right of it are greater. This means that pivot element is on the correct position 
in the array.

Partition returns the index of the pivot element after putting/swapping it to its
correct position (i + 1).

1. Deterministic Quicksort - 
Time Complexity = Best & Avg case O(nlog n), worst O(n^2)
Space Complexity = Avg case O(log n), worst O(n)

2. Randomized Quicksort - *same as Deterministic*

Main Difference - Randomized Quicksort reduces the likelihood of getting the
worst case O(n^2) by randomly selecting pivots, which makes it more reliable.
Randomized has an advantage in practice because the random pivot choice makes it
less dependent on input ordering.

'''

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
    global call_count
    call_count += 1

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
    global call_count
    call_count += 1

    if low < high:
        q = randomized_partition(arr, low, high)
        rand_quicksort(arr, low, q-1)
        rand_quicksort(arr, q+1, high)


def analyze_quicksort(arr, low, high, rand=False):
    global call_count
    call_count = 0

    start_time = time.time()
    if rand==True:
        rand_quicksort(arr, low, high)
    else:
        quicksort(arr, low, high)
    end_time = time.time()

    time_taken = end_time - start_time

    print(f"Sorted Array: {arr}\n")
    print(f"Time taken: {time_taken}")
    print(f"Number of recursive calls: {call_count}")


arr = [random.randint(0, 100) for _ in range(1000)]
n = len(arr)
analyze_quicksort(arr, 0, n-1, rand=True)


