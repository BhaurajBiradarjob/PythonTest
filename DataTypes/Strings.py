'''
In string, we can use single, double, triple single, trip double quotes
'''

# name = 'Python'
# name2="Java"
# name3='''Javascript'''
# name4=""""C++"""
# print(name)
# print(name2)
# print(name3)
# print(name4)

# name1 = input("Please enter your name ")
# print(f"Hi {name1}")

# name2=input("Programming language? ")
# print(f"{name1} learn {name2} very well")

# name3 = """"All the Best"""
# print(f"{name3} {name1 }")

# Print multiline information

# address = """
# ABC Company
# Silk Board
# Bangalore

# """
# address2 ='''
# XYZ Company
# Bommanhalli
# Bangalore

# '''

# print(address)
# print(address2)

# s1 = "Learn 'Python' today."
# s2 = 'Learn "Java" today.'
# s3 = """Learn 'C++' today."""
# s4 = 'Learn \'Java\' today.'
# print(s1)
# print(s2)
# print(s3)
# print(s4)

# We can access string characters by using Indexing
# slicing
# In case of indexing, we need to use [] to access the string index, it should be integer
# Python supports positive and negative indexing
# Positive indexing means the position of string characters from left to right, the 
# starting position is 0
# Negative indexing means the position of string characters from right to left, the 
# starting position is -1

str1 = "Hello Python"
# print(str1[1])
# print(str1[-1])
# print(str1[-3])
# print(str1[9])
# print(str1[-9])
#print(str1[20])#error

#Slicing
'''
string_name[start:stop]
string_name[start:stop:step]

start : represents the starting index position
stop : represents the ending index position (index-1)
step : represents the increment position, default is 1
'''
# print(str1[0:6])
# print(str1[0:8:2])

# #Accessing from 0th to last
# print(str1[0:])
# print(str1[::])
# print(str1[:])

# #Accessing the entire in step of 2
# print(str1[::2])
# #Accessing the specified index to end
# print(str1[3::])
# #Reverse the string
# print(str1[::-1])
# #take every element from index 5 to the beginning of the string but in reverse order
# print(str1[5::-1])

# #Strings are immutable, once we create string object we cannot change or modify the existing object
# name1="JavaScript"
# #name1[2]="S"
# name1 = "Python"
# print(name1)

# The + Operator is for concatenationor joins for string, both the arguments should be
# strings type, otherwise we will get error

x = "Python"
y = "C++"
print(x+y)
print(x+" "+y)
# z=45
# print(x+y+z) # Error

# * Operator, one argument should be of string type and other argument should be int type
x="Python"
y=2
print(x*y)#Print twice

# z="C"
# print(x*z) # error

# len()

# name1 = input("Your name? ")
# print(f"Your name is {name1}")
# name_len = len(name1)
# print(f"Length of your name is {name_len}")

# username = input("Enter Username ")
# password = input("Enter Password ")

# pass_len = len(password)
# hide_password = "*"*pass_len
# print(f"Your password is {hide_password}")

# in operator and not in operator
# in oprator returns true if the string or character found in the main string
# not in oprator returns true if the string or character not found in the main string

# name1="Python"
# print('p' in name1)
# print('p' not in name1)
# print('P' in name1)
# print('P' not in name1)

# #compare string
# name1 = "Python"
# name2="python"

# print(name1==name2)
# if(name1 == name2):
#     print(f"{name1} equal to {name2}")
# else:
#     print(f"{name1} not equal to {name2}")

# # capitalize() method
# # Returns us a string where the first character of this method is uppercase and the remaining
# # in lower case
# str1 = input("Name in lower case :")
# result = str1.capitalize()
# print(result)

#upper() and lower()

# message1 ="python"
# message2 = "PYTHON"
# print(message1.upper())
# print(message2.lower())

# x= message1.upper()
# y=message2.lower()
# print(x)
# print(y)

# swapcase()
# This method converts all lowercase characters to uppercase and all uppercase characters 
# to lowercase

# message1 ="PYTHON is"
# print(message1.swapcase())

# count()
# message2 = "Python is Python calls Python"
# result = message2.count("Python")
# print(f"Python present {result} times")

# split()
# We can split the string according to the specified operator. Default separator is space

# mesage3 ="Python is programming language"
# result = mesage3.split()
# print(f"before split : {mesage3}")
# print(f"after split : {result}")
# print(type(mesage3))
# print(type(result))
# for x in result:
#     print(x)

# endsWith() method
# This method returns True if the string ends with the specified substring, otherwise
# it returns false
# str1 = "Rakesh is learnin Python"
# result1 = str1.endswith("is")
# print(f"is ends with : {result1}")

# result2 = str1.endswith("Python")
# print(f"Python ends with : {result2}")

# find()
# This method finds a substring in the whole string and it returns the index of the first 
# match, if it is not matching we will get -1
# str1 = "Rakesh is learnin Python"
# result1= str.find("is")
# resul2 =str.find("has")
# print(f"is find is: {result1}")
# print(f"has find is: {resul2}")

# index()
# index is same as find method, difference is if it is not matching we will get error

# str1 = "Rakesh is learnin Python"
# result1= str.index("is")
# resul2 =str.index("has")
# print(f"is index is: {result1}")
# print(f"has index is: {resul2}")

# replace()
# returns a copy of the string with all occurences of substring old replaced by new.
str1 = "Java Python C C++ C#"
str2=str1.replace("Python","JavaScript")
print(f"Old string : {str1} ")
print(f"New string : {str2} ")

#strip()
# is used to remove the leading and trailing characters from the strings.
job = "    Programmer"
print(job)
print(len(job))
x=job.strip()
print(len(x))