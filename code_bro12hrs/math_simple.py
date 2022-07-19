# str.format() = optional method that gives users more control when displaying

from numpy import number


animal = "cow"
item = "moon"

print("The {} jumped over the {}".format(animal,item))

text = "The {} jumped over the  {}"

print(text.format(animal,item))

name = "Bro"

print("Hello, my name is {:<10}. Nice to meet you".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name))
print("Hello, my name is {:>10}. Nice to meet you".format(name))
print("Hello, my name is {:^10}. Nice to meet you".format(name))

number = 3.1415
numberr = 1000
print(f"The number pi is {number:.2f}")
print(f"The number is {numberr:b}")
print(f"The number is {numberr:o}")
print(f"The number pi is {numberr:X}")