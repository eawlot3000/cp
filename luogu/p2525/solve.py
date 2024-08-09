#!/usr/bin/env python3
def previous_permutation(arr):
    n = len(arr)

    # Step 1: Find the rightmost ascending pair
    i = n - 2
    while i >= 0 and arr[i] <= arr[i + 1]:
        i -= 1

    if i == -1:
        return "ERROR"

    # Step 2: Find the largest element to the right of i that is smaller than arr[i]
    j = n - 1
    while arr[j] >= arr[i]:
        j -= 1

    # Step 3: Swap the elements at i and j
    arr[i], arr[j] = arr[j], arr[i]

    # Step 4: Reverse the sequence after i
    arr = arr[:i + 1] + arr[i + 1:][::-1]
    
    return arr

# Reading input
n = int(input())
arr = list(map(int, input().split()))

# Get the previous permutation
result = previous_permutation(arr)

# Print the result
if result == "ERROR":
    print(result)
else:
    print(" ".join(map(str, result)))

