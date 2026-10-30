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

#create an array 
a= arr.array("i", [1,2,3,4,5])
for i in range (0,3):
    print(a[i], end=" \n") #printing the first 3 elements of the array

a= arr.array("i", [1,2,3,4,5])
print(*a) #printing all the elements of the array
a.insert(2, 10) #inserting a new element at index 2
print(*a) #printing all the elements of the array after inserting a new element