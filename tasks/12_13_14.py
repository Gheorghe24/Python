#  Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.

import calendar
print(calendar.month(2022,7))

# Write a Python program to print the following 'here document'. 
# Sample string :
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example

print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
""")

# Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

from datetime import date

d1 = date(2014, 7, 2)
d2 = date(2014, 7, 11)

delta = d2 - d1

print(delta.days)