small = 2
regular = 5
big = 6
 
user_budget = input('What is your budget? ')
 
try:
   user_budget = int(user_budget)
except:
   print('Please enter a number')
   exit()
 
if user_budget > 0:
   if user_budget >= big:
       print('You can afford the big coffee')
       if user_budget == big:
           print('It\'s complete')
       else:
           print('Your change is', user_budget - big)
   elif user_budget == regular:
       print('You can afford the regular coffee')
       print('It\'s complete')
   elif user_budget >= small:
       print('You can buy the small coffee')
       if user_budget == small:
           print('It\'s complete')
       else:
           print('Your change is', user_budget - small)