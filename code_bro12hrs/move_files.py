import os

source = "/mnt/d/Python/code_bro12hrs/file.txt"
destination = "C:\\Users\\user\\Desktop\\test.txt"

try:
    if os.path.exists(destination):
        print("There is another file in here")
        os.remove(destination)
    else:
        os.replace(source,destination)
        print(source+ " was moved")
except FileNotFoundError:
    print("source not found") 