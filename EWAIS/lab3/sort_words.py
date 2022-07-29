#I'm declaring a dictionary
d = {}

with open('random.txt', 'r') as file:
    # reading each line    
    for line in file:
   
        # reading each word        
        for word in line.split():
   
            # displaying the words           
            if word in d:  # verify if the character exists in the dictionary
                d[word] += 1  # if it exist add 1 to the value for that character
            else:  # if it doesn’t exist initialize a new key with the value of the character
                d[word] = 1  # and initialize the value (which is the counter) to 1

#Sorted the dictionary
sorted_dict = sorted(d.items(), key=lambda e: e[1], reverse=True)

#the result is a list
for key in sorted_dict:
    print(key[0] + " " + str(key[1]))