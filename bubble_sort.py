# bubble_sort.py
# Author: raksha shetty
# Date: 22 May 2025
# Description: Program to sort a list using Bubble Sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Optimization: stop if already sorted
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

# Example usage
numbers = [50, 20, 40, 10, 30]
bubble_sort(numbers)
print("Sorted list:", numbers)  # Output: [10, 20, 30, 40, 50]
