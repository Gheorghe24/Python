import os

name = "/mnt/d/Python/code_bro12hrs/test.txt"
folder = "/mnt/d/Python/lab1"
if os.path.exists(folder):
    print("That location exists")
    if os.path.isfile(folder):
        print("That is a file")
    elif os.path.isdir(folder):
        print("It's a folder")
else:
    print("That location doesn't exists")