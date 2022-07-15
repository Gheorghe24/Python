
# 30. Write a Python program that will accept the base and height of a triangle and compute the area. 

def area(base,height):
    return base*height/2

# 31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers. 

import math
def gcd_2(a,b):
    return math.gcd(a,b)

# 32. Write a Python program to get the least common multiple (LCM) of two positive integers. 

def lcm_2(a,b):
    return a*b/gcd_2(a,b)