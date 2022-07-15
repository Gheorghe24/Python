# 27. Write a Python program to concatenate all elements in a list into a string and return it. 


import string


def concat(list):
    string = ''.join(list)
    return string

# 28. Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence. 
# Sample numbers list :

# numbers = [    
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527
#     ]

def concat(list):
    for elem in list :
        print(elem)
        if int(elem) == 237:
            return



# 29. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2. 
# Test Data :
lst1 = set(["White", "Black", "Red"])
lst2 = set(["Red", "Green"])
# Expected Output :
# {'Black', 'White'}

def difference(lst1, lst2):
    lst3 = [value for value in lst1 if value not in lst2]
    return lst3

print(difference(lst1, lst2))

