# 18. Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum. 

a, b, c = map(int, input().split())

def sum3(a,b,c) :
    sum = a + b + c
    if a == b and b == c :
        sum*=3
    return sum

sum3(a, b, c)

# 19. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged. 

string = "some string"
if "Is" not in string :
    new = "Is " + string
else :
    new = string
print(new)

# 20. Write a Python program to get a string which is n (non-negative integer) copies of a given string. 

n = 3  #just an example
copied_string = string*3
print(copied_string)
