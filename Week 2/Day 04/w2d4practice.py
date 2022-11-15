# # Exception Handling in Python
#
#
# number = int(input("Enter a number: "))  # Entering a string here returns an exception
# print(number)
# print("end")
# # --------------------------------------------------------------------------------------------------------------------

# # With Exception handling
# # Generic exception handling, says invalid input for any error occurred in try block
# try:
#     # value=10/0
#     number = int(input("Enter a number: "))  # Entering a string here returns an exception
#     print(number)
#
# except:
#     print("Invalid Input")
# print("End of Program")
# # --------------------------------------------------------------------------------------------------------------------

# # Handling Multiple Exceptions
# try:
#     # value=10/0
#     number = int(input("Enter a number: "))  # Entering a string here returns an exception
#     print(number)
# except ZeroDivisionError:
#     print("Number cannot be divided by 0")
# except ValueError:
#     print("Invalid Input")

# # --------------------------------------------------------------------------------------------------------------------
#
# # Handling Multiple Exceptions with printing the error as returned
# try:
#     value=10/0
#     number = int(input("Enter a number: "))  # Entering a string here returns an exception
#     print(number)
# except ZeroDivisionError as err:
#     print(err)
# except ValueError as err:
#     print(err)

# # --------------------------------------------------------------------------------------------------------------------
#
# # Reading from Files

# # modes of opening files:
# # r= read only
# # w= write
# # a= append information but cannot modify existing information
# # r+ = read and write
#
# employee_file = open("employees.txt", "r")
# print(employee_file.readable())
# # print(employee_file.read())
# # print(employee_file.readline())
# print(employee_file.readlines())
# print(employee_file.readlines()[1])
# employee_file.close()


# # --------------------------------------------------------------------------------------------------------------------
#
# # Writing to Files
# # Append
# employee_file = open("employees.txt", "a")
# employee_file.write("\nNov - 145")
# employee_file.close()

# Write
# employee_file = open("employees1.txt", "w")  # overwrites everything thats in the file or create a new file
# employee_file.write("\nNov - 145")
# employee_file.close()

# Modules and PIP install

# Aliasing is just assigning the values of one variable to other like below
# Aliasing an introduce hard t0 find bugs

# list1 = [1, 2]
# list2 = list1
# list1.append(3)
# print(list2) # newly appended value also gets printed because list2 is also referenced to list1 data whereas if its
# a string variable python creates a new string when the data is modified

# # --------------------------------------------------------------------------------------------------------------------

# # Copy using Copy Module #Deep Vs Shallow copy
# # Shallow Copy: One level deep, only references of nested child objects
# # Deep Copy: Full independent copy
# # Works for Lists, Dictionaries, Tuples and Classes/Objects

# import copy

# list1 = [1, 2, 3, 4]
# list2 = copy.copy(list1)  # creates a separate list from list1
# list2[1] = 3
# print(list1)
# print(list2)


# list1 = [[1, 2, 3, 4], [5,6,7,8]]
# list2 = copy.deepcopy(list1)  # creates a separate list from list1
# list2[0][1] = 3
# print(list1)
# print(list2)

# # --------------------------------------------------------------------------------------------------------------------

# # Scope of Variables
# # LEGB - Local, Enclosing, Global, Built-in

# # Built-in variables are all the default functions that we use in python like min/max/round etc...

# # Local Vs Global

# x = 'global x'
#
#
# def test():
#     global x  # way to tell python that we want to use global x variable in this function
#     y = 'local y'
#     x = 'hgfjk'
#     print(y)
#     print(x)
#
#
# test()
# print(x)

# # Enclosing Scope
# def outer():
#     x = 'outer x'  # this X now has enclosing scope
#
#     def inner():
#         # x='inner x'
#         print(x)
#
#     inner()
#     print(x)
#
#
# outer()


# # All Scopes
x = 'global x' # this x has global scope
def outer():
    x = 'outer x'  # this x has enclosing scope

    def inner():
        x='inner x' # this x has local scope
        print(x)

    inner()
    print(x)


outer()
print(x)