s = [1, 3, 5 , 2, 1, 1, 5]
d = {}
for elem in s:  # pass through all the characters in the string
    if elem in d:  # verify if the character exists in the dictionary
        d[elem] += 1  # if it exist add 1 to the value for that character
    else:  # if it doesn’t exist initialize a new key with the value of the character
        d[elem] = 1  # and initialize the value (which is the counter) to 1

print("Frecquency of numbers in list")
for key, value in d.items():
    print(key, value)