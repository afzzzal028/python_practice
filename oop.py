"""OOP- Object Oriented Programming"""

# Class- It is a collection of objects.
#Creating Class

class Dog():
    species= "Canine"
    def __init__(self, name, age):
        self.name=name
        self.age=age
#objects- it an instance in class.

dog1= Dog("Buddy", 8)
print(dog1.name, dog1.age, dog1.species)


"""

Four Pillar of OOP
1. Inheritance
2. Polymorphism
3. Encapsulation
4. Data Abstraction

"""

#Inheritance

#Allows a chlid class to inherit the property of Parent Class.

class Animal():
    def __init__(self, name):
        self.name=name

    def info(self):
        print("Animal Info: ", self.name)

class Dog(Animal):
    def sound(self):
        print(self.name, "barks")

class Cat(Animal):
    def sound(self):
        print(self.name, "meows")

# animals=[Dog(), Cat(), Animal()]
# for animal in animals:
#     animal.sound()


class Student():
    def __init__(self, marks):
        self.__marks=marks

    
    def get_marks(self):
        return self.__marks

    #__methods can be accessed by _ClassName__method

    def set_marks(self, grade):
        if grade>0 or grade<=100:
            self.__marks

        else:
            print("Invalid Grade")

result = Student(-11)
print(result.get_marks())
result.set_marks(100)
print(result.get_marks())