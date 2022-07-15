# 36. Write a Python program to add two objects if both objects are an integer type. 

def add_obj(a,b):
    if type(a) == type(b) :
        return a+b

# 37. Write a Python program to display your details like name, age, address in three different lines. 

def personal_details():
    name, age = "Gheorghe", 20
    address = "Moldova, Chisinau :)"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))

# 38. Write a Python program to solve (x + y) * (x + y). 
# Test Data : x = 4, y = 3
# Expected Output : (4 + 3) ^ 2) = 49

def equation(a,b):
        return (a+b)**2

