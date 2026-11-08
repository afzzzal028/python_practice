"""
ML relevance: Dataset manipulation — selecting specific samples, extracting features and changing data dimensions.

"""

"""
1. Indexing
Indexing means accessing a specific element from an array.

Python uses zero-based indexing, meaning the first element has index 0."""
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])  # 10
print(arr[2])  # 30
print(arr[-1]) # 50

#For a 2D array, use two indices: [row, column].

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(data[0, 1])  # 20
print(data[2, 0])  # 70
print(data[1, 2])  # 60


# 2. Slicing
# Slicing extracts a portion of an array.
#Syntax
#array[start:stop:step]

arr = np.array([10, 20, 30, 40, 50, 60])

print(arr[1:4])

arr[:3]    # First three elements
arr[2:]    # From index 2 to the end
arr[::2]   # Every second element
arr[::-1]  # Reverse the array

#Slicing a 2D array

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(data[0:2, 1:3])


# 3. Reshaping
# Reshaping changes the dimensions of an array without changing its elements.

arr = np.arange(1, 7)

new_arr = arr.reshape(2, 3)

print(new_arr)

