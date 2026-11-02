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
while i<=5:
    j=1
    while j<=i:
        print(j, end=" ")
        j+=1
    print()
    i+=1