from functions_to_test import *
import unittest
from math import *


#
# def test_calc_area_of_circle():
#     radius = [2, 0, -3, 2 + 5, 4 + 5j, True, "radius"]
#     message = "Area of circle with r={radius} is {area}"
#
#     for i in radius:
#         area = calc_area_of_circle(i)
#         print(message.format(radius=i, area=area))
#
#
# test_calc_area_of_circle()


class TestCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(calc_area_of_circle(1), pi)
        self.assertRaises(ValueError, calc_area_of_circle, -2)
        self.assertRaises(TypeError, calc_area_of_circle, 3 + 2j)
        self.assertRaises(TypeError, calc_area_of_circle, True)
        self.assertRaises(TypeError, calc_area_of_circle, "radius")
