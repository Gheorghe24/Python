# 33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero. 

def sum_3(a,b,c):
    if a == b and b == c :
        return 0
    return a + b + c

# 34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20. 

def sum_3(a,b):
    sum = a + b

    if a<=20 and a>=15:
        sum = 20

    return sum

# 35. Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5. 

def equal(a,b):
    if a == b or a+b == 5 or abs(a-b) == 5:
        return True
    return False