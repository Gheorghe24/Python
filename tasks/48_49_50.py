# 48. Write a Python program to parse a string to Float or Integer. 

string = "2222"
f = float(string)
int = int(string)

# 49. Write a Python program to list all files in a directory in Python. 

from argparse import MetavarTypeHelpFormatter
from os import listdir
from os.path import isfile, join
from ssl import OP_CIPHER_SERVER_PREFERENCE
mypath = "/mnt/d/Python"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)

# 50. Write a Python program to print without newline or space. 
def print(var):
    print(var, end = '')

