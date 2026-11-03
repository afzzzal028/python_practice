"""For Loop"""
n =5
for i in range(n):
    print(i)

#Iterating by index Sequence
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(fruits[i])


fruits= ["apple", "cherry"]

for i in fruits:
    print(i)

"""While Loop"""
i = 0
while i < 5:
    print(i)
    i+= 1

#infinite while loop

# while True:
#     print("This is an infinite loop.")


"""Nested Loop"""
for i in range(6):
    for j in range(i):
        print(i, end = "")
    print()


"""Pattern Printing"""

#for loop
for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()

#while loop

i=0
while i<4:
    j=0
    while j<4:
        print("*", end = " ")
        j+=1
    print()
    i+=1

"""Right Angled Triangle"""

for i in range(6):
    for j in range(i):
        print("*", end=" ")
    print()

#using while loop

i=1
while i<6:
    j=1
    while j<=i:
        print("*", end= " ")
        j+=1
    print()
    i+=1


"""Inverted Right Angled Triangle"""

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

#using for loop

i=5
while i>=1:
    j=1
    while j<=i:
    
        print("*", end=" ")
        j+=1
    print() 
    i-=1
       
"""Pyramid Pattern"""

#single loop
n=5
for i in range(1, n+1):
    print(" "* (n-i) + "*"* (2*i-1))


#nested loop
rows = 5

for i in range(1, rows+1):

    for j in range(rows-i):
        print(" ", end=" ")

    for k in range(2*i-1):
        print("*", end=" ")

    print()



"""Number Pattern"""

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

#while loop
i=1
while i<6:
    j=1
    while j<=i:
        print(j, end=" ")
        j+=1
    print()
    i+=1


"""Repeated Number Pattern"""

for i in range(1, 6):
    for j in range(1, i+1):
        print(i, end=" ")
    print()

#inverted triangle pattern

for i in range(5,0, -1):
    for j in range(1, i+1):
        print(i, end=" ")
    print()

for i in range(5,0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

"""Floyds Triangle"""
num = 1
for i in range(1, 6):
    for j in range(1, i+1):
        print(num, end= " ")
        num+=1
    print()

# Question 1. Print a triangle with 6 rows of stars.
rows = 6
for i in range(1, rows+1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()


#Question 2. Print an inverted triangle of numbers: 1 2 3 4, then 1 2 3, etc.
rows=4
for i in range(rows, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

#Question 3. Print a square of numbers from 1 to 4 in every row.
rows=4
for i in range(1, rows+1):
    for j in range(1, rows+1):
        print(j, end=" ")
    print()

#Question 4. Print this pattern: 1 / 2 3 / 4 5 6 / 7 8 9 10.

num =1
for i in range(1,5):
    for j in range(1, i+1):
        print(num, end=" ")
        num+=1
    print()

#Question 5. Print a pyramid with 5 rows.

n=6
for i in range(1, n+1):
    print(" "*(n-i) + "*"*(2*i-1))


#Inverted Star Triangle

rows=5
for i in range(rows, 0, -1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()

#Right Aligned Triangle

rows=5
for i in range(1, rows+1): #controls the whole rows
    for j in range(rows-i):
        print(" ", end= " ") #makes the spacing
    for k in range(1, 1+i):
        print("*", end = " ") #prints the stars
    print()



#Numbwer Pyramid
rows=5
for i in range(1, rows+1 ):
    print(" "*(rows-i), end="") #for spacing
    for j in range(1, i+1):
        print(j, end=" ") #prints the numbers
    print() #for new line

#Diamond Pattern
rows=5
for i in range(1, rows+1):
    print(" "*(rows-i)+ "*"*(2*i-1))
for i in range(rows-1, 0, -1):
    print(" "*(rows-i)+ "*"*(2*i-1))


#Binary Number Pattern
rows=5
for i in range(1, rows+1):
    for j in range(1, i+1):
        if (i+j)%2==0:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()