import numpy as np
number=np.array([10,20,30,40])
print(number)

#2-d Array

numbers=np.array([
    [10, 20],
    [30, 40]
])

print(numbers)
"""Usefull Array Method"""
np.zeros((2, 3))       # 2x3 array filled with 0
np.ones((2, 3))        # 2x3 array filled with 1
np.full((2, 3), 7)     # 2x3 array filled with 7
np.arange(1, 10)       # Numbers from 1 to 9
np.eye(3)              # 3x3 identity matrix


numbers=np.eye(3)
print(numbers)

numbers=np.array([
    [10, 20],
    [30, 40]
])

print(numbers.ndim)
print(numbers.shape)
print(numbers.dtype)
print(numbers.size)