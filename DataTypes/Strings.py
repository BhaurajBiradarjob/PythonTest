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
print(str1[0:6])
print(str1[0:8:2])

