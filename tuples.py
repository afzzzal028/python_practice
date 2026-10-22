#creating a tuple
tup =()
print(tup)

#using string
tup=("Afzal", "Python", "Learning")
print(tup)

#using list
list1=[1, 2, 3, 4, 5]
tup=tuple(list1)
print(tup)

#built-in functions
tup=tuple("Afzal")
print(tup)

tup= (5, "Welcome", 3.14, True) #creating a tuple with different data types
print(tup)

print(tup[0]) #accessing the first element of the tuple
print(tup[1]) #accessing the second element of the tuple

tup=("Good", "Morning", "Afzal") #tuple unpacking

a, b, c = tup # unpacking the tuple into variables
print(a)
print(b)
print(c)  

#Concatenation of tuples
tup1 = (1, 2, 3)
tup2 = (4, 5, 6)
tup3 = tup1 + tup2 #concatenating two tuples
print(tup3)

#slicing of tuples
tup = (1, 2, 3, 4, 5)
print(tup[1:4]) #slicing the tuple from index 1 to 3
print(tup[::-1]) #reversing the tuple

#del tup #deleting the tuple
#print(tup) #this will raise an error as the tuple is deleted

a, *b, c = (1, 2, 3, 4, 5) #unpacking with * operator
print(a) #prints 1
print(b) #prints [2, 3, 4]
print(c) #prints 5