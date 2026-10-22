student = {"name": "Afzal", "age": 25, "city": "New York"}
print(student.get("city"))
print(student.get("age"))

student["age"] = 21 #updating the value of a key
student["course"] = "Python" #adding a new key-value pair
print(student)


marks = {"Python": 85, "Math": 72, "DSA": 90}
for key, value in marks.items():
    print(key, value)

marks = {"Ali": 75, "Afzal": 92, "Sara": 88, "Omar": 60}
for key, value in marks.items():
    if value>80:
        print(key)