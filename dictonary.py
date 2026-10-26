#dictionary
dict1 = {"name": "Afzal", "age": 25, "city": "New York"}
print(dict1)

#creating a dictionary using dict() constructor
d = dict(name="Afzal", age=25, city="New York")
print(d)
b={"Afzal": 25, "Python": "Learning", "City": "New York"}
print(b)

print(dict1["name"]) #accessing value by key
print(dict1.get("age")) #accessing value by key using get() method

d={"name": "Afzal", "age": 25, "city": "New York"}
d["age"]=26 #changing the value of a key
d["country"]="USA" #adding a new key-value pair
print(d)

del d["city"] #removing a key-value pair by key
print(d)

val= d.pop("country") #removing a key-value pair by key and returning the value
print(val)

#print(d.popitem()) #removing the last inserted key-value pair and returning it

for key in d: #iterating through the keys of the dictionary
    print(key)
for value in d.values(): #iterating through the values of the dictionary
    print(value)

for key, value in d.items(): #iterating through the key-value pairs of the dictionary
    print(key, value)

