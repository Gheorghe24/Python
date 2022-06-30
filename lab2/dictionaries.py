d = {}
d = dict()
 
# a dictionary with keys and values can be declared as follows:
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
 
# adding a new key to a dictionary:
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
 
print("dictionary")
# looping through a dictionary:
for key in d:
   print(key)  # print only key
   print(key, d[key])  # print key and value d[key]
 
print("using key and value")
# looping using the key and value:
for key, value in d.items():
    print(key, value)
 
# to verify if a dictionary has a specific key use the get() function:
if d.get('a'):  # verify if the dictionary contains the key 'a'
    print('ok')
else:
    print('not found')
 
# alternative
if 'a' in d:
    print('ok')
else:
    print('not found')
 
# counting the number of times a letter appears in a string:
s = [1, 3, 5 , 2, 1, 1, 5]
d = {}
for elem in s:  # pass through all the characters in the string
    if elem in d:  # verify if the character exists in the dictionary
        d[elem] += 1  # if it exist add 1 to the value for that character
    else:  # if it doesn’t exist initialize a new key with the value of the character
        d[elem] = 1  # and initialize the value (which is the counter) to 1

print("LAST")
for key, value in d.items():
    print(key, value)