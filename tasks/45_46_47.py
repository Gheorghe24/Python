# 45. Write a Python program to call an external command. 

import subprocess
return_code = subprocess.call(['ping', 'localhost'])
print("Output of call() : ", return_code)


# 46. Write a python program to get the path and name of the file that is currently executing. 


# 47. Write a Python program to find out the number of CPUs using. 

import os
  
  
# Get the number of CPUs
# in the system using
# os.cpu_count() method
cpuCount = os.cpu_count()
  
# Print the number of
# CPUs in the system
print("Number of CPUs in the system:", cpuCount)