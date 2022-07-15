
# 21. Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user. 
def odd_even(n) :
    if n%2 == 0:
        print("Your number is even")
    else :
        print("Your number is odd")

# 22. Write a Python program to count the number 4 in a given list. 
def count4(list):
    c = 0
    for elem in list:
        if int(elem) == 4 :
            c+=1
    return c 

# 23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2. 

def n_copies(n,string) :
    return string[0:2]*n

