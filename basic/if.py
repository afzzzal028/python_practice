age = 20 
if age>=18:
    print("You are eligible to vote.")

#short hand if statement
if age>=18: print("You are eligible to vote.")

#if-else statement
age = 17
if age>=18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#if-elif-else statement

age = 12
if age<4:
    print("You are a baby.")
elif age<13:
    print("You are a child.")
else:
    print("You are an adult")

#Nested if statement
age = 35
is_member=True
if age>50:
    if is_member:
        print("You are eligible for a senior citizen discount.")
    else:
        print("You are not eligible for a senior citizen discount.")
else:
    print("You are not eligible for a senior citizen discount.")


#condtional expression
age = 20
msg="You are a gooner" if age>18 else "You are not a gooner"
print(msg)

#Match Case Statement

number =7

match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")