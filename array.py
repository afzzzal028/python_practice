import numpy as np
a = np.array([1, 2, 3, 4, 5])
print(a*2) #multiplying each element of the array by 2

a=np.array([[1,2], [3,4]])
print(a*2) # printing the 2D array

import array as arr
a=arr.array('i', [1, 2, 3, 4, 5])
print(a[0]) #printing the first element of the array
a.append(6) #adding a new element to the array
print(a) 