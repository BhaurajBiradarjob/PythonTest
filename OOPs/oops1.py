'''
Features : 

Class
Object
Encapsulation
Inheritance
Abstraction
Polymorphism
Abstract class

'''
'''
Synatx:

Class Classname:
    Constructor
    Variables
        - instance variables
        - static variables
        - local variables

    Methods:
        - instance methods
        - static methods
        - local methods

'''

# class Employee:
#     def display(self):
#         print(self)
#         print("This is a method inside a class Employee")

'''
display method has a parameter named self and self is a default variable that refers to a
current class object or the current instance of a class

- By using self we can initialize the instance variable inside the constructor
- By using self variables we can access instance methods and variables
- It contains the address of the current object being referred
'''
# emp_obj = Employee()
# emp_obj.display()

# Constructor
'''
Constructor is a method which will invoked by default whenever object of a class is created

Syntax:
def __init__(self):
    code to be executed

Constructor is not mandatory for a class, it is completely based on our requirement
whether to have constructor or not.

At the time of object creation if any initialization is required then we should go for
a constructor, else it is not needed, so without a constructor also python is valid
'''
# class Employee:
#     def __init__(self):
#         print("This is a constructor")

# emp_obj = Employee()
# emp_obj.__init__()
# print(dir(emp_obj))

# Non-parameterized constructor
# class Student:
#     def __init__(self):
#         self.id=22
#         print(f"student id is: {self.id}")
#         print(self)

# s1 = Student()
# s2 = Student()
# s3 = Student()

# Parameterized Constructor
# class Employee:
#     def __init__(self, id):
#         self.id=id
#         print(f"Employee id is: {self.id}")
#         print(self)

# e1 = Employee(22)
# e2 = Employee(33)

# print(type(e1))
# print(type(e2))

# class Student:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name

#     def display(self):
#         print(f"Student name is {self.name}")
#         print(f"Student id is {self.id}")

# s1 =  Student(10, "Mahesh")
# s2 = Student(20, "Akshaya")

# s1.display()
# s2.display()

# print(id(s1))
# print(id(s2))

# Example 2
# class Student:
#     def __init__(self):
#         self.id=44
#         self.name="Mahesh"
#         self.subject="AI"
#         print(f"Inside constructor\n Student name : {self.name} \n Subject is :{self.subject}")

# s1 = Student()
# print(f"Student name is : {s1.name} Subject : {s1.subject}")
# print(s1.__dict__)

# We can declare and initialize instance variables inside instance method by using
# self variables

# class Student:
#     def m1(self):
#         self.a=11
#         self.b=22
#         self.c=45
#         self.name="Mahesh"
#         print(f"a:{self.a} b:{self.b} c:{self.c} name:{self.name}")

# s1 = Student()
# s1.m1()
# print(s1.__dict__)

# We can declare and initialize instance variables by using object name

# class Employee:
#     def __init__(self) :
#         print("This is constructor")
#     def m1(self):
#         print("This is instance method")

# e1 = Employee()
# e2 = Employee()
# e1.m1()
# e1.Name = "Mahesh"
# e1.Gender = "Male"
# e1.Salary = 65000

# e2.Name = "Akshay"
# e2.Gender = "Male"
# e2.Salary = 25000

# print(f"First Employee details")
# print(f"Name : {e1.Name} Gender : {e1.Gender} Salary : {e1.Salary}")

# print(f"Second Employee details")
# print(f"Name : {e2.Name} Gender : {e2.Gender} Salary : {e2.Salary}")

# print(e1.__dict__)
# print(e2.__dict__)

# Static variables
'''
If the value of a variable is not changing from object to object, such type of
variables are called static variables.

We can access 
'''
    