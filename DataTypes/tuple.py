'''
A tuple refers to a collection of objects which are ordered and it cannot be changed.
the python objects can be strings, lists, tuples, integers etc.

- In tuple the order in which the elements are added is the same order the output will
be displayed.

- Tuple can store duplicates
- in the tuples once we create tuple object, we cannot modify the content of the tuple object.
This is only difference between tuple and list

Tuple can be created using "()" symbol, paranthesis is not complusory. It is optional
'''
# t1 =()
# print(t1, type(t1))

# t2=(22,33,44,55)
# print(t2, type(t2))

# To create a tuple object with a single element we need to include a comma after
# the element, If we don't mention the comma then it will be recognized as integer
# t3 =(55)
# print(t3, type(t3))#int

# t4=(55,)
# print(t4, type(t4))#tuple

# Paranthesis are optional
# t5 = 22,33,44
# print(t5, type(t5))

# using tuple() constructor which can be used to create a tuple by passing an iterable
# object such as list as an argument

# list1 = [44,55,66]
# t1 = tuple(list1)
# print(t1, type(t1))

# t2 = ["Apple", "Banana", "Mango"]
# print(t2, type(t2))

# t3= tuple("Python")
# print(t3, type(t3))

# We can access tuples:
# indexing
# slicing operator
# looping

# t4 = (1,2,3,4,5,6)
# print(t4[2])
# print(t4[5])
# print(t4[-1])

# print(t4[1:4])
# print(t4[2::])
# print(t4[::2])
# print(t4[::])

# my_tuple =["A", "B", "C", "D"]
# for x in my_tuple:
#     print(x)

# Unpacking the tuple
# t5 = ("Sam", 45, "Hyderabad")
# name, age, location = t5
# print(name, age, location)

# tuple immutability
'''
Tuple have immutable nature, which means that if we create a tuple then we cannot
modify the elements of the existing tuple.
'''
# t6 =(10,20,30,40,50,60)
# t6[2] = 200
# print(t6) # error

# in case of list we can modify but in case of tuple we cannot modify
# l1=[1,2,3]
# l1[0]=100
# print(l1)

# Solve the tuple immutability
# 1st approach
# converting tuple to list and then back to tuple after modification
# my_typle=(1,2,4)

# # tuple to list
# my_list = list(my_typle)
# my_list[0] = 100
# # list back to tuple
# my_tuple = tuple(my_list)
# print(my_tuple)

# Second Approach
# my_tuple=(1,2,3)
# modified_tuple = (my_tuple[0], 231, 556, my_tuple[1])
# print(modified_tuple)

#3rd Approach
# my_list=[2,3,4]
# my_tuple=(1, my_list, 5)
# my_list[0]=55
# print(my_tuple)

# Concatenation (+) Operator : Adds 2 tuples
# t1=(10,20,30)
# t2=(40,50,60)
# print(t1+t2)

# Multiplication (*) Operator : adds n times duplicates
# t1 = (10,20,30)
# print(t1 * 3)

# Methods
#count()
# t1 = (10,20,30,10,20,30)
# print(t1.count(20))

#index() - returns first occurence of the element index
# my_tuple=(1,2,3,4,1,2,3,4)
# print(my_tuple.index(2))

#len()
# my_tuple=(1,2,3,4,1,2,3,4)
# print(len(my_tuple))

#sorted()
#This function can sort the elements which is default natural sorting order which is in
#ascending order.
# t1=(10,20,30,40,50,60)
# asc_order = sorted(t1)
# print(asc_order)
# desc_order = sorted(t1, reverse=True)
# print(desc_order)

#max() min() and sum()
# my_tuple = (10,20,30,40,50)
# print(min(my_tuple))
# print(max(my_tuple))
# print(sum(my_tuple))

# Tuple packing and unpacking
'''
Tuple packing and unpacking involve combining values into a tuple(packing) or
extracting values from tuple into individual variables(unpacking).
'''
# Tuple Packing - process of combining multiple values or objects into a single 
# tuple, we can pack values by separating them with commas.

# person = "Sam",55,"Hyderabad"
# print(person)

# tuple unpacking
# name, age, location = person
# print(name, age, location)

'''
Tuple packing and unpacking are particularly useful when working with functions that
return or accept multiple values
'''

#Tuple comprehension
'''
Tuple comprehension allows us to perform transformations, filtering and calculations
on the elements of the iterable to generate new tuple
'''
# Print from 1 to 5, and their squares
# squares = tuple(x**2 for x in range(1,5))
# print(squares)

# Filtering odd numbers
# numbers = (1,2,3,4,5)
# odd_numbers = tuple(x for x in numbers if x%2 == 1)
# print(odd_numbers)

# text = "Python"
# chara = tuple(ch for ch in text)
# print(chara)