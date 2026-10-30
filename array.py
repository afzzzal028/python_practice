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
print(a[0]) #printing the first element of the array

a.remove(10) #removing the element 10 from the array
a.pop(1) #removing the element at index 1 from the array

"""Slicing of an array"""

"""
Elements from beginning to a range use [:Index]
Elements from end use [:-Index]
Elements from specific Index till the end use [Index:]
Elements within a range, use [Start Index:End Index]
Print complete List, use [:]
For Reverse list, use [::-1]

"""

a= [1,2,3,4,5,6,7,8,9,10]
b=arr.array("i", a)
res = b[3:7] #slicing the array from index 3 to 6
print(res)

"""Searching in Array"""

a= arr.array("i", [1,2,3,4,5,6,7,8,9,10])
print(a.index(5)) #searching for the index of element 5 in the array

"""Updating an Array"""

a=arr.array("i", [1,2,3,4,5])

a[0]=10 #updating the first element of the array to 10
print(a)

"""Opeartion On Array"""

import array as arr
a=arr.array("i", [1,2,3,4,5,2,2,2])
count=a.count(2)
print(count) #printing the count of elements in the array

reverse= a[::-1]
print(reverse) #printing the reverse of the array
reverse=a.reverse() #reversing the array
print(a) #printing the reversed array

a.extend([4,5,6,7])
print(a)