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

res= [x for x in a if x%2==0] #creating a new list with only the even elements from the original list
print(res)

a = [9, 10, 11, 12, 13, 18]
res= [x for x in a if x>10] #creating a new list with only the elements greater than 10 from the original list
print(res)

a =[i for i in range(10)] #creating a new list with elements from 0 to 9
print(a)

c= [(x,y) for x in range(3) for y in range(3)] #creating a new list with tuples of all combinations of x and y from 0 to 2
print(c)

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res= [val for row in mat for val in row] #flattening a nested list into a single list
print(res)


data = [5, 2, 8, 1, 9, 2]

# Length
print(len(data))

# Sorting
print(sorted(data))
data.sort()

# Minimum, maximum, sum
print(min(data))
print(max(data))
print(sum(data))

# Membership testing
print(8 in data)

# Counting occurrences
print(data.count(2))

# Finding an element's index
print(data.index(8))

# Slicing
print(data[1:4])
print(data[:3])
print(data[::2])

# Enumerate: index and value
for i, value in enumerate(data, start=1):
    print(i, value)


data = [1, 2, 3, 4, 5]

squares = [x**2 for x in data]
evens = [x for x in data if x % 2 == 0]
labels = ['Even' if x % 2 == 0 else 'Odd' for x in data]
print(squares)
print(evens)
print(labels)