# Write a Python program to display the current date and time.

# Sample Output :
# Current date and time :
# 2014-07-05 14:34:

import time

t = time.localtime()
current_time = time.strftime("%Y-%m-%d %H:%M", t)
print(current_time)