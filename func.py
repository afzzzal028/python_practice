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