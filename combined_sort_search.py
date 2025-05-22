# combined_sort_search_custom.py
# Author: Cupcake
# Date: 22 May 2025
# Description: Bubble Sort + Binary Search with custom string output

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):  # Reduce the range as we go
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

def binary_search(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return f"Target found at index {mid}"
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return "Target not found"

# Example usage
dataset = [70, 10, 90, 20, 40, 60]
print("Original List:", dataset)

# Sort the list first
bubble_sort(dataset)
print("Sorted List:", dataset)

# Now search for a target
target = 40
result = binary_search(dataset, target)
print(result)  # Output: Target found at index 2 (or similar depending on sorting)
