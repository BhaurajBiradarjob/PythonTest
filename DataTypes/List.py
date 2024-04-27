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
list1 =["Orange", 22, 33,44, 55,"Red"]
print(list)
list1.reverse()
print(list1)


