'''
A list is a data structure that can show a group of elements.
A list can store same type as well as different types of elements.
In Python it is not neccessary to mention the size of the list while
other programming it is required. the size will increase dynamically.
The list can store duplicate elements, in list index plays a important
role, through index we can perform all operations.
List objects are mutable which means we can modify or change the content
of the list even after creation.
we need to use [] brackets.
'''
# list1 =[]
# print(list1)
# print(type(list1))

# names = ["name1","name2","name3","name4","name5"]
# print(names)
# print(type(names))
# print(names[2])

# Genearlly we use list function for creating lists from other datatypes like range, tuple etc.
# number = list(range(5))
# print(number)

# modify using index number
# number[2]=22
# number[3]=33
# print(number)

# There are 3 ways in which we can access elements in a list
# They are:
'''
By using index
By using slicing operator
By using loops
'''
#By using slicing
# Syntax :
# list_name = [start:stop:step]

# numbers =[11,12,13,14,15,16,17]
# print(numbers[1:4])
# print(numbers[0:5:2])

# for n in numbers:
#     print(n)

# len() method
# numbers =[11,12,13,14,15,16,17]
# print(len(numbers))

# count() method
# numbers =[11,12,13,14,15,16,17, 11, 12, 12, 12]
# print(numbers.count(12))
# print(numbers.count(11))
# print(numbers.count(15))

# append() method
# This method can add elements to the list, the elements or items will be added at the 
# end of the list.
# list1 =[]
# list1.append("Apple")
# list1.append("Banana")
# list1.append("Orange")
# list1.append(101)
# print(list1)

# insert() method
# can add elements to the list which takes 2 arguments as  input 
# one is index number and other is element
# which will add element to the list at the specified index
'''
While using insert() method, some important points:

- If the specified index is greater than the max index, then the element will be inserted 
at the last position.
- If the specified index is smaller than the min index, then the element will be inserted
at the first position.
- In case of append() method which will add elements to the last
- In case of insert() method elements can be inserted to the list at first, last, middle any

'''
# numbers =[11,12,13,14,15,16,17, 11, 12, 12, 12]
# print(numbers)
# numbers.insert(1, 100)
# numbers.insert(2, 200)
# numbers.insert(-5, 500)
# numbers.insert(25, 2500)
# print(numbers)

# extend() method
# This method can be used to add items inone list to another
# list1 = [1,2,3,4,5]
# list2 = ["A","B","C"]
# list2.extend(list1)
# print(list2)
# print(list1)

# november_txn =[1200, 1300, 1400, 1500]
# december_txn = [313,123213,3211312,213123]
# december_txn.extend(november_txn)

# print(november_txn)
# print(december_txn)
# print(f"Total transaction is {sum(december_txn)}")

# remove() method
# numbers =[11,12,13,14]
# numbers.remove(13)
# print(numbers)

# If the item exists multiple times, then only the first occurence will be removed
# numbers=[1,1,1,2,2,23,3,3,3,3]
# numbers.remove(1)
# print(numbers)

# pop() method
# This method takes an index as an arguments and removes and returns the elements
# present at the given index
# If no index given then removes last items and returns the elements
# If the index is not in the range then we will get the error

# numbers = [11,12,13,14,15,16]
# print(numbers.pop()) # Last element
# print(numbers.pop(1)) # First Index
# print(numbers.pop(10)) # Error

'''
remove() and pop() difference
remove() - removes item based on the element
pop() - removes item based on the index
remove() - This method doesn't return any value
pop() - this method returns popped element
remove() - If the item is not present then we will get ValueError
pop() - If the item is not present in range then we will get IndexError
'''

#reverse() method
# list1 =["Orange", 22, 33,44, 55,"Red"]
# print(list)
# list1.reverse()
# print(list1)

# sort()
# numbers = [12, 1,13,15,16,18]
# numbers.sort() # ascending order
# print(numbers) 

# numbers.sort(reverse=True) # descending order
# print(numbers)

# names = ["ABC", "BCD", "XX", "YYY"]
# names.sort()
# print(names)

# names.sort(reverse=True)
# print(names)

# In Sort method the list should contains homogenous elements, otherwise we will get error

# x=["python", 23, "C++", 55.66]
# x.sort() # error
# x.sort(reverse=True) # error

# Aliasing the list
# numbers1=[22,33,44,55,66]
# numbers2 = numbers1
# print(numbers2)
# print(numbers1)

# print(id(numbers1))
# print(id(numbers2))

# numbers2[2] =20
# print(numbers1)

# We can create duplicate independent objects which is called cloning in list.
# Possible using slicing or using copy() method

# numbers1=[22,33,44,55,66]
# Creating new memory location for numbers2
# numbers2 = numbers1[:]

# numbers2[2] =20
# print(numbers1)
# print(numbers2)

# using copy() method
# numbers1=[22,33,44,55,66]
# numbers2 = numbers1.copy()

# print(f"{id(numbers1), id(numbers2)}")
# numbers2[2] =50
# print(numbers1)
# print(numbers2)

# We can join 2 list objects using + operator and returns single list object
# l1=["x","y","z"]
# l2 =[1,2,3,4,5]

# l3=l1+l2
# print(l3)

# Both the operands should be list type, otherwise we will get error
# str1="Python"
# l1 = [1,2,3]
# print(str1+l1) # error

# Using * operator
# numbers = [1,2,3,4]
# l1 = numbers * 2
# print(l1) # doubles the list

# list comparison
'''
We can use relational operator on the first objects for comparing 2 lists,
so in this case the first 2 items are compared, and if they are not same
then the correspounding result is returned.

If they are equal then the next 2 items are compared
It compares the correspounding elements of the lists starting from the first index until a
mismatch is found and all elements are compared

'''
# l1=[1,2,3]
# l2=[2,3,4]
# print(l1>l2)
# print(l1<l2)
# print(id(l1[0]))
# print(id(l2[0]))

'''
Here all the correspounding elements in the list are equal, the comparison
proceed to the next level.

Since there are no elements to compare, the result is False because the lists 
are considered equal.
'''
# print([5,6,7]<=[5,6,7])
# print([5,6,7]==[5,6,7])

# print(id(l1[0]))
# print(id(l1[1]))
# print(id(l2[0]))
# print(id(l2[1]))

'''
Here we are using > operator, so the comparison starts from the first elements
which is True, the next element compares which is also True, so the final element 
is True and the result is True.
'''
# print([5,6,7]>[4,4,5])

# List comparison with strings
# a=["xyz","abc","www"]
# b=["aaa", "bbb","ccc"]
# c=["xyz","abc","www"]
# d=["xyz","abc","www","qqq"]

# print(a==c)
# print(a==b)
# print(b==c)
# print(a==d)

'''
List unpacking also known as iterable unpacking or destructing which is a feature in
python that allows to assign the elements of a list to individual variables
'''
# fruits =["Banana","Mango", "Grapes", "Apple"]
# fruit1, fruit2, fruit3, fruit4 = fruits
# print(f"{fruit1} - {fruit2} - {fruit3} - {fruit4}")

# numbers = [1,2,3,4,5]
# first, second, *rest = numbers
# print(f"{first} - {second} and {rest}")

# first, *rest, last = numbers
# print(f"{first} - {rest} and {last}")


# In and Not In operators
# numbers = [1,2,3,4,5]

# print(5 in numbers)
# print(5 not in numbers)
# print(11 in numbers)
# print(11 not in numbers)

# Nested list
# nested_list = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# print(nested_list)
# print(nested_list[1][1])

# nested_list[1][1] = 100
# nested_list[2][2] = 400

# print(nested_list)

'''
List comprehension 
is an concise and expressive way to create lista that allows us to
generate a new list by appliyng an expression to each element
of an existing iterables(list, tuple, range)

Syntax:
list=[expression for item in iterable]
'''
# numbers = [1,2,3,4,5, 6]
# squares = [x**2 for x in numbers]
# print(squares)

'''
List comprehension consists of 3 parts
expression - so here x**2 defines what operation to perform on each element of the iterable,
so in that case it squares each element x.

iteration - for clause specifies the iteration over the existing iteration in each iteration

option condition - this can be added to filter the elements based on the conditions

list = [expression for item in iterable if statement]
'''

# numbers = [1,2,3,4,5, 6]
# even_number = [x for x in numbers if x%2 == 0]
# odd_number = [x for x in numbers if x%2 ==1]

# print(even_number)
# print(odd_number)