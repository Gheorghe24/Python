# # 39. Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years. 
# # Test Data : amt = 10000, int = 3.5, years = 7
# # Expected Output : 12722.79
# The formula for future value with compound interest is FV = P(1 + r/n)^nt.
# FV = the future value;
# P = the principal;
# r = the annual interest rate expressed as a decimal;
# n = the number of times interest is paid each year;
# t = time in years.

from urllib3 import Retry


def value(amt,int,years):
    return amt*((1+(0.01*int)) ** years)


# # 40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2). 
import math
def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

# # 41. Write a Python program to check whether a file exists. 

import os.path
def exists(name):

    return os.path.exists(name)