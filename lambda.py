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