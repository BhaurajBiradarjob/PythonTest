'''
Set is an unordered collection of unique elements.
Sets are mutable, iterable and do not allow duplicate values.
They are implemented using a Hash Table which provides efficient membership testing
and element retrieval operation.
'''
# We can create set using {} or by using set() constructor.

# my_set = {4,5,16}
# print(my_set)
# print(type(my_set))

# my_set = set([1,2,3,1])
# print(my_set)

# my_set = {12, '45', True, 345.66}
# print(my_set)

# Methods
# add()
# my_set={10,20,30}
# my_set.add(40)
# print(my_set)

# l1=[3,4,5,6]
# my_set.add(l1) #Error unhashable List use update method
# print(my_set)

# update()
# my_set ={10,20,30}
# my_set2={40,50}
# my_set.update(my_set2, range(5))
# print(my_set)

# l1=[101,202,303]
# my_set.update(l1)
# print(my_set)

'''
Difference between add() and update()
- add() method can add individual items to the set.
- update() method can be used to add multiple items to the set.

The add() method can take one argument whereas the update() method can take the
more than one arguments but only point is all of them should be iterable objects.

'''

# my_set = set()
# my_set.add(10)
# # my_set.add(20,30,40) #error - add()  takes one argument
# print(my_set)

# # my_set.update(1) # error - update() takes more than one arguments
# # print(my_set)
# my_set.update(range(5),[12,3,4])
# print(my_set)

# copy() - returns a copy of the set, it is a cloned object.
# my_set = {5,6,7}
# my_set2 = my_set.copy() # here using copy() pointing to different location.
# my_set3 = my_set # Pointing to same memory location
# print(f"{id(my_set), id(my_set2), id(my_set3)}")
# print(my_set, my_set2, my_set3)

# my_set2.update([12,13,14])
# print(my_set, my_set2, my_set3)

# my_set3.update([100,200,300])
# print(my_set, my_set2, my_set3)

#pop() method
# This method removes and returns some random element from the set.
# my_set={35,66,77,88}
# print(my_set)
# x=my_set.pop()
# print(x)
# print(my_set)

#remove() method
# This method removes specific elements from the set, If the specified element is not
# present then we will get error

# my_set={35,66,77,88}
# my_set.remove(77)
# print(my_set)
# my_set.remove(110) # error
# print(my_set)

# discard() method
# This method removes the specified element from the set, id the specified element is not present
# then we won't get any error

# my_set={35,66,77,88}
# my_set.discard(77)
# my_set.discard(110) # No error
# print(my_set)

# clear() - This method clears all elements in the set
# my_set={5,6,7}
# print(my_set)
# my_set.clear()
# print(my_set)

# union() - This method returns all elements present in both sets.
# a={1,2,3}
# b={4,5,6}
# result = a.union(b)
# print(result) 

# intersection() - This method returns common elements present in both sets
# x={10,20,30,40}
# y={30,40,50,60}
# result = x.intersection(y)
# print(result)

# difference() - This method returns the elements present in Set A and not in Set B
# a={10,20,30,40}
# b={30,40,50,60}
# result = a.difference(b)
# print(result)
# print(a-b)
# print(b-a)

# symmetric_difference() - This method returns elements present in either A or B but not in both
# a={10,20,30,40}
# b={30,40,50,60}
# result = a.symmetric_difference(b)
# print(result)

# in and not in 
# s1={2,3,4,"Python"}
# print(s1)
# print(1 in s1)
# print(2 in s1)
# print(8 not in s1)
# print(5 not in s1)

# set comprehension
# numbers = [1,2,3,4,5]
# even_numbers = {x for x in numbers if x%2==0}
# square_numbers = {x**2 for x in numbers}
# print(even_numbers)
# print(square_numbers)
