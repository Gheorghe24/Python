# 24. Write a Python program to test whether a passed letter is a vowel or not. 

from argparse import _MutuallyExclusiveGroup


def isvowel(ch) :
    vowel = "AEIOUaeiou"
    if ch in vowel :
        print("is vowel")
    else :
        print("is not")

# 25. Write a Python program to check whether a specified value is contained in a group of values. 
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

def isvowel(value, list) :
    if value in list :
        return True
    else :
        return False

# 26. Write a Python program to create a histogram from a given list of integers. 

import matplotlib.pyplot as plt
 
# list of weights
weights = [30, 50, 45, 80, 76, 55,
           45, 47, 50, 65]
 
# plotting labelled histogram
plt.hist(weights)
plt.xlabel('weight')
plt.ylabel('Person count')
plt.show()
