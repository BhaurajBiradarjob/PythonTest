'''
Syntax : 

if condition:
    statements (4 indentation)

'''

# x=int(input("Please enter any value "))
# y=int(input("Please enter any value "))

# if x==y:
#     print("x and y are equal")
#     print("success")

'''
Syntax:
if condition:
    if block
else:
    else block

'''
# x=int(input("Please enter any value "))

# if x>0:
#     print("x is positive number")
# else:
#     print("x is negative number")

#if elif else statement

'''
The if elif statement is used to check multiple conditions and execute the specific
block of statements depending upon the condition amoung them

Syntax:

if condition:
    if block
elif condition1:
    elif block
else
    else block

'''
# marks=int(input("Please enter the marks "))

# if marks >= 85 and marks <= 100:
#     print("A+")
# elif marks >= 60 and marks < 85:
#     print("A")
# elif marks >= 40 and marks < 60:
#     print("B")
# elif marks >= 30 and marks < 40:
#     print("B")
# else:
#     print("Fail")


# Nested if else statements
# username = input("Please enter your username: ")
# password = input("Please enter your password: ")

# if username == "bhauraj":
#     if password == "b1234":
#         print("Login Successfully")
#     else:
#         print("Password Wrong")
# else:
#     print("Invalid username")

marks=int(input("Please enter the marks "))

if marks >= 85 and marks <= 100:
    print("A+")
else:
    if marks >= 60 and marks < 85:
        print("A")
    elif marks >= 40 and marks < 60:
        print("B+")
    elif marks >= 30 and marks < 40:
        print("B")
    else:
        print("Failed, Please try again")