'''
Types of function
- Predefined or built-in functions : which come installed along with python software
  or built-in functions

- User defined functions : which are defined by developers as per requirement 

Terminology related to function in Python:

def keyword:
Every function should start with the keyword def.

Name of the function:
paranthesies
colon:
Body
return statement is optional
Syntax :
def function_name():
    code to be executed
    return something(optional)
'''

# function without parameters
# def person():
#     print("My name is Bhauraj")
#     print("I am from Bangalore")

# person()
# person()

# function with parameters
# def add(a,b):
#     print(f"Sum of {a}+{b} : {a+b}")

# def mult(a,b):
#     print(f"Multiplication of {a}*{b} : {a*b}")

# def sub(a,b):
#     return a-b

# add(20,10)
# mult(20,10)

# sub_result = sub(20,10)
# print(sub_result)

# Even or odd number 

# def check_even_odd(num):
#     if num%2 == 0:
#         print(f"{num} is an even number")
#     else:
#         print(f"{num} is an odd number")

# check_even_odd(20)
# check_even_odd(30)

# Return multiple values from the function
'''
A function that returns multiple values, same should be handled at the 
function calling statement 

'''
# def function1(a,b):
#     r1 = a+b
#     r2 = a-b
#     r3 = a*b
#     r4 = a/b
#     return r1,r2,r3,r4

# result1,result2,result3,result4 = function1(20,10)
# print(f"Addition: {result1}")
# print(f"Substraction: {result2}")
# print(f"Multiplication : {result3}")
# print(f"Division: {result4}")

# def get_person_details():
#     name="Mahesh"
#     age = 22
#     salary = 42000000
#     return name,age,salary

# person_name, person_age, person_salary = get_person_details()

# print(f"Person Name: {person_name} \n Person age: {person_age} \n Person salary: {person_salary}")

# def calculate_statistics(numbers):
#     minimum = min(numbers)
#     maximum = max(numbers)
#     total = sum(numbers)
#     average = total/len(numbers)
#     return minimum,maximum,total,average

# result = calculate_statistics([5,10, 20, 30, 40, 50])
# min_value,max_value, total_value, average_value = result
# print(f"Minimum : {min_value}, maximum : {max_value}, total : {total_value}, average : {average_value}")

# Function can call another function
'''
Syntax:
def first_function():
    code to be executed
    def second_function():
        code to be executed
    we can call another function based on the requirements

'''
# def fun1():
#     print("This is fun1")

# def fun2():
#     print("This is fun2")
#     fun1()

# fun2()

# def multiply(a, b):
#     return a*b

# def add_and_multiply(a, b,x):
#     addition_result = a+b
#     multiplication_result = multiply(addition_result,x)
#     return multiplication_result

# result = add_and_multiply(10,20,30)

# print(f"Result : {result}")

# Function are first class objects
'''
Function are first class objects means they can be treated like any
other objects such as integers, strings or lists
- We can assign a function to variables
- We can pass function as a parameter to another function
- We can define one function inside another function
- Even the function can return another function
'''

# def function1():
#     print("This is a function1")

# # Assign a function to a variable
# res = function1

# #call function
# res()

# def square(x):
#     return x**2

# def cube(x):
#     return x**3

# def apply_operation(fnc, x):
#     return fnc(x)

# result1 = apply_operation(square, 5)
# result2 = apply_operation(cube, 3)

# print(f"Square is {result1} and cube is {result2}")

# Formal argument and Actual argument
'''
Formal arguments are variables that will hold the valued passed to the function
Actual arguments are also known as arguments to the function which are values 
passed to the function when it is called

'''

# Formal arguments
# def welcome(name, age):
#     print(f"Welcome {name}, you are {age} years old")

# welcome("Sam", 45)# Actual arguments

# Positional arguments
'''
Positional arguments are passed to the function based on their position or order
If there are 3 formal arguments in function definition, then we need to send 3 actual arguments
while calling the function
'''

# def fnc1(x,y):
#     return x+y

# res = fnc1(2,1)
# print(f"Result : {res}")

# Default arguments

# def greet(name, age=35):
#     print(f"Welcome {name}, you are {age} years old")

# greet("Bhauraj")
# greet("Sam",44)

# def greet(name="Sam", age=35):
#     print(f"Welcome {name}, you are {age} years old")

# greet()
# greet("Bhauraj")
# greet("Bhauraj",37)

# in the below example we cannot write only default values in the beginningdef greet(name="Sam", age=35):
# def greet(name="Sam", age): # Error non default arguments should be there first
#     print(f"Welcome {name}, you are {age} years old")

# greet()
# greet("Bhauraj")
# greet("Bhauraj",37)

# Keyword arguments
'''
Keyword arguments are passed to a function using the name of the parameter
as a key-value pair.
The order of arguments does not matter as long as they are specified by their
parameter names
'''

# def cal_total(quantity, price):
#     return quantity*price

# total = cal_total(quantity=5, price=10)
# total2= cal_total(price=15, quantity=4)

# print(f"Total : {total}")
# print(f"Total2 : {total2}")

# def details(id, name):
#     print(f"ID : {id} \n Name : {name}")

# details(1001, name="Sam")

# positinal arguments always should come first before keyword arguments, otherwise error comes
# details(name="Kiran", 2000)

# Variable length arguments
'''
Variable length arguments are used when we don't know how many arguments will be passed 
to the function

The variable length arguments is an argument that can accept any number of values, which
is written with a * befor the variable in function definition

Syntax:
def function(*a):
    code to be executed
'''

# def tot_cost(a, *b):
#     sum = 0
#     for i in b:
#         sum += i
#     print(a+sum)

# tot_cost(10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 21)
# tot_cost(10, 20, 30)
# tot_cost(10)
# tot_cost(10, )

# def total_cost(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum

# result = total_cost(3,6,8,10,10,10)
# print(result)

# Keyword variable length arguments
'''
Just as variable length arguments, there are keywrd variable length arguments
that are in key-value pairs

Syntax:
def function(** args):
    code to be executed

**args is keyword variable argument, so internally it represents a dictionary object
which stores the data in the forms of Key-value pairs

'''

# def print_display(** kwrds):
#     r=kwrds
#     print(f"{r}{type(r)}")
#     print(kwrds)
#     for k,v in kwrds.items():
#         print(f"key is {k} : value is {v}")

# print_display(a=12, b=44, c=55)
# print_display(empid=2121, empName="Suresh", empAge =55)

# Global keyword
'''
Global keyword is used to indicate that a variable inside a function should refer to a
global variable with the same name, rather than creating a new local variable within
the function scope. This is necessary when we want to modify a global variable from within
a function

'''
# global_var = 10

# def modify_global():
#     global global_var
#     global_var = 20
#     print(f"Inside the function {global_var}")

# print(f"Before the function {global_var}")
# modify_global()
# print(f"After the function {global_var}")

# globals() function
'''
This function returns a dictionary representing the current global symbol table.
The symbol table contains information about all the global variables and their corresponding
values.
So globals() function can be useful when we want to inspect or manipulate global variables
dynamically at runtime.

'''
# global_var=10
# def modify_global():
#     global global_var
#     global_var = 55

# def print_global_variables():
#     print(f"Global variables: {global_var}")

# print(f"Before modification: {global_var}")
# modify_global()
# print(f"After modification: {global_var}")
# print(f"Global variable before update: {globals()}")
# globals()["global_var"] = 101
# print(f"Global variable before update: {globals()}")
# print_global_variables()

# Recursive function - a function which is called by its self
# Factorial number
'''
factorial(5) = 5 * factorial(4)
factorial(4) = 4 * factorial(3)
factorial(3) = 3 * factorial(2)
factorial(2) = 2 * factorial(1)
1 * factorial(0) = 5 * 4 * 3 * 2 * 1
'''
# def factorial(n):
#     if n==0:
#         result = 1
#     else:
#         result = n*factorial(n-1)

#     return result

# result = factorial(5)

# print(f"Factorial of 5 is {result}")

# Lambda function
'''
A lambda function  is a small anonymous function that can have any number of arguments
but can only have one expression

Lambda expression or lambda function or lambda from

Lambda function are defined using the lambda keyword and they are commonly used when we
need a simple function for a short period of time.
Syntax:

lambda arguments : expression
'''

# add = lambda x,y : x + y

# result = add(10,20)

# print(f"Result : {result}")

# square = lambda x : x*x

# result = square(10)

# print(f"Square of 10 is {result}")

'''
Points:
- A lambda function can take any number of arguments but should have only one expression
- It takes the parameters and does some operation on them and returns the result just the
same as normal function
- the lambda function, mostly can be used in combination with other functions such as
map(), filter() etc..
- It can be used for only simple functions but not for complex functions and it improves
readability of the code.

'''
# filter() function
'''
filter() function allows us to filter the elements from a sequence(list, tuple or string)
based on a given function(predicate)
The function takes 2 arguments
- The predicate function
- the iterable to filter.

Syntax:
filter(function, iterable)

- A function that takes an element from the iterable as input and returns either True or False
'''

# def iseven(number):
#     return number%2==0

# numbers = [1,2,3,4,5,6,7,8,9,10]
# even_number = filter(iseven, numbers)
# print(even_number)
# print(list(even_number))

# numbers = [-2, -1, 0, 3,44, 55, -6]
# positive_number = filter(lambda x: x > 0, numbers)

# print(positive_number)
# print(list(positive_number))

# map() function
'''
map() function allows us to apply a given function to each item in a iterable(ex : list,
tuple or string) and returns a new iterator containing the results.

Syntax:
map(function, iterable)

'''

# def square(c):
#     return c**2

# numbers=[1,2,3,4,5,6,7,8,9,10]

# square_numbers = map(square, numbers)
# result = list(square_numbers)
# print(result)

# words=["A", "B", "C", "D", "E", "F", "G", "H"]
# capitalize = map(lambda x: x.swapcase(), words)
# print(list(capitalize))

'''
The reduce() function is a  built in function from the "functools" module that
allows to reduce a sequence(ex: list, tuple or string) to a single value by
applying a given function cumulatively to the items in the sequence.

Syntax:

functools.reduce(function, iterable[,initializer])

initializer is a optional value
If provided the function will start with this initial value

'''

# from functools import reduce

# def add(x,y):
#     return x+y

# numbers=[10,20,30,40,50,60,70,80]
# result = reduce(add, numbers)
# print(f"Result is : {result}")


# Decorators
'''
A decorator is a function that accepts a function as a parameter and returns a
function. Decorators are useful to perform some additional processing required 
by a function.

Extension function
'''
# Example 1
# def decor(func):
#     def inner_function(x,y):
#         if x<0:
#             x=0
#         if y<0:
#             y=0

#         return func(x,y)
    
#     return inner_function

# def add(a,b):
#     return a + b

# add1 = decor(add)
# print(add1(20,30))
# print(add1(20,20))

# Example 2

# def decor(func):
#     def inner_function(x,y):
#        if x<0:
#            x=0
#        if y<0:
#              y=0

#        return func(x,y)
#     return inner_function

# @decor
# def add(a,b):
#     return a+b

# @decor
# def sub(a,b):
#     return a-b

# print(add(30,-40))
# print(add(30,40))

# print(sub(30,-40))
# print(sub(30,40))

# generators()
'''
Generators are like functions which give us a sequence of values one as an 
iterable, it contains yield statement just like as function contain
return statement.
'''
# def fnc():
#     yield "ZZZ"
#     yield "AAA"

# res = fnc()
# print(res)

# print(type(res))

# for g in res:
#     print(g)

# Example 2
# def fnc(a,b):
#     while a<=b:
#         yield a
#         a+=1

# res = fnc(10, 20)

# for g in res:
#     print(g)

# next function
# We can use next function on the iterator returned by the generator, if we want to
# retrive elements from the generator

def fnc():
    yield "ZZZ"
    yield "AAA"

res=fnc()
print(next(res))
print(next(res))