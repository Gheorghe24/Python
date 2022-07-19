
try:
    with open('//mnt//d//Python//code_bro12hrs//test.txt') as file:
        print(file.read())

except FileNotFoundError:
    print("That file was not found :( ")

text = "yooo\nThis is some text\nhave a good one"
try:
    with open('//mnt//d//Python//code_bro12hrs//test.txt','a') as file:
        file.write(text)

except FileNotFoundError:
    print("That file was not found :( ")


