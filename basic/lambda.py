"""A lambda is a small anonymous function written in a single expression."""

# Normal Function

def square(n):
    return n**2
print(square(2))

#lambda function 

square = lambda x:x**2
print(square(4))


#syntax- lambda arguments: expression

add= lambda a,b: a+b

print(add(5,5))

is_even=lambda x:x%2==0
print(is_even(10))
print(is_even(9))

greater=lambda x,y: x if x>y else y
print(greater(5,6))


"""Map Function"""

l=[1,2,3,4,5]
square=list(map(lambda x: x**2, l))
print(square)


"""Filter Function"""

numbers=[1,2,3,4,5,6]
result=list(filter(lambda x: x%2==0, numbers))
print(result)


"""reduce"""
from functools import reduce

#repeatadly combines two value

numbers=[1,2,3,4,5]
result=reduce(lambda x,y: x+y, numbers)
print(result)


"""Practice"""

numbers=[2,4,6,8]
result=list(map(lambda x: x*3, numbers))
print(result)

numbers=[5, 12, 8, 20, 3, 15]
result=list(filter(lambda x: x>10, numbers))
print(result)

from functools import reduce

numbers =[1, 2, 3, 4, 5]
result= reduce(lambda x,y: x*y, numbers)
print(result)

names=["afzal", "ali", "ahmed"]

result=list(map(lambda x: x.upper(), names))
print(result)