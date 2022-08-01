# 57. Write a Python program to get execution time for a Python method. 

import time

def execution_time(n):
    # get the start time
    st = time.time()

    # 58. Write a Python program to sum of the first n positive integers. 

    # main program
    # find sum to first n numbers
    sum_x = 0
    for i in range(1, n + 1):
        sum_x += i

    # wait for 3 seconds
    time.sleep(3)
    print('Sum of first 1 million numbers is:', sum_x)

    # get the end time
    et = time.time()

    # get the execution time
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')

# 59. Write a Python program to convert height (in feet and inches) to centimeters. 

print("Input your height: ")
h_ft = int(input("Feet: "))
h_inch = int(input("Inches: "))
 
h_inch += h_ft * 12
h_cm = round(h_inch * 2.54, 1)
 
print("Your height is : %d cm." % h_cm)
