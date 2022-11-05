# If Statements

# is_male = False
# is_tall = True
#
# if is_male:
#     print("You are male")
# else:
#     print("You are not male")
#
# # or condition
# if is_male or is_tall:
#     print("You are male or tall or both")
# else:
#     print("You are neither male or tall")
#
# # and condition
# if is_male and is_tall:
#     print("You are tall male")
# else:
#     print("You are either not male or not tall or both")
#
# # else if condition
# if is_male and is_tall:
#     print("You are tall male")
# elif is_male and not(is_tall):
#     print("You are a short male")
# elif not(is_male) and (is_tall):
#     print("You are not a male but tall")
# else:
#     print("You are either not male and not tall")

# ------------------------------------------------------------------------------------------------

# Biggest Number
#
# def biggest_number(num1, num2, num3):
#     if num1 > num2 and num1 > num3:
#         return num1
#     elif num2 > num3:
#         return num2
#     else:
#         return num3
#
#
# print(biggest_number(5, 1, 8))

# ------------------------------------------------------------------------------------------------


# Building a calculator

# def cal(num1, num2, opr):
#     if opr == '+':
#         return num1 + num2
#     elif opr == '-':
#         return num1 - num2
#     elif opr == '*':
#         return num1 * num2
#     elif opr == '/':
#         return num1 / num2
#     else:
#         return None
#
#
# num1 = float(input("Enter a number:"))
# num2 = float(input("Enter another number:"))
# opr = input("Enter a operator:")
# print(cal(num1, num2, opr))

# ------------------------------------------------------------------------------------------------

#  Building a dictionary

# dayConv = {
#     "Sun": "Sunday",
#     "Mon": "Day 01",
#     "Tue": "Day 02",
#     "Wes": "Day 03",
#     "Thur": "Day 04",
#     "Fri": "Friday",
#     "Sat": "Saturday",
#     "Sun": "Sunday",
# }
#
# print(dayConv)
# print(dayConv["Sun"])  # returns error if key does not exist
# print(dayConv.get("sun"))  # returns None if key does not exist


# ------------------------------------------------------------------------------------------------

#  While Loop

# i=1
# while i<=10:
#     print(i)
#     i=i+1
# print("loop complete")

# ------------------------------------------------------------------------------------------------

#  Building a guessing game

# secretword = "Nasa"
# guess = ""
# count=0
# limit =3
#
# while guess!=secretword and count<limit:
#     guess=input("Enter the guess: ")
#     count += 1
#
# if guess == secretword:
#     print("Correct Guess!!")
# else:
#     print("You Lost!!!!!!! Loserrrr!!")


# ------------------------------------------------------------------------------------------------

#  For Loops

# for letter in "Giraffe Academy": # Iterating through string
#     print(letter)
#
# friends= ["Alpha","Beta","Gamma"]
# for friend in friends: # Iterating through List/Array
#     print(friend)
#
# for num in range(10): # Iterating through a range of numbers
#     print(num)
#
# for num in range(3,10): # Iterating through a specific range of numbers
#     print(num)
#
# for num in range(len(friends)): # Iterating through a range of numbers
#     print(friends[num])

# ------------------------------------------------------------------------------------------------

#  Exponent Function

# print(2 ** 3)  # print 2^3 (2 cube)
#
#
# def powerof(num,pow):
#     return num ** pow
#
# print(powerof(2,4))


# def powerloop(num,pow):
#     result =1
#     for x in range(pow):
#         result = result*num
#     return result
#
# print(powerloop(2,2))
