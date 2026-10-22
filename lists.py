#creating lists
mylist = [1, 2, 3, 4, 5]
print(mylist)
mylist2 = ["apple", "banana", "cherry"]
print(mylist2)
#creating list with list constructor
mylist3 = list((1, 2, 3, 4, 5, "afzal"))
print(mylist3)

#creating list with repetition
a=[5]*2
b = [1, 2, 3, 4, 5]*2
print(a)
print(b)

#internal representation of list
a = [1, 2, 3, 4, 5, "afzal"]
print(a[0])
print(a[5][0]) #will print the first character of the string "afzal"

print(a[-1]) #will print the last element of the list

a.append(6) #adding an element to the end of the list
print(a)

a.insert(0, 0) #adding an element at a specific index
print(a)

a.extend([7, 8, 9]) #adding multiple elements to the end of the list
print(a)

a[1]= 10 #changing the value of an element at a specific index
print(a)

a.remove(10) #removing an element by value
print(a)

a.pop() #removing an element by index (default is the last element)
print(a)

del a[0] #removing an element by index
print(a)

# a.clear() #removing all elements from the list
# print(a)

for i in a: #iterating through the list
    print(i)

a=[[1, 2, 3], [4, 5, 6], [7, 8, 9]] #creating a nested list
print(a[0][0]) #accessing an element in a nested list

'''List Comprehension'''

a = [1, 2, 3, 4, 5]
res = [x**2 for x in a] #creating a new list with the square of each element in the original list
print(res)