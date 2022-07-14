# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them. 
name = str(input())
name = name.split()
print(name[1] + ' ' + name[0])