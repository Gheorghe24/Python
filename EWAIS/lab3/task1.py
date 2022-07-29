import numpy as np
import math

li = []
size = 100
maxn = 10
li = [int(np.random.rand()*maxn) for i in range(size)]


# Python code to illustrate 
# filter() with lambda() to get even numbers

final_list = list(filter(lambda x: (x%2 != 0) , li)) 
print(final_list) 
print(" ")

# Python code to illustrate  
# map() with lambda() to get square numbers

final_list = list(map(lambda x: math.sqrt(x) , final_list)) 
print(final_list) 
print(" ")

# Python code to illustrate  
# reduce() with lambda() for sum of list

from functools import reduce
sum = reduce((lambda x, y: x + y), final_list) 
print (sum) 
