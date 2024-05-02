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
my_set = {5,6,7}
my_set2 = my_set.copy() # here using copy() pointing to different location.
my_set3 = my_set # Pointing to same memory location
print(f"{id(my_set), id(my_set2), id(my_set3)}")
print(my_set, my_set2, my_set3)

my_set2.update([12,13,14])
print(my_set, my_set2, my_set3)

my_set3.update([100,200,300])
print(my_set, my_set2, my_set3)


