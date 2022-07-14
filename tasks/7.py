# Write a Python program to accept a filename from the user and print the extension of that. 
# Sample filename : abc.java
# Output : java

import os

# unpacking the tuple
file_name, file_extension = os.path.splitext("./ionel.java")
print(file_extension)