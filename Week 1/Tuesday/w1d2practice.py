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

# String Utilities and Functions

print("String Util")
print("New Line: String \n Util")
print("Tab Space: String \t Util")

seperator = "#"
mystring = "string Functions"
print("Lower Case: " + mystring.lower())
print("Upper Case: " + mystring.upper())
print("Joining Strings with a seperator: " + seperator.join(("Str1","str2","str3")))
print("Length of the String: " + str(len(mystring)))
print("Find character at position in string: " + mystring[0])
print("Find position: " + str(mystring.index("r")))

# print("Find the sub string between the positions mentioned" + mystring.find("s", 1, 20))
