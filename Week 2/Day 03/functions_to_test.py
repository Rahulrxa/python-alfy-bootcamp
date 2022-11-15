from math import pi


def calc_area_of_circle(radius):
    if type(radius) not in [int, float]:
        raise TypeError("Radius must be an integer of float")
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return pi * (radius ** 2)
