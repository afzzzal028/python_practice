#Defining a function,
"""
def- keyword
function_name- Function Name
()-  parameter
#statement
return expression

"""

def fun():
    print("Hello")
fun()

"""

Funtion Argumenta

def function_name(arguments):
    # function body

    return value

"""

def evenOdd(x):
    if x%2==0 :
        return "Even"
    else:
        return "Odd"
print(evenOdd(15))
print(evenOdd(10))


"""Types of Function Argument"""

#default argument- use a predefined value when no value is passed during the function call.

def myFUn(x, y=5):
    print("X", x)
    print("Y", y)
myFUn(10)

#Keyword Argument- pass values using parameter names, so argument order does not matter.

def student(fname, lname):
    print(f"Hello, {fname} {lname}")
student(fname="Afzal", lname= "Siddiqui")
student(fname="Jack", lname="Reacher")

#Positinal Argument- values are assigned to parameters based on their order in the function call.
def nameAge(name, age):
    print("Hi, I am", name)
    print(f"I am {age} years old." )

print("Case-1:")
nameAge("Ali", 20)

print("Case-2:")
nameAge(20, "Ali")


#Arbitrary Argument- allow functions to accept multiple values. This is done using two special symbols
#*args- collects extra positional arguments as a tuple.
# **kwargs- collects extra keyword arguments as a dictonary.

def myFun(*args, **kwargs):
    print("Non-keyword Argument")
    for arg in args:
        print(arg)

    print("Keyword Argument")
    for key, value in kwargs.items():
        print(f"{key}=={value}")

myFun("Hey", "Welcome", first="geeks", second= "for", last="Geeks")


"""Nested Fucntions"""

def f1():
    s="I love sm1"
    def f2():
        print(s)
    f2()
f1()


"""Return Statement"""

#return [expression]

def sq_value(num):
    return num**2
print(sq_value(4))
print(sq_value(2))

"""Pass by Reference and Pass by Value"""

def myFun(x):
    x[0]="strawberry" #can modify the list
b=["apple", "kiwi", "mango"]
myFun(b)
print(b)

"""
b creates a list in memory.
myFun(b) passes the list to the function.
x now refers to the same list as b.
x[0] = 20 modifies the first element of that original list.
When you print b, the modification is visible.
"""

def myFun2(x):
    x=20 # a didn't become 20

a=10
myFun2(a)
print(a)

"""

a = 10 creates an integer object.
myFun2(a) passes the value's object reference to the function.
Initially, x refers to the same integer object as a.
x = 20 makes x refer to a different integer object.
a still refers to the original integer object, 10.

"""




""""Practice"""

#Write a function called greet() that
def person(name):
    print(f"Hello, {name}")
person("Afzal")

#Return Statement

def square(n):
    return n**2
print(square(5))

#Multiple Argument

def calculate(a, b):
    return a+b, a-b, a*b
print(calculate(5,2))

#understanding arguments
def student(name, age=20):
    print(f"{name}")
    print(f"{name}, {age}")
student("Afzal")
student("Ali", 21)


def add(a,b):
    print(a+b)
result=(add(10,20))
print(result)

def check_number(n):
    if n>0:
        return "Positive"
    elif n==0:
        return "Zero"
    else:
        return "Negative"
print(check_number(5))


def find_max(a, b, c):
    max=a
    max_num=[a, b, c]
    for i in max_num:
        if i>max:
            max=i
    
    return max

print(find_max(10, 25, 15))


#factorial
def factorial(n):
    if n<0:
        return "factorial not defined for negative"
    elif n==1 or n==0:
        return 1

    factorial=1
    for i in range(1, n+1):
        result*=i
    return result

print(factorial(0))


#count vowels

def count_vowels(str):
    vowles="aeiouAEIOU"
    count=0
    for char in str:
        if char in vowles:
            count+=1
    return count
print(count_vowels("Afzal Siddiqui"))


def is_prime(n):
    if n<=1:
        return "Prime"
    for i in range(2,n):
        if n%i==0:
            break
        else:
            return "Not a Prime"
    return "Prime"
print(is_prime(8))


def reverse_string(str):
    reversed_str=""
    for ch in str:
        reversed_str= ch + reversed_str
    return reversed_str
print(reverse_string("Python"))
