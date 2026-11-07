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

d=Dog("Gold")
c=Cat("Gracie")
animals=[Dog(), Cat(), Animal()]
for animal in animals:
    animal.sound()