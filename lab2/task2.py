from hashlib import new
import math
list1 = [1, 3, 4, 5, 8]
list3 = [1, 3, -4, 5, -8, -12]
weights1 = [0.2, 0.3, 0.6, 0.1, 0.5]
list2 = [1, 3, 4, 5, 7, 8]
 
# function to compute the arithmetic mean of a list
 
def my_mean(v):
    s_elem = sum(v)
    n_elem = len(v)
    return s_elem / n_elem
 
# function to compute the weighted arithmetic mean of a list
 
def my_pmean(v, p):
    s_pond = sum(p)
    i = 0
    s_lp = 0
    while i < len(v):
        s_lp += v[i] * p[i]
        i += 1
    return s_lp / s_pond
 
# function to compute the variance and standard deviation of a list
 
def my_stdvar(v):
    s = 0
    m = my_mean(v)
    n = len(v)
    for elem in v:
        s += (elem - m)**2
    return s / n, math.sqrt(s / n)
 
# function to compute the L2-norm normalization for list
 
def l2norm(v):
    new_list = []
    s = 0
    # compute the L2 norm
    for elem in v:
        s += elem**2
    s = math.sqrt(s)
 
    # list normalization using the L2 norm
    # for elem in v:
    #     new_elem = elem / s
    #     new_list.append(new_elem)

    new_list = [x/s for x in v]
 
    # TODO: same task with list comprehension    
 
    return new_list


list = l2norm(list1)
for elem in list:
    print(elem)
