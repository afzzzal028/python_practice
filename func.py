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
student(fname="Ariba", lname="Aslam")