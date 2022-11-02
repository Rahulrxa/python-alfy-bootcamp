# # Variable Initialization

# character_name = "John"
# character_age = "35"
# print("Name: " + character_name + "!")
# print("Age: " + character_age + ".")
# print("Confirm Name: " + character_name + "!")
# print("Confirm Age: " + character_age + ".")
#
# # ------------------------------------------------------------------------------
#
# # Updating variables

# character_name = "John"
# character_age = "35"
# print("Name: " + character_name + "!")
# print("Age: " + character_age + ".")
# character_name = "Tom "
# character_age = "40"
# print("Confirm Name: " + character_name + "!")
# print("Confirm Age: " + character_age + ".")
#
# # ------------------------------------------------------------------------------
#
# # Datatypes
#
# string = "Tom"
# integer = 50
# floating_point = 540.2155
# boolean_option_1 = False
# boolean_option_2 = True
#
# print(string)
# print(integer)
# print(floating_point)
# print(boolean_option_1)
# print(boolean_option_2)
#
# ------------------------------------------------------------------------------

# # String Utilities and Functions
#
# print("String Util")
# print("New Line: String \n Util")
# print("Tab Space: String \t Util")
#
# seperator = "#"
# mystring = "string Functions"
# print("Lower Case: " + mystring.lower())
# print("Upper Case: " + mystring.upper())
# print("Joining Strings with a seperator: " + seperator.join(("Str1", "str2", "str3")))
# print("Length of the String: " + str(len(mystring)))
# print("Find character at position in string: " + mystring[0])
# print("Find position: " + str(mystring.index("r")))
# print("Replace a part of the string: " + mystring.replace("string", "STR"))

# # ------------------------------------------------------------------------------

# # Integer/Number Utilities and Functions

# from math import *
#
# Num_1 = 6
# Num_2 = 8
# Num_3 = 5
# Num_4 = -5
# Num_5 = 1.50
# print(Num_1 + Num_3)
# print(Num_2 * Num_3 + Num_3)
# print("Total of all numbers: " + str(Num_3 + Num_2 + Num_1))
# print("Print absolute value of the number: " + str(abs(Num_4)))
# print("Print power of the first number: " + str(pow(Num_3, 2)))
# print("Returns largest of all numbers: " + str(max(Num_3, Num_4, Num_5, Num_2, Num_1)))
# print("Returns smallest of all numbers: " + str(min(Num_3, Num_4, Num_5, Num_2, Num_1)))
# print("Round of Value: " + str(round(Num_5)))
# print("Floor of Value: " + str(floor(Num_5)))
# print("Top of Value: " + str(ceil(Num_5)))
# print("Square root of : " + str(sqrt(36)))

# # ------------------------------------------------------------------------------

# # Input from the user

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print ("Hello " + name + "! your age is "+ age)

# # Building a basic calculator

# number1 = float(input ("Enter a number: "))
# number2 = float(input ("Enter another number: "))
#
# result = number1 + number2
#
# print("Result: " + str(result))

# # ------------------------------------------------------------------------------

# # Mat Libs with Format Function

# color = input("Enter a color")
# sport = input("Enter a favorite sport")
# name = input("Enter name of a favorite team")
#
# print("{2} wore a {0} jersey and scored a lot in {1} the other day".format(color,sport,name))

# # ------------------------------------------------------------------------------

# # Lists

# Movies = ["Interstellar", "Inception", "Dunkirk", "Memento", "Tenet"]
#
# print("All movies in the list: " + str(Movies))
# print(Movies[0])
# print(Movies[-1])
# print(Movies[1:])
# print(Movies[1:3])
#
# Movies[0] = "Batman"
# print(Movies)
#
# Actors = ["Leo", "Tom", "Mathew", "Christian", "Harry","Harry", "Robert"]
# print(Actors)
#
# Movies.append("Interstellar")  # adds a element value at the end
# print(Movies)
#
# Movies.insert(1, "Prestige")  # inserts a new element at a given position
# print(Movies)
#
# Actors.remove(Actors[1])  # removes teh selected element
# print(Actors)
#
# Actors.pop()  # removes the last element
# print(Actors)
# print(Actors.index("Harry")) # prints the index number, if the mentioned name is on the list
# print(Actors.count("Harry")) # prints the count of value mentioned
#
# Actors.sort() #sorts the list
# print(Actors)
#
# Actors.reverse() # reverse sorts the list
# print(Actors)
#
# Movies.extend(Actors)  # merges both lists
# print(Movies)
#
# Movies2=Movies.copy()
# print(Movies2)

# # ------------------------------------------------------------------------------

# # Tuples
# # Tuples are Data Structures that are very similar to lists, major difference is that tuple cannot be edited at all

# coordinates = (33.305,30.903)
# print(coordinates)
# print(coordinates[1])
#
# # List of Tuples
#
# coordinates = [(33.34,33.36), (30.5,34.5)]
# print(coordinates)
# print(coordinates[0])
# print(coordinates[0][1])

# # ------------------------------------------------------------------------------

# # Functions

# def greetings():
#     print("Hello User")
#     # defining the function
#
#
# def greetings_name(name):
#     print("Hello " + name)
#
#
# greetings()  # calling the function
# greetings_name("Rahul")


# # ------------------------------------------------------------------------------

# # Return Statements

def cube(number):
    cuberoot = number * number * number
    return cuberoot


print(cube(3))
