'''
If we want to represent a group of objects as key value pairs then we should
go for dictionaries.

Each key is unique in the dictionary and is used to access its associate values.

here key can be of any of immutable types(strings, numbers, tuples) while values
can be of type(lists, objects etc..)

Dictionaries are mutable and it is ordered.
Dictionaries can grow or shrink dynamically as key value pairs which are added or removed

Dictionaries are hashtable implementation making key based lookups highly efficient.
retrieving the value associated with the given key, which has a constant time complexity 
an average regardless of the size of the dictionary

Syntax:
d={key1:value1, key2:value2,....., keyN:valueN}
'''
# d={1:"Python", 2:"C++", 3:"Java", 4:"C"}
# print(d)
# print(type(d))

# d={}
# d[1] = "Flutter"
# d[2] = "Python"
# d[3] = "JavaScript"
# d[4] = "Java"
# print(d)
# print(type(d))

# Access using keys
# print(d[2])

#print(d[5]) # error

# Handle error
# if 5 in d:
#     print(d[5])
# else:
#     print("Key not found")

# Updating dictionary
# d={1:"Python", 2:"C++", 3:"Java", 4:"C"}
# print(f"Old dictionary : {d}")

# d[5] = "Dart"
# d[6] = "PHP"
# print(f"New added keys in dictionary : {d}")

# d[1]="Ruby"
# print(d)

# Employee

# d={}
# no_emp = int(input("Please enter number of employees : "))
# i=1
# while i<= no_emp:
#     name = input("Please enter employee name: ")
#     salary = input("Please enter employee salary: ")
#     d[name] = salary
#     i +=1

# for emp in d:
#     print(f"The name is {emp} and the salary is {d[emp]}")

# del keyword
# d={1:"Python", 2:"C++", 3:"Java", 4:"C"}
# print(d)
# del d[2]
# print(d)
# # del d[5] # error

# clear()
# d={1:"Python", 2:"C++", 3:"Java", 4:"C"}
# d.clear()
# print(d)

# del()
# d={1:"Python", 2:"C++", 3:"Java", 4:"C"}
# print(d)
# del d
# print(d) # error

# dict() - This function can be used to create an empty dictionary
# d=dict()
# print(d)
# print(type(d))

# d1=dict({1:"Python", 2:"C++"})
# print(d1)
# print(type(d1))

# dict([tuple1, tuple2])
# This creates a dictionary with list of tuple elements
# dp = dict({1:"Python", 2:"C++"})
# print(dp, type(dp))

# len()
# d1=dict({1:"Python", 2:"C++", 3:"Java", 4:"C"})
# print(f"Length of dictionary : {len(d1)}")

# get() - is used to get the value associated with the key, if key is 
# available then it returns the correspounding value otherwise return None
# d=dict({1:"Python", 2:"C++", 3:"Java", 4:"C"})
# result=d.get(2)
# print(result)
# result=d.get(3)
# print(result)

# result=d.get(5)
# print(result)
# result=d.get(7, "No key found")
# print(result)

#pop() - Method removes element and expects one argument
# d1=dict({1:"Python", 2:"C++", 3:"Java", 4:"C"})
# print(d1)
# result = d1.pop(3) 
# print(result)
# print(d1)
# print(d1.pop(3)) # Error - already removed item

#popitem() - removes an arbitrary item(key-value) from dictionary and returns it
# Gives an error when dictionary is empty
# d1=dict({1:"Python", 2:"C++", 3:"Java", 4:"C"})
# result = d1.popitem()
# print(result)
# print(d1)

# keys() - returns all keys associated with dictionary
# d1=dict({1:"Python", 2:"C++", 3:"Java", 4:"C"})
# print(d1)

# for x in d1.keys():
#     print(x)

# values() - Returns all values associated with dictionary
# d1=dict({1:"Python", 2:"C++", 3:"Java", 4:"C"})
# print(d1)

# for x in d1.values():
#     print(x)

# items() - each key value pair is called item, item() method returns the list
# of tuples representing key-value pair
# d1=dict({1:"Python", 2:"C++", 3:"Java", 4:"C"})
# print(d1)

# for k,v in d1.items():
#     print(f"The key is {k} and Value is {v}")

#copy()
d1=dict({1:"Python", 2:"C++", 3:"Java", 4:"C"})
d = d1
print(id(d))
print(id(d1))

# d[2] ="C"
# print(d)
# print(d1) 
# above is reference copy, both will change
# d=d1.copy()
# print(id(d))
# print(id(d1))
# d[2] ="C"
# print(d)
# print(d1) 

#dictionary comprehension
squares = {a:a*a for a in range(1,5)}
print(squares)