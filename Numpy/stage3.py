"""Stage 3: NumPy Vectorization and Broadcasting"""

#Vectorization

#Vectorization means applying an operation to an entire NumPy array instead of processing each element individually using a loop.

#withour vectorization it take lots of iteration using for loop to put an operation on an array

import numpy as np
arr= np.array([10,20,30,40])

result=arr*2
print(result)

print(arr + 5)   # [15 25 35 45]
print(arr - 5)   # [ 5 15 25 35]
print(arr * 3)   # [30 60 90 120]
print(arr / 10)  # [1. 2. 3. 4.]
print(arr ** 2)  # [100 400 900 1600]

#we can perform an operation on two arrays

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(a + b)
print(a * b)


"""2. Broadcasting"""

#Broadcasting allows NumPy to perform operations between arrays of different but compatible shapes.

arr = np.array([10, 20, 30])

print(arr + 5)

#it goes like this [10,20,30]+[5,5,5]

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

add = np.array([1, 2, 3])

print(arr + add)

"""
umPy adds [1, 2, 3] to every row.
Broadcasting rules
NumPy compares array dimensions from right to left.

Two dimensions are compatible when:
1. They are equal, or
2. One of them is 1.
"""

a = np.array([[1], [2], [3]])  # Shape (3, 1)
b = np.array([10, 20, 30, 40]) # Shape (4,)

print(a + b)


"""3. Why this matters in Machine Learning"""
#Suppose a model predicts house prices and you want to calculate prediction errors.

actual = np.array([100, 200, 300, 400])
predicted = np.array([110, 190, 310, 380])

errors = actual - predicted

print(errors)

#You can calculate squared errors:

squared_errors = errors ** 2

print(squared_errors)


"""Practice"""
#Create a NumPy array `[2, 4, 6, 8, 10]`. Multiply every element by 5 without using a loop.
arr=np.array([2,34,6,8,10])

result=arr*5
print(result)

#Given `a = np.array([10, 20, 30])` and `b = np.array([1, 2, 3])`, calculate their element-wise sum and product.
a=np.array([10,20,30])
b=np.array([1,2,3])
print(a+b)
print(a*b)

#Create a 2D array `[[10,20,30],[40,50,60]]`. Add `[5,10,15]` to every row using broadcasting.

arr=np.array([[10,20,30],
              [40,50,60]])

arr2=np.array([5,10,15])
print(arr+arr2)