s= {10, 20, 30, 40}
print(s)
print(type(s))
s=set(["a", "b", "c"])
print(s)

s={"Afzal", "and", "Afzal"}
print(s) #removing duplicate values
#s[1]= "Ali" #this will give an error because sets are unordered and do not support indexing
s={10, "Afzal", 20, 30, 40, 5.8, }
print(s)

s= set([10, 20, 30, 40])
print("Normal Set:", s)
fs = frozenset([10, 20, 30, 40])
# fs.add(50) #this will give an error because frozensets are immutable and do not support adding new elements
print("Frozen Set:", fs)

s= set([10, 20, 30, 40])
s.add(50) #adding a new element to the set
print(s)

a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
u = a.union(b) #union of two sets
print(u)
up = a.intersection(b) #intersection of two sets
print(up)
d = a.difference(b) #difference of two sets
print(d)
print(a & b) #intersection of two sets using & operator