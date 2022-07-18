# 51. Write a Python program to determine profiling of Python programs. 
# Note: A profile is a set of statistics that describes how often and for how long various parts of the program executed. These statistics can be formatted into reports via the pstats module.

import cProfile
def sum():
    print(8+2)

cProfile.run('sum()')

# 52. Write a Python program to print to stderr. 

import sys
sys.stderr.write("This is an error msg\n")

# 53. Write a python program to access environment variables. 

# Import os module
import os

# Iterate loop to read and print all environment variables
print("The keys and values of all environment variables:")
for key in os.environ:
    print(key, '=>', os.environ[key])

# Print the value of the particular environment variable
print("The value of HOME is: ", os.environ['HOME'])