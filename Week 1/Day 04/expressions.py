import math


def calc_math_expression(num1, num2, operator) -> object:
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == ':':
        if num1 == 0 or num2 == 0:
            return None
        else:
            return num1 / num2
    else:
        return None


def calc_math_expression_from_str(str_input):
    values = str_input.split(" ")
    print(values)
    return calc_math_expression(float(values[0]), float(values[2]), values[1])


def find_largest_and_smallest_numbers(num1, num2, num3):
    # if num1 > num2 and num1 > num3:
    #     if num2 > num3:
    #         return num1, num3
    #     else:
    #         return num1, num2
    # elif num2 > num3:
    #     if num1 > num3:
    #         return num2, num3
    #     else:
    #         return num2, num1
    # else:
    #     if num1 > num2:
    #         return num3, num2
    #     else:
    #         return num3, num1
    input_numbers = [num1, num2, num3]
    return max(input_numbers), min(input_numbers)


def quadratic_equation_solver(a, b, c):
    if a == 0 or (pow(b, 2) < (4 * a * c)):
        return None, None

    q = math.sqrt(pow(b, 2) - (4 * a * c))
    solution1 = ((-b) + q) / (2 * a)
    solution2 = ((-b) - q) / (2 * a)
    if solution1 != solution2:
        return solution1, solution2
    else:
        return solution1, None


def quadratic_equation_solver_from_user_input():
    str_input = input("Please enter 3 numbers separated by space: ")
    numbers = str_input.split(" ")
    return quadratic_equation_solver(float(numbers[0]), float(numbers[1]), float(numbers[2]))


def temp_checker(min_temp, temp_1, temp_2, temp_3):
    count = 0
    templist = [temp_1, temp_2, temp_3]
    for index in templist:
        if min_temp < index:
            count += 1
    if count >= 2:
        return True
    else:
        return False


# print(quadratic_equation_solver_from_user_input())
